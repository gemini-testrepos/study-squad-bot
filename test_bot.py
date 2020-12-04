import unittest
from bot import build_bot


class TestStudyBot(unittest.TestCase):
    def test_study_and_reminders(self):
        bot = build_bot()
        res = bot.dispatch('alex', '!remind CS240 Fri-5pm Lab3')
        self.assertIn('CS240', res)
        self.assertIn('Lab3', bot.dispatch('alex', '!schedule'))
        self.assertIn('50m', bot.dispatch('alex', '!study 50'))
