import requests
import urllib
import time
import tkinter as tk
from tkhtmlview import HTMLLabel


root = tk.Tk()
root.title("Simple Primo Title List Checker")

title_textbox = tk.Text(root, width=50, height=25, borderwidth=2)
title_textbox.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

links_textbox = tk.Text(root, width=50, height=25, borderwidth=2)
links_textbox.grid(row=3, column=0, columnspan=1, padx=10, pady=10)

def clear_text():
    title_textbox.delete(1.0, tk.END)

def search_primo():
    payload = {
        "blendFacetsSeparately": False,
        "disableCache": False,
        "getMore": 0,
        "inst": "01MNPALS_MCT",
        "lang": "en",
        "limit": 10,
        "mode": "advanced",
        "newspapersActive": False,
        "newspapersSearch": False,
        "offset": 0,
        "pcAvailability": False,
        "rapido": False,
        "refEntryActive": False,
        "rtaLinks": True,
        "scope": "MyInst_and_CI",
        "skipDelivery": "Y",
        "sort": "title",
        "tab": "Everything",
        "vid": "01MNPALS_MCT:MCT",
            }

    url = r"https://mnpals-mct.primo.exlibrisgroup.com/primaws/rest/pub/pnxs?"
    primo_url1 = r'https://mnpals-mct.primo.exlibrisgroup.com/discovery/search?query=title,begins_with,'

    titles_str = title_textbox.get(1.0, tk.END).strip()

    if titles_str:
        title_list = titles_str.split("\n")
        title_textbox.delete(1.0, tk.END)
        root.update_idletasks()
        title_textbox.insert(tk.END, "Watch the fucking magic asshat!\n\n")

        for title in title_list:
            encoded_title = f'{urllib.parse.quote(title)}'
            query = f"&q=title,begins_with,{encoded_title},AND;rtype,exact,books,AND"
            primo_url2 = f"{encoded_title},AND&pfilter=rtype,exact,books,AND&tab=Everything&search_scope=MyInst_and_CI&sortby=title&vid=01MNPALS_MCT:MCT&mode=advanced&offset=0"

            r = requests.get(f"{url}{query}", params=payload)

            label1 = HTMLLabel(root, html='<a href="{primo_url1}{primo_url2}">link</a>')

            title_textbox.insert(tk.END, f"CHECKING: {title} ...\n")
            root.update_idletasks()

            try:
                json_response = r.json()
                recs_found = json_response["info"]["total"]

                if recs_found > 0:
                    title_textbox.insert(tk.END, f"{recs_found} RECS FOUND!\n")
                    links_textbox.insert(label1)
                    root.update_idletasks()


                else:
                    title_textbox.insert(tk.END, f"NO RECS FOUND!\n\n")
                    root.update_idletasks()


            except:
                err_msg = f'CANNOT DETERMINE HOW MANY RECS\n\n'
                title_textbox.insert(tk.END, err_msg)
                root.update_idletasks()

            time.sleep(1)


def quit_app():
    root.destroy()
    quit()

clear_button = tk.Button(root, text="CLEAR", command=clear_text)
clear_button.grid(row=2, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="SEARCH", command=search_primo)
search_button.grid(row=2, column=1, padx=10, pady=10)

quit_button = tk.Button(root, text="QUIT", command=quit_app)
quit_button.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()