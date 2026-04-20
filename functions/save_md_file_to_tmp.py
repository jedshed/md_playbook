from config import Config as conf
import functions as func
from pathlib import Path

def save_md_file_to_tmp(latest_filename,markdown_final, do_func):

    func_text = "SAVE MD FILE TO TMP DIR"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ### Convert String Path to Path Object
    try:
        target_dir = Path(conf.out_folder_tmp_path)
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    #### Combine the directory and filename using the / operator
    try:
        file_path = target_dir / latest_filename
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    try:
        file_path.write_text(markdown_final, encoding='utf-8')

        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")
    