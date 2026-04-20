from config import Config as conf
from pathlib import Path
import shutil
import time
import sys
import inspect

def helper_update_remote_line(n_up, text):
    # \033[{n_up}A : Jump up
    # \r           : Start of line
    # \033[K       : Wipe everything on that line
    # {text}       : Write your new content
    # \033[{n_up}B : Jump back down
    # \r           : Reset to column 0
    print(f"\033[{n_up}A\r\033[K{text}\033[{n_up}B\r", end="", flush=True)

# # clean one-liner call:
# helper_update_remote_line(
#     5, f"{func_text:<{conf.fpad}} ... DONE")
