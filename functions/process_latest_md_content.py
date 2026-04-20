from config import Config as conf
import functions as func
from pathlib import Path
import re

""" ---- MARKITDOWN INFO -----                  """
""" Uses MarkItDown to fetch and convert a URL  """
""" md.convert loses hyperlinks                 """
""" md.convert_url preserves hyperlinks         """

def process_latest_md_content(latest_md_content, do_func, do_display):
    func_text = "PROCESS LATEST MD CONTENT"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    #### REGEX REMOVE TOP
    regex_remove_top_text = "--- REGEX REMOVE TOP"
    print(f"{regex_remove_top_text:<{conf.fpad}} ...")
    func.debug_delay_long()
    try:
    # Regex breakdown:
    # (?s) matches across newlines
    # ^.*? matches from the start
    # \*\*Good morning matches your specific text
    # .*? matches the rest of the line
    # \n? removes the trailing newline
        pattern = r'(?s)^.*?(\*\* *(?:Good.*?morning|Good.*?afternoon).*?\n?)'
        latest_md_content = re.sub(pattern, r"\1", latest_md_content, count=1)

        func.helper_update_remote_line(
            1, f"{regex_remove_top_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()

    except Exception as e:
        print(f"Failed to {func_text:<{conf.fpad}} {e}")  

    ##### REGEX REMOVE BOTTOM
    regex_remove_bottom_text = "--- REGEX REMOVE BOTTOM"
    print(f"{regex_remove_bottom_text:<{conf.fpad}}")
    func.debug_delay_long()
    try:
    # Regex breakdown:
    # \*\*SUBSCRIBE     -> Matches the literal characters "**SUBSCRIBE"
    # .*                -> Matches any character (the dot) zero or more times
    # re.DOTALL         -> Makes the "." match newline characters, ensuring 
    #                      it captures everything until the end of the string
        pattern = r'\*\*SUBSCRIBE to the POLITICO.*'
        latest_md_content = re.sub(pattern, '', latest_md_content, flags=re.DOTALL)

        func.helper_update_remote_line(
            1, f"{regex_remove_bottom_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()

    except Exception as e:
        print(f"Failed to {regex_remove_bottom_text} {e}")

    ##### REGEX REMOVE LINES BEGINNING WITH PIPE '|'
    regex_remove_pipe_lines_text = "--- REGEX REMOVE PIPE LINES"
    print(f"{regex_remove_pipe_lines_text:<{conf.fpad}}")
    func.debug_delay_long()
    
    try:
    # Pattern explanation:
    # ^      -> Start of a line (enabled by re.MULTILINE)
    # \|     -> Matches the literal pipe character (escaped because | is a special regex char)
    # .*     -> Matches everything else on that line
    # \n?    -> Matches the optional trailing newline so the gap is closed
        latest_md_content = re.sub(r'^\|.*\n?', '', latest_md_content, flags=re.MULTILINE)

        func.helper_update_remote_line(
            1, f"{regex_remove_pipe_lines_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()

    except Exception as e:
        print(f"Failed to {regex_remove_pipe_lines_text} {e}")

    ##### Update Function DONE (n number of REGEXes)
    func.helper_update_remote_line(
        4, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()

    ##### DISPLAY PROCESSED latest_md_content
    display_latest_md_content_text = "--- DISPLAY PROCESSED latest_md_content"
    print(f"{display_latest_md_content_text:<{conf.fpad}} ...")

    if not do_display:
        func.helper_update_remote_line(
            1, f"{display_latest_md_content_text:<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()
        return latest_md_content

    try:
        print(f"\n{conf.seperator2}\n")
        print(f"{latest_md_content}")
        print(f"\n{conf.seperator2}\n")
        func.debug_delay_long()
    except Exception as e:
        print(f"Failed to {display_latest_md_content_text} {e}")

    return latest_md_content
