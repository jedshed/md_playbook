import functions as func
from config import Config as conf
import socket
import sys

# Connect to Google's public DNS server on port 53
# Timeout is set to 3 seconds to avoid long hangs

def check_internet_connected(do_func) -> None:

    func_text = "CHECKING INTERNET CONECTION"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    #Do Func Check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()
    except Exception as e:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FAIL - EXITING")
        print(f"{e}")
        sys.exit()