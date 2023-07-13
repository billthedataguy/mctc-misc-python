from tkinter.ttk import Progressbar
from tkinter.messagebox import showinfo
import requests
import time
import tkinter as tk
import urllib

#############################################################################################
payload = {
    "blendFacetsSeparately" : False,
    "disableCache" : False,
    "getMore" : 0,
    "inst" : "01MNPALS_MCT",
    "lang" : "en",
    "limit" : 10,
    "mode" : "advanced",
    "newspapersActive" : False,
    "newspapersSearch" : False,
    "offset" : 0,
    "pcAvailability" : False,
    "rapido" : False,
    "refEntryActive" : False,
    "rtaLinks" : True,
    "scope" : "MyInst_and_CI",
    "skipDelivery" : "Y",
    "sort" : "title",
    "tab" : "Everything",
    "vid" : "01MNPALS_MCT:MCT",
}

url = r"https://mnpals-mct.primo.exlibrisgroup.com/primaws/rest/pub/pnxs?"
#############################################################################################



root = tk.Tk()
root.title("Simple Primo Title List Checker")

title_textbox = tk.Text(root, width=100, borderwidth=2)
title_textbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

progress_bar = Progressbar(root, orient="horizontal", length=100, mode="determinate")
progress_bar.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

def search_primo():
    titles_str = title_textbox.get(1.0, tk.END).strip()
    if titles_str:
        progress_bar.start()
        root.update_idletasks()

        title_list = titles_str.split("\n")
        title_textbox.delete(1.0, tk.END)
        num_titles = len(title_list)
        portions = int(100 // num_titles)
        title_textbox.insert(tk.END, f'<html><head></head><body>')


        for title in title_list:

            progress_bar["value"] = portions
            root.update_idletasks()

            # title_textbox.insert(tk.END, f"\n{title.upper()}\n\n<p></p>")

            encoded_title = f'{urllib.parse.quote(title)}'

            query = f"&q=title,begins_with,{encoded_title},AND;rtype,exact,books,AND"

            r = requests.get(f"{url}{query}", params=payload)

            primo_url1 = r'https://mnpals-mct.primo.exlibrisgroup.com/discovery/search?query=title,begins_with,'

            primo_url2 = f"{encoded_title},AND&pfilter=rtype,exact,books,AND&tab=Everything&search_scope=MyInst_and_CI&sortby=title&vid=01MNPALS_MCT:MCT&mode=advanced&offset=0"

            title_textbox.insert(tk.END, f'<a href="{primo_url1}{primo_url2}">{title.upper()}</a>\t\t\t\t\t')


            try:
                title_textbox.insert(tk.END, f'{r.json()["info"]["total"]} rec(s) found.\n\n<p></p>')
            except:
                continue
            time.sleep(.5)
            portions += portions

        title_textbox.insert(tk.END, f'</body></html>')
        progress_bar.stop()
        root.update_idletasks()
        showinfo(message="Done!")


def clear_text():
    title_textbox.delete(1.0, tk.END)

def save_html():
    with open("title_checker_results.html", "w") as f:
        f.write(f'{title_textbox.get("1.0", tk.END)}')

    title_textbox.delete(1.0, tk.END)
    showinfo(message="Saved!")

def quit_app():
    root.destroy()
    quit()

clear_button = tk.Button(root, text="CLEAR", command=clear_text)
clear_button.grid(row=2, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="SEARCH", command=search_primo)
search_button.grid(row=2, column=1, padx=10, pady=10)

save_button = tk.Button(root, text="SAVE", command=save_html)
save_button.grid(row=2, column=2, padx=10, pady=10)

quit_button = tk.Button(root, text="QUIT", command=quit_app)
quit_button.grid(row=2, column=3, padx=10, pady=10)

root.mainloop()