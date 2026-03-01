#!/usr/bin/env python3
# run set tasks for recentchanges qt gui
import sys
from .dirwalker import main_entry as dirwalker_main
from .findfile import main_entry as findfile_main
from .recentchangessearch import main as recentchanges_main
from .recentchangessearchparser import build_subparser
from .gpgkeymanagement import import_key
from .qtfunctions import load_konsole
from .qtfunctions import load_file_manager
from .qtfunctions import kill_process
from .rntchanges import main as rntchanges_main
# 02/28/2026


def dispatch_internal(argv):
    if not argv:
        return False
    arglen = len(argv)
    if arglen >= 3:
        script = argv[1].lower()
        args = argv[2:]
        if not args:
            print("Insufficient args")
            return False
        cmd = args[0]
        if arglen > 5:

            DISPATCH_MAP = {
                "dirwalker.py": {
                    "hardlink": 9,
                    "scan": 6,
                    "build": 5,
                    "downloads": 10,
                },
                "recentchangessearch.py": recentchanges_main,
                "findfile.py": findfile_main,
                "import": import_key
            }

            entry = DISPATCH_MAP.get(script)
            # os.setsid()
            # p_id = os.getpgid(0)  # print("pid",  p_id)
            if isinstance(entry, dict):
                if cmd not in entry:
                    print(
                        f"Invalid parameter for dirwalker; expected one of: "
                        f"{'/'.join(entry.keys())}, got {cmd}"
                    )
                    sys.exit(1)
                min_args = entry[cmd]
                if len(args) < min_args:
                    print(f"Not enough args for '{cmd}', expected {min_args}, got {len(args)}")
                    sys.exit(1)

                sys.exit(dirwalker_main(args))

            elif entry:

                if script == "recentchangessearch.py":
                    recent_args = build_subparser(script)
                    sys.exit(entry(*recent_args))
                elif script == "findfile.py":
                    sys.exit(entry(args))
                elif script == "import":
                    sys.exit(entry(args))
        elif script == "run":
                if cmd == "filemanager":
                    sys.exit(load_file_manager(*args[1:]))
                if cmd == "terminal":
                    sys.exit(load_konsole(*args[1:]))
                if cmd == "kill":
                    sys.exit(kill_process(*args[1:]))
        sys.exit(rntchanges_main(argv))