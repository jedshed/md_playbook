from config import Config as conf
import functions as func

def process_latest_md_title(latest_md_title, do_func, do_display):

    ##### func_text
    func_text = "PROCESS LATEST MD TITLE"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### process_latest_md_title
    try:
        latest_md_title = latest_md_title.replace(".", "")
        latest_md_title = latest_md_title.replace(": ", " - ")
        latest_md_title = latest_md_title.replace("%", " percent")

    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    func.helper_update_remote_line(
        1, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()

    ##### display_process_latest_md_title
    display_text = f"--- DISPLAY {func_text}"
    if do_display:
        print(f"--- {latest_md_title}")
    else:
        print(f"{display_text:<{conf.fpad}} ... DISPLAY SKIPPED")

    return latest_md_title