from mythic_container.C2ProfileBase import *
from pathlib import Path

class mdm(C2Profile):
    name = "mdm"
    description = "Speaks to a locally hosted MicroMDM server to issue commands using the Apple Push Nofification service."
    author = "@rookuu"
    is_p2p = False
    is_server_routed = False
    mythic_encrypts = False
    server_folder_path = Path(".") / "c2_code"
    server_binary_path = server_folder_path / "server.py"
    parameters = [
        C2ProfileParameter(
            name="callback_host",
            description="Callback Host",
            default_value="https://domain.com",
            verifier_regex="^https:\/\/.+",
        ),
    ]