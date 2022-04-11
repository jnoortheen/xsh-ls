# Why does this file exist, and why not put this in `__main__`?
#
# You might be tempted to import things from `__main__` later,
# but that will cause problems: the code will get executed twice:
#
# - When you run `python -m xsh_ls` python will execute
#   `__main__.py` as a script. That means there won't be any
#   `xsh_ls.__main__` in `sys.modules`.
# - When you import `__main__` it will get executed again (as a module) because
#   there's no `xsh_ls.__main__` in `sys.modules`.

"""Module that contains the command line application."""
import argparse
import logging
import sys

from arger import Arger

from xsh_ls import language_server

PROG = "xsh-ls"


def get_version():
    from importlib_metadata import version

    return version(PROG)


def cli(
    tcp=False,
    ws=False,
    host="127.0.0.1",
    port=2007,
    version=False,
    log_file: str = None,
):
    """
        Start Xonsh Language server
    Args:
        tcp: Use TCP server
        ws: Use WebSocket server
        host: Bind to this address
        port: Bind to this port
        version: Display version info and exit
        log_file: redirect logs to file specified
    """
    if version:
        print(get_version())
        return

    if log_file:
        logging.basicConfig(filename=log_file, level=logging.DEBUG, filemode="w")
    else:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    if tcp:
        language_server.server.start_tcp(host, port)
    elif ws:
        language_server.server.start_ws(host, port)
    else:
        language_server.server.start_io()


def main(args) -> None:
    """
    Run the main program.

    This function is executed when you type `xsh-ls` or `python -m xsh_ls`.

    Arguments:
        args: Arguments passed from the command line.

    Returns:
        An exit code.
    """
    arger = Arger(
        cli,
        prog=PROG,  # for testing purpose. otherwise not required
        add_help=False,
    )
    arger.add_argument(
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="show this help message and exit",
    )
    arger.run(*args, capture_sys=False)


if __name__ == "__main__":
    cli(tcp=True)
