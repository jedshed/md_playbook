from markitdown import MarkItDown
from config import Config as conf
import functions as func
from pathlib import Path

""" ---- MARKITDOWN INFO -----                  """
""" Uses MarkItDown to fetch and convert a URL  """
""" md.convert loses hyperlinks                 """
""" md.convert_url preserves hyperlinks         """

def create_latest_md_content(latest_url, do_func, do_display):
    func_text = "CREATE LATEST MD CONTENT"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### CREATE LATEST MD CONTENT
    try:
        md = MarkItDown()
        result = md.convert_url(latest_url) # preserves links in content
        latest_md_content = result.text_content
        
    except Exception as e:
        print(f"Failed to {func_text:<{conf.fpad}} {e}")

    func.helper_update_remote_line(
        1, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()

    ##### DISPLAY latest_md_content
    display_latest_md_content_text = "--- DISPLAY latest_md_content"
    print(f"{display_latest_md_content_text:<{conf.fpad}} ...")

    if not do_display:
        func.helper_update_remote_line(
            1, f"{display_latest_md_content_text:<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()
        return latest_md_content

    try:
        print(f"\n{conf.seperator2}\n")
        print(f"{latest_md_content}")
        print(f"\n{conf.seperator2}\n")
        func.debug_delay_long()
    except Exception as e:
        print(f"Failed to {display_latest_md_content_text} {e}")

    return latest_md_content
