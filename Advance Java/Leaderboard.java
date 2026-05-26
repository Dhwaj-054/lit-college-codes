package leaderboard;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

/**
 * Real-Time Leaderboard implementation.
 * Uses ConcurrentHashMap for thread-safe score storage.
 * Maintains a bounded TreeSet (acting as max-heap) of size 100 for top players, ordered by score descending.
 * TreeSet chosen over PriorityQueue for easier updates on mutable objects.
 * Buckets score deltas into per-minute windows using Instant.truncatedTo(ChronoUnit.MINUTES) for efficient time-based queries.
 */
public class Leaderboard {
    private final ConcurrentHashMap<String, PlayerScore> scores = new ConcurrentHashMap<>();
    private final TreeSet<PlayerScore> top100 = new TreeSet<>(
        Comparator.comparingInt(PlayerScore::getTotalScore).reversed()
                  .thenComparing(PlayerScore::getPlayerId)
    );
    private final ConcurrentHashMap<Instant, ConcurrentHashMap<String, Integer>> minuteDeltas = new ConcurrentHashMap<>();

    /**
     * Ingests a score event, updating the score store, maintaining the top-100 heap, and bucketing deltas.
     * Synchronized to ensure atomic updates to the heap.
     */
    public synchronized void ingest(ScoreEvent event) {
        // Update score store
        PlayerScore ps = scores.computeIfAbsent(event.playerId(), k -> new PlayerScore(k, 0));
        ps.addScore(event.score());

        // Update top-100 heap
        top100.remove(ps); // Remove old instance if present
        if (top100.size() < 100 || ps.getTotalScore() > top100.last().getTotalScore()) {
            top100.add(ps);
            if (top100.size() > 100) {
                top100.pollLast(); // Remove the smallest
            }
        }

        // Bucket delta into per-minute windows
        Instant minute = event.timestamp().truncatedTo(ChronoUnit.MINUTES);
        minuteDeltas.computeIfAbsent(minute, k -> new ConcurrentHashMap<>())
                   .merge(event.playerId(), event.score(), Integer::sum);
    }

    /**
     * Returns the top K players by total score.
     * Uses Stream API for lazy evaluation and sorting.
     */
    public List<PlayerScore> getTopK(int k) {
        return scores.values().stream()
                     .sorted()
                     .limit(k)
                     .collect(Collectors.toList());
    }

    /**
     * Returns rankings for a specific minute, sorted by score descending.
     * Uses Stream with Map.Entry comparator for value-based sorting.
     */
    public List<Map.Entry<String, Integer>> getMinuteRankings(Instant minute) {
        return minuteDeltas.getOrDefault(minute, new ConcurrentHashMap<>())
                          .entrySet().stream()
                          .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
                          .collect(Collectors.toList());
    }

    /**
     * Returns the earliest minute with data, or null if none.
     */
    public Instant getEarliestMinute() {
        return minuteDeltas.keySet().stream().min(Instant::compareTo).orElse(null);
    }

    /**
     * Rebuilds global ranking from all minute windows.
     * Uses flatMap to combine entries, groupingBy for aggregation, and LinkedHashMap to preserve order.
     */
    public Map<String, Integer> getGlobalRankingFromWindows() {
        return minuteDeltas.values().stream()
                          .flatMap(map -> map.entrySet().stream())
                          .collect(Collectors.groupingBy(Map.Entry::getKey,
                                                         LinkedHashMap::new,
                                                         Collectors.summingInt(Map.Entry::getValue)))
                          .entrySet().stream()
                          .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
                          .collect(Collectors.toMap(Map.Entry::getKey,
                                                   Map.Entry::getValue,
                                                   (a, b) -> a,
                                                   LinkedHashMap::new));
    }
}