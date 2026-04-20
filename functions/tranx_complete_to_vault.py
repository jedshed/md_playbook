
from config import Config as conf
import functions as func
import time
import shutil
from pathlib import Path

def tranx_complete_to_vault(do_func):

    func_text = "TRANX MD FILES FROM complete TO vault "
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ### Set Retries
    retries = 10

    source_path = Path(conf.out_folder_complete_path)
    target_path = Path(conf.tranx_path)

    # 1. Strict check: If target directory is missing, notify and exit
    if not target_path.is_dir():
        print(f"--- ERROR: Target directory does not exist: {target_path}")
        return  # Stop the function to protect folder structure

    for item in source_path.iterdir():
        if item.is_file():
            destination = target_path / item.name
            
            # 2. Collision check: Skip if already in vault
            if destination.exists():
                print(f"--- SKIP: {item.name} already exists in vault.     ")
                continue

            # 3. Move with retry logic
            for attempt in range(retries):
                try:
                    shutil.move(str(item), str(destination))
                    break 
                except Exception as e:
                    if attempt < retries - 1:
                        time.sleep(1)
                        continue
                    else:
                        print(f"--- FAIL: Could not move {item.name}: {e}")

    func.helper_update_remote_line(
        1, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()