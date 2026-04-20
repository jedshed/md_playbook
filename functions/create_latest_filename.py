''' Create latest filename '''

import functions as func
from config import Config as conf

def create_latest_md_filename(latest_md_title, do_func, do_display):

    ##### Set func_text & do_func check
    func_text = ("CREATE LATEST FILENAME")
    print(f"{func_text:<{conf.fpad}}")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### Create latest_md_filename from latest_md_title and conf.file_ext
    latest_md_filename = f"{latest_md_title}{conf.file_ext}"

    func.helper_update_remote_line(
        1, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()

    ##### Disply latest_md_filename 
    if do_display:
        print(f"--- {latest_md_filename}")
        func.debug_delay_long()
    else:
        print(f"{'--- DISPLAY ' + func_text:<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()

    return latest_md_filename

