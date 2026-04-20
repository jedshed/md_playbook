''' Move MD File from tmp to Complete '''
from config import Config as conf
import functions as func
import shutil

def move_md_file_tmp_to_complete(latest_filename, do_func):

    func_text = "MOVE MD FILE FROM tmp TO complete"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    else:
        ### Move File
        try:
            shutil.move(f'{conf.out_folder_tmp_path}/{latest_filename}', f'{conf.out_folder_complete_path}')

            func.helper_update_remote_line(
                1, f"{func_text:<{conf.fpad}} ... DONE")
            func.debug_delay_long()

        except Exception as e:
            print(f"Failed to: {func_text:<{conf.fpad}} {e}")