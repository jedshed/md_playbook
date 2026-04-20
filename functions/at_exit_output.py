from config import Config as conf
from datetime import datetime
from pathlib import Path

def at_exit_output() -> None:
    
    tmp_path = Path(conf.out_folder_tmp_path)
    comp_path = Path(conf.out_folder_complete_path)
    log_path = Path(conf.out_folder_log_path)

    ##### Output Script Exit details to stdout
    print("\n" + conf.seperator1)
    print(f"SCRIPT:                      {conf.ROOT_DIR}")
    print(f"STARTED:                     {conf.start_time}")
    print(f"FINISHED:                    {datetime.now():%Y-%m-%d--%H:%M:%S}")
    print(f"sys.executable:              {conf.sys_executable}")
    print(f"sys.platform:                {conf.sys_platform}")
    print(f'TARGET URL:                  {conf.base_url}')
    print(f'BS LIMIT:                    {conf.limit}')
    print(f'OUTPUT FOLDER PATH:          {conf.out_folder_path}')
    print(f'OUTPUT FOLDER log PATH:      {conf.out_folder_log_path}')
    print(f'OUTPUT FOLDER tmp PATH:      {conf.out_folder_tmp_path}')
    print(f'OUTPUT FOLDER complete PATH: {conf.out_folder_complete_path}')           
    print(f'ROOT_DIR:                    {conf.ROOT_DIR}')
    print(f'YAML FRONTMATTER PATH:       {conf.yaml_frontmatter_path}')
    print(f"TMP FILE COUNT:  {sum(1 for item in tmp_path.iterdir() if item.is_file())}")
    print(f"COMP FILE COUNT: {sum(1 for item in comp_path.iterdir() if item.is_file())}")
    print(f"LOG FILE COUNT:  {sum(1 for item in log_path.iterdir() if item.is_file())}")
    print(conf.seperator1 + "\n")
