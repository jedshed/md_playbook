### Standard library imports
from pathlib import Path
import atexit
from config import Config as conf

### Third-party library imports

### Local application library imports
import functions as func
from config import Config as conf

def main():
    
    ###############
    # DEBUG FUNCS #
    ###############
    # func.debug_write_to_vault(markdown_final)
    # func.debug_clear_tmp_and_complete_and_log_folders()
    # func.debug_break()

    ##### Register atexit function
    atexit.register(func.at_exit_output)

    ##### Print Start Output
    func.at_start_output(
    do_func = True)

    ##### CHECK Internet Connected
    func.check_internet_connected(
    do_func = True)

    ##### GET_latest_url with BS
    latest_url = func.get_latest_url(conf.base_url, conf.limit,
    do_func = True,
    do_display_all_hrefs = False)

    ##### CHECK if MD File Already Created - I.E. URL in Log File    
    func.check_url_in_log(latest_url,
    do_func = True)

    ##### CHECK and Make Output Folders
    func.check_make_output_folders(
    do_func = True)

    ##### EXTRACT metadata as metadata_vars OBJ and display if required
    metadata_vars = func.extract_metadata_vars(latest_url,
    do_func = True,
    do_display_metadata_select = True,
    do_display_metadata_all = True)
    ### Assign metadata VARS from metadata_vars OBJ
    meta_date           = metadata_vars['meta_date']
    meta_filedate       = metadata_vars['meta_filedate']
    meta_title          = metadata_vars['meta_title']
    meta_sitename       = metadata_vars['meta_sitename']
    meta_url            = metadata_vars['meta_url']
    meta_author         = metadata_vars['meta_author']
    meta_description    = metadata_vars['meta_description']
    meta_publish_date   = metadata_vars['meta_publish_date']

    ##### CREATE_latest_md_title
    latest_md_title = func.create_latest_md_title(latest_url, meta_publish_date,
    do_func = True,
    do_display = False)

    ###### PROCESS_latest_md_title
    latest_md_title = func.process_latest_md_title(latest_md_title,
    do_func = True,
    do_display = True)

    ##### CREATE_latest_filename
    latest_filename = func.create_latest_md_filename(latest_md_title,
    do_func = True,
    do_display = True)

    ##### CREATE and UPDATE YAML VAR from yaml_frontmatter file
    frontmatter_yaml = func.update_yaml(latest_md_title, meta_url, meta_sitename, meta_publish_date, meta_author,
    do_func = True,
    do_display = False)

    ##### CREATE latest_md_header
    latest_md_header = func.create_latest_md_header(latest_md_title, meta_description, meta_sitename, meta_publish_date,
    do_func = True,
    do_display = False)

     ##### PROCESS latest_md_header
    latest_md_header = func.process_latest_md_header(latest_md_header,
    do_func = True,
    do_display = False)

    ##### CREATE latest_md_content 
    latest_md_content = func.create_latest_md_content(latest_url,
    do_func = True,
    do_display = False)

    ##### PROCESS latest_md_content
    latest_md_content = func.process_latest_md_content(latest_md_content,
    do_func = True,
    do_display = False)

    ##### CREATE markdown_final - Combine; frontmatter - header - content
    markdown_final = func.make_md_final(frontmatter_yaml, latest_md_header, latest_md_content,
    do_func = True,
    do_display = False)

    ##### SAVE markdown final to tmp
    func.save_md_file_to_tmp(latest_filename,markdown_final,
    do_func = True)

    ##### MOVE MarkDown File FROM tmp TO completed Dir
    func.move_md_file_tmp_to_complete(latest_filename,
    do_func = True)

    ##### TRANX complete to vault
    func.tranx_complete_to_vault(
    do_func = True)

    ##### UPDATE LOG File with Latest_URL
    func.update_log(latest_url,
    do_func = True)

    ##### COMPLETION
    print(f"\nALL DONE")
    
if __name__ == '__main__':
    main()

    ###############
    # DEBUG BREAK #
    ###############
    # func.debug_write_to_vault(markdown_final)
    # func.debug_clear_tmp_and_complete_and_log_folders()
    # func.debug_break()
