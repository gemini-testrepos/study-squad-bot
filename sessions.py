"""Group study check-in and Pomodoro streak tracker."""

from collections import defaultdict
from typing import Dict, List


class StudyTracker:
    def __init__(self) -> None:
        self.minutes: Dict[str, int] = defaultdict(int)

    def log_session(self, user: str, duration_min: int = 25) -> int:
        self.minutes[user] += max(1, duration_min)
        return self.minutes[user]

    def leaderboard(self, limit: int = 5) -> List[tuple[str, int]]:
        return sorted(self.minutes.items(), key=lambda kv: kv[1], reverse=True)[:limit]
