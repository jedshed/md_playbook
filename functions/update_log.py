# Update Log File
from config import Config as conf
import functions as func
from pathlib import Path

def update_log(latest_url, do_func):
    func_text = "UPDATE LOG"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    # Assuming these are already Path objects or strings
    log_path = Path(conf.out_folder_log_path) / conf.log_file_name
    # 1. Read existing content if it exists
    existing_urls = log_path.read_text().splitlines() if log_path.exists() else []
    # 2. Append if the URL is new
    if latest_url not in existing_urls:
        # Use .open() directly on the Path object
        with log_path.open("a", encoding="utf-8") as f:
            f.write(f"{latest_url}\n")

    func.helper_update_remote_line(
        1, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()