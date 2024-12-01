from rich.console import Console
import random
from time import sleep


class Loader():
    DOTS = "dots"
    BAR = "aesthetic"
    MONKEY = "monkey"


class TypeDelay():
    INSTANT = 0
    HYPER = 3
    FAST = 10
    NORMAL = 30
    SLUGGISH = 75
    SLOW = 125
    SNAIL = 200


class LogType():
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    COMMS = 'COMMS'


_AUTOPAUSE_TRIGGERS = {',', '.', ';', ':', '!', '?'}
'''
Characters that will trigger a pause if `autopause` is enabled
'''

# Note: Should handle characters that change the cursor position
_WRAPPABLE_CHARACTERS = {" ", "-"}
'''
Characters that a line wrap can be triggered on
'''


class Logger:

    def __init__(self,
                 initial_delay_ms: int = 0,
                 char_delay_ms: int = TypeDelay.INSTANT,
                 sentence_pause_delay_ms: int = 0,
                 max_line_length: int = None,
                 autopause: bool = False):

        self._initial_delay_ms = initial_delay_ms
        self._char_delay_ms = char_delay_ms
        self._sentence_pause_delay_ms = sentence_pause_delay_ms
        self.console = Console()
        self._appending = False
        self._max_line_length = max_line_length
        self._autopause = autopause
        self._cursor_pos = 0

        self.clear()

    def _print(self,
               message: str,
               header: str = None,
               append: bool = False,
               char_delay_ms: int = None,
               initial_delay_ms: int = None,
               sentence_pause_delay_ms: int = None,
               autopause: bool = None,
               style: str = ""):

        if header and not self._appending:
            message = f"{header} {message}"

        if initial_delay_ms is None:
            initial_delay_ms = self._initial_delay_ms

        if char_delay_ms is None:
            char_delay_ms = self._char_delay_ms

        if sentence_pause_delay_ms is None:
            sentence_pause_delay_ms = self._sentence_pause_delay_ms

        if autopause is None:
            autopause = self._autopause

        self._pause_ms(initial_delay_ms)

        for i, char in enumerate(message):

            self._pause_ms(char_delay_ms)
            self.console.print(char, style=style, end='')
            self._cursor_pos += 1

            if self._max_line_length and char in _WRAPPABLE_CHARACTERS:
                if self._cursor_pos >= self._max_line_length:
                    self.console.print()
                    self._cursor_pos = 0

            if autopause and char in _AUTOPAUSE_TRIGGERS:

                # Don't sleep if this punctuation is at the end of the message
                if i != len(message) - 1:
                    self._pause_ms(sentence_pause_delay_ms)

        if not append:
            self.console.print()
            self._cursor_pos = 0

        self._appending = append

    def info(self,
             message: str,
             append: bool = False,
             char_delay_ms: int = None,
             initial_delay_ms: int = None,
             sentence_pause_delay_ms: int = None,
             autopause: bool = None,
             ):
        self._print(message,
                    f"[{LogType.INFO}]",
                    append,
                    char_delay_ms,
                    initial_delay_ms,
                    sentence_pause_delay_ms,
                    autopause)

    def warn(self,
             message: str,
             append: bool = False,
             char_delay_ms: int = None,
             initial_delay_ms: int = None,
             sentence_pause_delay_ms: int = None,
             autopause: bool = None,
             ):
        self._print(message,
                    f"[{LogType.WARNING}]",
                    append,
                    char_delay_ms,
                    initial_delay_ms,
                    sentence_pause_delay_ms,
                    autopause,
                    "yellow")

    def error(self,
              message: str,
              append: bool = False,
              char_delay_ms: int = None,
              initial_delay_ms: int = None,
              sentence_pause_delay_ms: int = None,
              autopause: bool = None,
              ):
        self._print(message,
                    f"[{LogType.ERROR}]",
                    append,
                    char_delay_ms,
                    initial_delay_ms,
                    sentence_pause_delay_ms,
                    autopause,
                    "red")

    def debug(self,
              message: str,
              append: bool = False,
              char_delay_ms: int = None,
              initial_delay_ms: int = None,
              sentence_pause_delay_ms: int = None,
              autopause: bool = None,
              ):
        self._print(message,
                    f"[{LogType.DEBUG}]",
                    append,
                    char_delay_ms,
                    initial_delay_ms,
                    sentence_pause_delay_ms,
                    autopause,
                    "blue")

    def comms(self,
              message: str,
              append: bool = False,
              char_delay_ms: int = None,
              initial_delay_ms: int = None,
              sentence_pause_delay_ms: int = None,
              autopause: bool = None,
              ):
        self._print(message,
                    f"[{LogType.COMMS}]",
                    append,
                    char_delay_ms,
                    initial_delay_ms,
                    sentence_pause_delay_ms,
                    autopause,
                    "green")

    def garbage(self,
                length: int,
                append: bool = False,
                char_delay_ms: int = None,
                initial_delay_ms: int = None):

        # TODO: Some improvements to be made here.
        # if a generated character happens to be special,
        # like \\r or \\n, we need to generate a new one
        message = ""

        for _ in range(length):
            message += chr(random.randint(0, 255))

        self._print(message,
                    append=append,
                    char_delay_ms=char_delay_ms,
                    initial_delay_ms=initial_delay_ms,
                    autopause=False)  # Need to force autopause off, don't want to pause during this

    def spinner(self,
                process_name: str,
                duration_ms: int,
                initial_delay_ms: int = None,
                spinner: str = Loader.DOTS):

        if initial_delay_ms is None:
            initial_delay_ms = self._initial_delay_ms

        self._pause_ms(initial_delay_ms)

        with self.console.status(process_name, spinner=spinner):
            self._pause_ms(duration_ms)

    def set_initial_delay(self, delay_ms: int):
        self._initial_delay_ms = delay_ms

    def set_char_delay(self, delay_ms: int):
        self._char_delay_ms = delay_ms

    def set_pause_delay(self, delay_ms: int):
        self._sentence_pause_delay_ms = delay_ms

    def clear_initial_delay(self):
        self._initial_delay_ms = 0

    def clear_char_delay(self):
        self._char_delay_ms = TypeDelay.INSTANT

    def clear_pause_delay(self):
        self._sentence_pause_delay_ms = 0

    def set_autopause(self, autopause: bool):
        self._autopause = autopause

    def clear(self):
        self.console.clear()

    def _pause_ms(self, duration_ms: int):
        sleep(duration_ms / 1000)

