"""Study Squad Bot wiring and offline test runner."""

from reminders import ReminderBoard
from router import CommandRouter
from sessions import StudyTracker


def build_bot() -> CommandRouter:
    router = CommandRouter(prefix='!')
    board = ReminderBoard()
    tracker = StudyTracker()

    router.register('help', lambda u, a: 'Commands: !remind <course> <time> <note>, !study [min], !top')
    router.register(
        'remind',
        lambda u, a: (
            f'Added reminder for {board.add(a[0], a[1], " ".join(a[2:])).course}'
            if len(a) >= 3 else 'Usage: !remind CS301 Tue-10am Midterm review'
        ),
    )
    router.register('schedule', lambda u, a: board.format_board())
    router.register(
        'study',
        lambda u, a: f'{u} logged study time! Total: {tracker.log_session(u, int(a[0]) if a else 25)}m',
    )
    router.register(
        'top',
        lambda u, a: ', '.join(f'{k}: {v}m' for k, v in tracker.leaderboard()) or 'No sessions yet.',
    )
    return router
