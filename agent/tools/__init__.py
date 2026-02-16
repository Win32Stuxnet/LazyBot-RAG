"""Tool registry – every tool is imported here for easy discovery."""

from agent.tools.filesystem import (
    list_directory,
    read_file,
    search_files,
    get_file_info,
)
from agent.tools.web import web_search, web_fetch
from agent.tools.confirmations import request_confirmation

# Master list used by the orchestrator to build the LLM tool schema.
ALL_TOOLS = [
    list_directory,
    read_file,
    search_files,
    get_file_info,
    web_search,
    web_fetch,
]
