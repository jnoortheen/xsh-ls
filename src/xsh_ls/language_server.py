from pygls.capabilities import COMPLETION
from pygls.server import LanguageServer
from pygls.lsp import (
    CompletionItem,
    CompletionList,
    CompletionOptions,
    CompletionParams,
)

server = LanguageServer()


@server.feature(COMPLETION, CompletionOptions(trigger_characters=[","]))
def completions(params: CompletionParams):
    """Returns completion items."""
    print(params)
    return CompletionList(
        is_incomplete=False,
        items=[
            CompletionItem(label='"'),
            CompletionItem(label="["),
            CompletionItem(label="]"),
            CompletionItem(label="{"),
            CompletionItem(label="}"),
        ],
    )
