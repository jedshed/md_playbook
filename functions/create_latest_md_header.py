import functions as func
from config import Config as conf
import re


def create_latest_md_header(latest_md_title, meta_description, meta_sitename, meta_publish_date, do_func, do_display):

    func_text = "CREATE LATEST MD HEADER"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### Create latest_md_header
    try:
        latest_md_header = f"# {latest_md_title}\n\n> {meta_description}\n\n{meta_sitename}  \n{meta_publish_date}\n\n***"

        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()

    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    ##### Display latest_md_header
    display_latest_md_header_text = "--- DISPLAY LATEST MD HEADER:"
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
