import traceback
import bot_config
import bot_logging

from datetime import datetime
from typing import Any, Dict, Optional, Type

from bot_comms import publish_event_card, publish_list
from bot_utils import tool_description, tool_error


from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool


tool_logger = bot_logging.logging.getLogger('ToolLogger')
tool_logger.addHandler(bot_logging.file_handler)


class NoteCreate(BaseTool):
    parameters = []
    optional_parameters = []
    name = "JOURNAL_PAGE_CREATE"
    summary = """Useful for when you need to add a new page to the journal."""
    parameters.append({"name": "notebook", "description": "The name or identifier of the notebook in the journal."})
    parameters.append({"name": "section", "description": "The name or identifier of the section within the notebook."})
    parameters.append({"name": "page", "description": "The page number or identifier within the section."})
    parameters.append({"name": "content", "description": "The text or content to be added to the specified page within the journal."})
    description = tool_description(name, summary, parameters, optional_parameters)
    return_direct = False


    def _run(self, notebook: str = None, section: str = None, page: str = None, content: str = None, publish: str = "True", run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        try:
            ai_summary = ""
            human_summary = []
            
            #code to create a page in onenote using microsoft graph
            #tenant id = bot_config.Ten
            
        except Exception as e:
            #traceback.print_exc()
            tb = traceback.format_exc()
            return tool_error(e, tb, self.description)
    
    async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("JOURNAL_ADD does not support async")

class NoteAppend(BaseTool):
    parameters = []
    optional_parameters = []
    name = "JOURNAL_PAGE_APPEND"
    summary = "Useful for when you need to add an entry to existing page in the journal"
    parameters.append({"name": "notebook", "description": "The name or identifier of the notebook in the journal."})
    parameters.append({"name": "section", "description": "The name or identifier of the section within the notebook."})
    parameters.append({"name": "page", "description": "The page number or identifier within the section."})
    parameters.append({"name": "content", "description": "The text or content to be added to the specified page within the journal."})
    description = tool_description(name, summary, parameters, optional_parameters)
    return_direct = False

    def _run(self, notebook: str = None, section: str = None, page: str = None, content: str = None, publish: str = "True", run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        try:
            ai_summary = ""
            human_summary = []

            
            
        except Exception as e:
            #traceback.print_exc()
            tb = traceback.format_exc()
            return tool_error(e, tb, self.description)
    
    async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("JOURNAL_GET does not support async")

