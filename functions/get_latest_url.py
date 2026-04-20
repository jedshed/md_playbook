
from config import Config as conf
import functions as func
import sys
from curl_cffi import requests
from bs4 import BeautifulSoup

def get_latest_url(base_url, lim, do_func, do_display_all_hrefs):

    ###### func_text
    func_text = ("GET LATAEST URL")
    print(f"{func_text:<{conf.fpad}} ... ")
    func.debug_delay_long()

    ##### do func check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    # 'impersonate' mimics a real browser's TLS fingerprint to bypass blocks
    #  This is much harder for sites to detect than standard 'requests'
    try:
        response = requests.get(conf.base_url, impersonate="chrome120")
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            # Extract all unique <a> tag links
            # links = {link.get("href") for link in soup.find_all("a") if link.get("href")}
            links = [link.get("href") for link in soup.find_all("a") if link.get("href")]
            latest_url = (list(links)[lim]) if len(links) > lim else print("Link not found")
            func.helper_update_remote_line(
                1, f"{func_text:<{conf.fpad}} ... DONE")
            func.debug_delay_long()
            print(f"--- {latest_url}")
            func.debug_delay_long()
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            sys.exit()
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")
        sys.exit()


    ##### do_display_all_hrefs
    if do_display_all_hrefs:
        print(f"{'--- DISPLAY ALL URL HREFs':<{conf.fpad}}")
        func.debug_delay_long()
        print (conf.seperator2)
        count = 0
        for href in links:
            print(count, href)
            count += 1
        print ("")

    ##### Print the no of links found
        func.debug_delay_long()
        print(f"--- Found {len(links)} links:")    
        print (conf.seperator2)
        func.debug_delay_long()
    else:
        print(f"{'--- DISPLAY ALL URL HREFs':<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()
    return latest_url