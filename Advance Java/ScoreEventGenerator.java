package leaderboard;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Instant;
import java.util.List;
import java.util.Map;
import java.util.Random;

/**
 * Mock CSV generator and main driver for the leaderboard.
 * Generates 10,000 events for 500 players with scores -50 to +150, spread over 15 minutes.
 * Uses Files.lines() for lazy CSV streaming in main() to avoid loading all data into memory.
 */
public class ScoreEventGenerator {
    private static final int NUM_EVENTS = 10_000;
    private static final int NUM_PLAYERS = 500;
    private static final int SCORE_MIN = -50;
    private static final int SCORE_MAX = 150;
    private static final int MINUTES_SPREAD = 15;
    private static final String CSV_FILE = "events.csv";

    public static void main(String[] args) throws IOException {
        // Generate CSV
        generateCSV();

        // Lazy stream CSV and ingest
        Leaderboard leaderboard = new Leaderboard();
        Path csvPath = Paths.get(CSV_FILE);
        Files.lines(csvPath)
             .skip(1) // Skip header
             .map(ScoreEventGenerator::parseLine)
             .forEach(leaderboard::ingest);

        // Print results
        System.out.println("Top 10 Leaderboard:");
        leaderboard.getTopK(10).forEach(System.out::println);

        // First minute rankings (earliest minute with data)
        Instant firstMinute = leaderboard.getEarliestMinute();
        if (firstMinute != null) {
            System.out.println("\nFirst Minute Rankings:");
            leaderboard.getMinuteRankings(firstMinute).stream().limit(10).forEach(e -> System.out.println(e.getKey() + ": " + e.getValue()));
        }

        System.out.println("\nTop 5 from Window Rebuild:");
        leaderboard.getGlobalRankingFromWindows().entrySet().stream().limit(5).forEach(e -> System.out.println(e.getKey() + ": " + e.getValue()));
    }

    private static void generateCSV() throws IOException {
        Random random = new Random();
        Instant start = Instant.parse("2023-01-01T00:00:00Z");
        Instant end = start.plusSeconds(MINUTES_SPREAD * 60);

        StringBuilder sb = new StringBuilder();
        sb.append("playerId,score,timestamp\n");
        for (int i = 0; i < NUM_EVENTS; i++) {
            String playerId = "player" + (random.nextInt(NUM_PLAYERS) + 1);
            int score = random.nextInt(SCORE_MAX - SCORE_MIN + 1) + SCORE_MIN;
            long timestampSeconds = start.getEpochSecond() + random.nextInt((int) (end.getEpochSecond() - start.getEpochSecond()));
            Instant timestamp = Instant.ofEpochSecond(timestampSeconds);
            sb.append(playerId).append(",").append(score).append(",").append(timestamp).append("\n");
        }
        Files.writeString(Paths.get(CSV_FILE), sb.toString());
    }

    private static ScoreEvent parseLine(String line) {
        String[] parts = line.split(",");
        return new ScoreEvent(parts[0], Integer.parseInt(parts[1]), Instant.parse(parts[2]));
    }
}