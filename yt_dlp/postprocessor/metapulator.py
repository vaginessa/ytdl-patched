import json
import re

from ..utils import render_table
from .common import PostProcessor


class MetapulatorPP(PostProcessor):
    """
    Metadata manuplator via commands
    """

    COMMANDS = {}  # command, object

    def __init__(self, downloader=None):
        super().__init__(downloader)
        self.COMMANDS = dict((x.COMMAND_NAME, x()) for x in CLASSES)

    def run(self, info):
        for f in self._actions:
            next(filter(lambda x: 0, f(info)), None)
        return [], info

    def find_command(self, cmd):
        if not cmd:
            return None
        for name, value in self.COMMANDS.items():
            # shortest match
            if name.startswith(cmd):
                return value
        return None


class ShowHelp(Exception):
    pass


class MetapulatorCommand:
    COMMAND_NAME = False
    HELP = ''

    def run(self, pp: MetapulatorPP, info: dict, args: list) -> None:
        raise Exception('Override this method in child classes')


class PrintCommand(MetapulatorCommand):
    """
    Equivalent to --print option but in Metapulator
    """

    COMMAND_NAME = 'print'
    HELP = """\
Prints the content of metadata. You can use the same notation as --print
This accepts multiple queries at a time

Examples:
print title
print "%(subtitles.en.-1.ext)s"
print "%(id.3:7:-1)s" "%(formats.:.format_id)s"

Refer to https://github.com/yt-dlp/yt-dlp#output-template for the query details
"""

    def run(self, pp, info, args):
        info = info.copy()

        def format_tmpl(tmpl):
            mobj = re.match(r'\w+(=?)$', tmpl)
            if mobj and mobj.group(1):
                return f'{tmpl[:-1]} = %({tmpl[:-1]})r'
            elif mobj:
                return f'%({tmpl})s'
            return tmpl

        for tmpl in args:
            pp.to_screen(pp._downloader.evaluate_outtmpl(format_tmpl(tmpl), info))


class ChaptersCommand(MetapulatorCommand):
    """
    Command to manuplate and view chapters
    """

    COMMAND_NAME = 'chapters'
    HELP = """\
Manuplates or displays chapters for this video.
"""

    def run(self, pp, info, args):
        ydl = pp._downloader
        if not args or 'view'.startswith(args[0]):
            # view
            chap = info.get('chapters')
            if not chap:
                pp.to_screen('There are no chapters')
                return

            if not isinstance(chap, list):
                pp.report_warning('Extracted chapters are in unexpected structure. Fix extractor code')
                return

            cs = len(chap)
            pp.to_screen(f'There are {cs} chapters:' if cs > 1 else 'There is one chapter:')
            delim = ydl._format_out('\u2502', ydl.Styles.DELIM, '|', test_encoding=True)
            header_line = ydl._list_format_headers('INDEX', delim, 'START', 'END', delim, 'TITLE')

            table = [[
                ch.get('index'),  # INDEX
                delim,
                ch.get('start_time', 0),  # START
                ch.get('end_time', ydl._format_out('???', ydl.Styles.SUPPRESS)),  # END
                delim,
                ch.get('index'),  # TITLE
            ] for ch in chap]
            tbl = render_table(
                header_line, table, hide_empty=True,
                delim=ydl._format_out('\u2500', ydl.Styles.DELIM, '-', test_encoding=True))
            pp.to_screen(tbl, False)
            return
        elif 'add'.startswith(args[0]):
            # add START END [TITLE]
            return
        elif 'insert'.startswith(args[0]):
            # insert INDEX START END [TITLE]
            return
        elif 'remove'.startswith(args[0]):
            # remove [idx:]INDEX[-INDEX_END]|[t:]TITLE_REGEX
            return
        elif 'sort'.startswith(args[0]):
            # sort
            return
        pp.to_screen(f'Unknown command: {args[0]!r}. Use "help {self.COMMAND_NAME}" to see help')


class SetValueCommand(MetapulatorCommand):
    """
    Command to set a value to a key
    """

    COMMAND_NAME = 'setvalue'
    HELP = """\
Synopsis: setvalue KEY [TYPE] VALUE

Command to set a value to a key.

TYPE can be any of: STRING, INT, FLOAT and JSON
Defaults to STRING.

For INT and FLOAT, the VALUE must be an interger or a decimal number.

For JSON, the VALUE must be a valid JSON.
"""

    def run(self, pp, info, args):
        if len(args) not in (2, 3):
            raise ShowHelp()
        _type = 'string'
        if len(args) == 2:
            key, value_str = args
        elif len(args) == 3:
            key, _type, value_str = args
        _type = _type.lower()
        value = value_str
        if _type == 'int':
            value = int(value_str)
        elif _type == 'float':
            value = float(value_str)
        elif _type == 'json':
            value = json.loads(value_str)
        info[key] = value


class HelpCommand(MetapulatorCommand):
    """
    Command to show help
    """

    COMMAND_NAME = 'setvalue'
    HELP = """\
Synopsis: help [COMMAND]

If COMMAND is not given, it shows all of the available commands.
"""

    def run(self, pp, info, args):
        if not args:
            pp.to_screen('All available commands:')
            pp.to_screen('\n'.join(sorted(pp.COMMANDS.keys())), False)
            return
        cmd = pp.find_command(args[0])
        if not cmd:
            pp.to_screen(f'Command {args[0]!r} not found')
            return
        pp.to_screen(f'Help for {cmd.COMMAND_NAME!r}')
        pp.to_screen(cmd.HELP, False)


CLASSES = (PrintCommand, ChaptersCommand, SetValueCommand, HelpCommand)
