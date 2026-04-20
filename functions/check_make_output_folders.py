#Make DOT Output Folder in Users Home Folder
import functions as func
from config import Config as conf
from pathlib import Path
import time

def check_make_output_folders(do_func):

    ### Check if folder exists and create if not
    func_text = ("CHECK MAKE OUTPUT FOLDERS")
    print(f"{func_text:<{conf.fpad}} ...")

    func.debug_delay_long()

    ### Do Func Check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        return

    ### create path objects
    out_folder_path = Path(conf.out_folder_path)
    out_folder_tmp_path = Path(conf.out_folder_tmp_path)
    out_folder_complete_path = Path(conf.out_folder_complete_path)
    out_folder_log_path = Path(conf.out_folder_log_path)

    ### Check / Create  Out folder
    try:
        out_text = (f"OUT FOLDER")
        if out_folder_path.exists():
            print(f"{'--- ' + out_text:<{conf.fpad}} ... EXISTS")
            func.debug_delay_long()
        else:
            print(f"{'--- CREATING - ' + out_text:<{conf.fpad}} ...")
            func.debug_delay_long()
            # make folder
            out_folder_path.mkdir(parents=True, exist_ok=True)
            func.helper_update_remote_line(
                1, f"{'--- ' + out_text:<{conf.fpad}} ... CREATED")
            func.debug_delay_long()
    except Exception as e:
        print(f"Failed to Create: {func_text:<{conf.fpad}} {e}")

    ### Check / Create TMP folder
    try:
        tmp_text = "TMP SUB-FOLDER"
        if out_folder_tmp_path.exists():
            print(f"{'--- ' + tmp_text:<{conf.fpad}} ... EXISTS")
            func.debug_delay_long()
        else:
            print(f"{'--- CREATING - ' + tmp_text:<{conf.fpad}} ...")
            func.debug_delay_long()
            # make folder
            out_folder_tmp_path.mkdir(parents=True, exist_ok=True)
            func.helper_update_remote_line(
                1, f"{'--- ' + tmp_text:<{conf.fpad}} ... CREATED")
            func.debug_delay_long()
    except Exception as e:
        print(f"Failed to Create: {func_text:<{conf.fpad}} {e}")

    ### Check / Create COMP folder
    try:
        comp_text = "COMP SUB-FOLDER"
        if out_folder_complete_path.exists():
            print(f"{'--- ' + comp_text:<{conf.fpad}} ... EXISTS")
            func.debug_delay_long()
        else:
            print(f"{'--- CREATING - ' + comp_text:<{conf.fpad}} ...")
            func.debug_delay_long()
            # make folder
            out_folder_complete_path.mkdir(parents=True, exist_ok=True)
            func.helper_update_remote_line(
                1, f"{'--- ' + comp_text:<{conf.fpad}} ... CREATED")            
            func.debug_delay_long()
    except Exception as e:
        print(f"Failed to Create: {func_text:<{conf.fpad}} {e}")

    ### Check / Create LOG folder
    try:
        log_text = "LOG SUB-FOLDER"
        if out_folder_log_path.exists():
            print(f"{'--- ' + log_text:<{conf.fpad}} ... EXISTS")
            func.debug_delay_long()
        else:
            print(f"{'--- CREATING - ' + log_text:<{conf.fpad}} ...")
            func.debug_delay_long()
            # make folder
            out_folder_log_path.mkdir(parents=True, exist_ok=True)
            # print(f"{'--- CREATING LOG SUB-FOLDER':<{conf.fpad}} ... DONE")
            func.helper_update_remote_line(
                1, f"{'--- ' + log_text:<{conf.fpad}} ... CREATED")
            func.debug_delay_long()
    except Exception as e:
        print(f"Failed to Create: {func_text:<{conf.fpad}} {e}")

    ### Replace the func line with funcline DONE using helper function
    func.helper_update_remote_line(5, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()
