from mythic_container.MythicCommandBase import *

class SecurityInfoArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = []

    async def parse_arguments(self):
        pass


class SecurityInfoCommand(CommandBase):
    cmd = "security_info"
    needs_admin = False
    help_cmd = "security_info"
    description = "Returns security related information from the device."
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = False
    is_remove_file = False
    is_upload_file = False
    author = "@rookuu"
    argument_class = SecurityInfoArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass