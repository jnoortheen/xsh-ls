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
import logging

from arger import Arger

from . import language_server

logging.basicConfig(filename="xsh-ls.log", level=logging.DEBUG, filemode="w")


def cli(tcp=False, ws=False, host="127.0.0.1", port=2007):
    """
        Start Xonsh Language server
    Args:
        tcp: Use TCP server
        ws: Use WebSocket server
        host: Bind to this address
        port: Bind to this port
    """
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
        main,
        prog="xsh-ls",  # for testing purpose. otherwise not required
    )
    arger.run(args)


if __name__ == "__main__":
    cli(ws=True)
