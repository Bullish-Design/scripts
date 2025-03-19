import os

from dotenv import load_dotenv

load_dotenv()

# Constants: --------------------------------------------
ENV_LOC = ".env"
ROOT = os.getenv("DEVENV_ROOT")
PYTHON_DIR = os.getenv("PYTHON_DIR")
LOGDIR = ROOT + "/logs"
