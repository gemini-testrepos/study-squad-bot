"""Lecture and assignment reminder store."""

from dataclasses import dataclass
from typing import List


@dataclass
class Reminder:
    course: str
    when: str
    note: str


class ReminderBoard:
    def __init__(self) -> None:
        self.items: List[Reminder] = []

    def add(self, course: str, when: str, note: str) -> Reminder:
        item = Reminder(course=course.upper(), when=when, note=note)
        self.items.append(item)
        return item

    def format_board(self) -> str:
        if not self.items:
            return "No upcoming reminders."
        return "\n".join(f"- [{r.course}] {r.when}: {r.note}" for r in self.items)
