# Check if latest URL in log
import functions as func
from config import Config as conf
from pathlib import Path
import sys
import time

def check_url_in_log(latest_url, do_func,):

    func_text = (f"CHECKING URL IN LOG")
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### Do Func Check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### Do the Check
    try:
        ### Create Path Object
        path_to_log_file = Path(conf.out_folder_log_path) / conf.log_file_name
        check = False # Initialize check so it exists even if file is missing
        if path_to_log_file.is_file():
            with open(path_to_log_file, 'r') as file:
                for line in file:
                    if latest_url in line:
                        check = True

        if check:
            func.helper_update_remote_line(
               1, f"{func_text:<{conf.fpad}} ... URL IN LOG - EXITING")
            sys.exit() # This kills the whole project right here
            func.debug_delay_long()
        else:
            func.helper_update_remote_line(
               1, f"{func_text:<{conf.fpad}} ... URL NOT IN LOG - CONTINUING")
            func.debug_delay_long()

    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")    



