from config import Config as conf
from pathlib import Path
import shutil
import time
import sys
import inspect

##### debug_delay_long 
def debug_delay_long() -> None:
    time.sleep(conf.sleep_duration_long)

##### debug_delay_short 
def debug_delay_short() -> None:
    time.sleep(conf.sleep_duration_short)

##### debug_break
def debug_break() -> None:
    print("\n ================= DEBUG BREAK ================= \n")
    sys.exit()

##### debug_write_to_vault
def debug_write_to_vault(payload) -> None:
    func_text = "debug_write_to_vault"
    print(f"{func_text} ...", end="\r", flush=True)
    try:
        frame = inspect.currentframe().f_back
        var_name = [name for name, val in frame.f_locals.items() if val is payload][0]
        file_path = Path(conf.tranx_path).with_name(f"{var_name}.md")
        file_path.write_text(payload, encoding="utf-8")
        print(f"{func_text} ... DONE")
    except Exception as e:
        print(f"Failed to {func_text} {e}")
    return

##### debug_clear_tmp_and_complete_and_log_folders
def debug_clear_tmp_and_complete_and_log_folders() -> None:
    func_text = "debug_clear_tmp_and_complete_folders"
    print(f"{func_text} ...")

    # Convert your variable to a Path object
    folder = Path(conf.out_folder_tmp_path)
    # Loop through everything inside the folder
    for item in folder.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()         # Deletes files and symlinks
            elif item.is_dir():
                shutil.rmtree(item)   # Deletes subdirectories and their contents
        except Exception as e:
            print(f"Could not delete {item}: {e}")
    
    # Convert your variable to a Path object
    folder = Path(conf.out_folder_complete_path)
    # Loop through everything inside the folder
    for item in folder.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()         # Deletes files and symlinks
            elif item.is_dir():
                shutil.rmtree(item)   # Deletes subdirectories and their contents
        except Exception as e:
            print(f"Could not delete {item}: {e}")

    # Convert your variable to a Path object
    folder = Path(conf.out_folder_log_path)
    # Loop through everything inside the folder
    for item in folder.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()         # Deletes files and symlinks
            elif item.is_dir():
                shutil.rmtree(item)   # Deletes subdirectories and their contents
        except Exception as e:
            print(f"Could not delete {item}: {e}")