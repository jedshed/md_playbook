import functions as func
from config import Config as conf
import re


def process_latest_md_header(latest_md_header, do_func, do_display):

    func_text = "PROCESS LATEST MD HEADER"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### REGEX TIDY TO END OF LINE
    latest_md_header = re.sub(r'Send tips here.*', '', latest_md_header).strip()

    func.helper_update_remote_line(
        1, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()

    ##### Display processed latest_md_header
    display_latest_md_header_text = "--- DISPLAY PROCESSED LATEST MD HEADER:"
    print(f"{display_latest_md_header_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    if not do_display:
        func.helper_update_remote_line(
            1, f"{'--- DISPLAY ' + func_text:<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()
        return latest_md_header

    if do_display:
        print(f"{conf.seperator2}")
        print(f"{latest_md_header}")
        print(f"{conf.seperator2}")
        func.debug_delay_long()
        return latest_md_header
