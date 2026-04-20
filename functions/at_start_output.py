from config import Config as conf
from datetime import datetime
from pathlib import Path

def at_start_output(do_func) -> None:
    
    ##### Output Script Start details to stdout
    print("\n" + conf.seperator1)
    print(f"SCRIPT:          {conf.ROOT_DIR}")
    print(f"STARTED:         {conf.start_time}")
    print(conf.seperator1 + "\n")
