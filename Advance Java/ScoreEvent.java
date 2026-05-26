package leaderboard;

import java.time.Instant;

/**
 * Immutable record representing a score event.
 * Uses record for immutability and concise syntax.
 */
public record ScoreEvent(String playerId, int score, Instant timestamp) {
}