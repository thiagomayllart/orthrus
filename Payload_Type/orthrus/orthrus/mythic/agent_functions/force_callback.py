from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *
from mythic_container.MythicGoRPC import (
    SendMythicRPCResponseCreate,
    MythicRPCResponseCreateMessage,
    SendMythicRPCCallbackUpdate,
    MythicRPCCallbackUpdateMessage,
)
import requests 

class ForceCallbackArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = []

    async def parse_arguments(self):
        pass


class ForceCallbackCommand(CommandBase):
    cmd = "force_callback"
    needs_admin = False
    help_cmd = "force_callback"
    description = "Force a callback from an agent."
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = False
    is_remove_file = False
    is_upload_file = False
    author = "@rookuu"
    argument_class = ForceCallbackArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        r = requests.post("http://localhost:8035/webhook",json={"callback_uuid": task.callback.agent_callback_id, "topic": "mythic.force_callback"})
        print(task.callback.agent_callback_id)

        task.status = MythicStatus.Completed
        return task

    async def process_response(self, response: AgentResponse):
        pass