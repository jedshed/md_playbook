import functions as func
from config import Config as conf
from trafilatura import *
import textwrap
import shutil

def extract_metadata_vars(
    latest_url,
    do_display_metadata_all,
    do_display_metadata_select,
    do_func):

    ##### Extract Metadate with Trafilatura
    func_text = ("EXTRACT METADATA")
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do_func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### Download page content as downloaded
    try:
        downloaded = fetch_url(latest_url)
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    ##### Extract metadata object
    try:
        metadata = extract_metadata(downloaded)
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    ##### Assign Select metadata as Vars
    try:
        if metadata:
            meta_date = metadata.date if metadata and metadata.date else "None"
            meta_filedate = metadata.filedate if metadata and metadata.filedate else "None"
            meta_title = metadata.title if metadata and metadata.title else "None"
            meta_sitename = metadata.sitename if metadata and metadata.sitename else "None"
            meta_url = metadata.url if metadata and metadata.url else "None"
            meta_description = metadata.description if metadata and metadata.description else "None"
            meta_author = metadata.author if metadata and metadata.author else "None"

            ### Set meta_oldest_date to oldest as site data not always consistent 
            meta_publish_date = max(meta_date, meta_filedate)

            # ### Put vars in metadata_items list for display looping
            metadata_items = [
                ("meta_date", meta_date),
                ("meta_filedate", meta_filedate),
                ("meta_publish_date", meta_publish_date),
                ("meta_title", meta_title),
                ("meta_sitename", meta_sitename),
                ("meta_author", meta_author),
                ("meta_url", meta_url),
                ("meta_description", meta_description)]

            func.helper_update_remote_line(
                1, f"{func_text:<{conf.fpad}} ... DONE")
            func.debug_delay_long()

    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")


    ##### display metadata

    ### display metadate select
    display_metadata_select_text = ("--- DISPLAY METADATA - SELECT")
    print(f"{display_metadata_select_text:<{conf.fpad}}")
    func.debug_delay_long()
    
    if not do_display_metadata_select:
        func.helper_update_remote_line(
                1, f"{display_metadata_select_text:<{conf.fpad}} ... DISPLAY SKIPPED")        
        func.debug_delay_long()
    
    ### display_metadata_select
    try:
        if do_display_metadata_select and metadata:

            ### Detect current terminal width
            term_width = shutil.get_terminal_size(fallback=(80, 24)).columns
            
            ### Loop over metadata_items and print the list with text wrap 
            textwrap_width = 20
            indent_space = " " * (int(textwrap_width) + 4)
            print(f"\n    {conf.seperator2}")
            for key, value in metadata_items:
                func.debug_delay_short()
                val_str = str(value)
                prefix = f"    {(key + ':'):<{textwrap_width}}"
                ### Wrap with a hanging indent for long keys
                print(textwrap.fill(
                    val_str, 
                    width=max(40, term_width - 1), 
                    initial_indent=prefix, 
                    subsequent_indent=indent_space
                ))
            print(f"    {conf.seperator2}\n")
            func.debug_delay_long()

    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")


    ##### display_metadata_all
    display_metadata_all_text = ("--- DISPLAY METADATA - ALL")
    print(f"{display_metadata_all_text:<{conf.fpad}}")
    func.debug_delay_long()

    ### Do display_metadata_all
    if not do_display_metadata_all:
        func.helper_update_remote_line(
                1, f"{display_metadata_all_text:<{conf.fpad}} ... DISPLAY SKIPPED")        
        func.debug_delay_long()

    ##### display_metadata_all
    try:
        if do_display_metadata_all and metadata:

            ### Get the actual width of  terminal window - Else default to 80
            term_width = shutil.get_terminal_size(fallback=(80, 24)).columns
            all_values = metadata.as_dict()
            ### Hardcode label width (column 1)
            textwrap_width = 18
            indent_space = " " * (int(textwrap_width) + 4)

            print(f"\n    {conf.seperator2}")
            for key, value in all_values.items():
                func.debug_delay_short()
                val_str = str(value)
                prefix = f"    {(key + ':'):<{textwrap_width}}"
                ### Wrap based on terminal size ###
                ### Subtract 1 to prevent "phantom" newlines at the edge##
                print(textwrap.fill(
                    val_str, 
                    width=term_width - 1, 
                    initial_indent=prefix, 
                    subsequent_indent=indent_space
                ))

            print(f"    {conf.seperator2}\n")
            func.debug_delay_long()
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    ##### Return Vars
    return {
        "meta_date": meta_date,
        "meta_filedate": meta_filedate,
        "meta_title": meta_title,
        "meta_sitename": meta_sitename,
        "meta_url": meta_url,
        "meta_author": meta_author,
        "meta_description": meta_description,
        "meta_publish_date": meta_publish_date
    }