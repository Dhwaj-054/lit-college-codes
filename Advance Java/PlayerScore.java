package leaderboard;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * Mutable aggregate for player scores.
 * Uses AtomicInteger for thread-safe score updates.
 * Implements Comparable for ordering by score descending (higher scores first).
 */
public class PlayerScore implements Comparable<PlayerScore> {
    private final String playerId;
    private final AtomicInteger totalScore;

    public PlayerScore(String playerId, int initialScore) {
        this.playerId = playerId;
        this.totalScore = new AtomicInteger(initialScore);
    }

    public String getPlayerId() {
        return playerId;
    }

    public int getTotalScore() {
        return totalScore.get();
    }

    public void addScore(int delta) {
        totalScore.addAndGet(delta);
    }

    @Override
    public int compareTo(PlayerScore other) {
        // Descending order: higher score first
        return Integer.compare(other.getTotalScore(), this.getTotalScore());
    }

    @Override
    public String toString() {
        return playerId + ": " + getTotalScore();
    }
}