
import functions as func
from config import Config as conf
import re
import time
import textwrap

def update_yaml(latest_md_title, meta_url, meta_sitename, meta_publish_date, meta_author, do_func, do_display, retries=10,):

    func_text = "UPDATE YAML FRONTMATTER"
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    # Use an absolute path relative to this script to avoid directory confusion
    file_path = conf.ROOT_DIR / 'yaml_frontmatter'
    try:
        for attempt in range(retries):
            try:
                frontmatter_yaml = file_path.read_text()
                
                # Perform substitutions with re
                frontmatter_yaml = re.sub(r'^title:.*', f'title: {latest_md_title}', frontmatter_yaml, flags=re.M)
                frontmatter_yaml = re.sub(r'^source:.*', f'source: {meta_url}', frontmatter_yaml, flags=re.M)
                frontmatter_yaml = re.sub(r'^author:.*', f'author: {meta_author}', frontmatter_yaml, flags=re.M)
                frontmatter_yaml = re.sub(r'^created:.*', f'created: {meta_publish_date}', frontmatter_yaml, flags=re.M)
                
            except FileNotFoundError:
                if attempt < retries - 1:
                    time.sleep(1)  # Wait 1 second before trying again
                    continue
                else:
                    raise  # Re-raise error if all retries fail
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")
    
    func.helper_update_remote_line(
        1, f"{func_text:<{conf.fpad}} ... DONE")
    func.debug_delay_long()

    ##### Display
    display_frontmatter_yaml_text = "--- DISPLAY FRONTMATTER YAML"
    print(f"{display_frontmatter_yaml_text:<{conf.fpad}} ...")
    func.debug_delay_long()

    if not do_display:
        func.helper_update_remote_line(
            1, f"{display_frontmatter_yaml_text:<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()
        return frontmatter_yaml

    if do_display:

        # Add 4 spaces to the start of every line of frontmatter_yaml
        frontmatter_yaml = textwrap.indent(frontmatter_yaml, '    ')

        print(f"    {conf.seperator2}\n")
        print(f"{frontmatter_yaml}")
        print(f"\n    {conf.seperator2}")

    return frontmatter_yaml