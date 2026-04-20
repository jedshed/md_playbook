# Make md file using Trafilatura and Frontmatter to inject metadata to yaml frontmatter
from config import Config as conf
import functions as func
from pathlib import Path
from datetime import datetime
import time
import sys

def make_md_final(frontmatter_yaml, latest_md_header, latest_md_content, do_func, do_display):

    func_text = "MAKE MD FINAL"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()
    
    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    ##### Create Markdown Final - Combine frontmatter - header - content
    try:
        markdown_final = f"{frontmatter_yaml}\n\n{latest_md_header}\n\n{latest_md_content}"

        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()
    except Exception as e:
        print(f"Failed to Combine Frontmatter, Header and Content {e}")

    ##### DISPLAY latest_md_content
    display_markdown_final_text = "--- DISPLAY MARKDOWN FINAL"
    print(f"{display_markdown_final_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    if not do_display:
        func.helper_update_remote_line(
            1, f"{display_markdown_final_text:<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()
        return markdown_final
    else:
        print(f"\n{conf.seperator2}\n")
        print(f"{markdown_final}")
        print(f"\n{conf.seperator2}\n")

        return markdown_final