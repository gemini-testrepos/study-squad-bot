"""Lightweight command router compatible with Discord message handlers."""

from typing import Callable, Dict, List

CommandFn = Callable[[str, List[str]], str]


class CommandRouter:
    def __init__(self, prefix: str = "!"):
        self.prefix = prefix
        self._commands: Dict[str, CommandFn] = {}

    def register(self, name: str, fn: CommandFn) -> None:
        self._commands[name.lower()] = fn

    def dispatch(self, user: str, message: str) -> str:
        if not message.startswith(self.prefix):
            return ""
        parts = message[len(self.prefix):].strip().split()
        if not parts:
            return ""
        cmd, args = parts[0].lower(), parts[1:]
        handler = self._commands.get(cmd)
        if not handler:
            return f"Unknown command `{cmd}`. Try `!help`."
        return handler(user, args)
