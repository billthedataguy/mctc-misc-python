#! python3

import isbnlib as il
import pyperclip
import tkinter as tk
import webbrowser



#########################


ranges_dict = {

    'Tom': ["Alternative Press", "A", "C", "D", "E", "F", "G-GF", "GN-GT", "H", "J", "K", "QM", "QP", "QR", "R"],
    'Bill': ["B", "L", "Q", "S", "T-TP", "TS", "Z"],
    'Jenny': ["GV", "M", "N", "TR", "TT", "TX"],
    'Amanda': ["P-PZ"],
    'Freecart': ["U, V"],



}




selector_dict = {

    'A': 'Tom',

    'B': 'Bill', 'BC': 'Bill', 'BD': 'Bill', 'BF': 'Bill', 'BH': 'Bill', 'BJ': 'Bill', 'BL': 'Bill', 'BM': 'Bill',
    'BP': 'Bill', 'BQ': 'Bill', 'BR': 'Bill', 'BS': 'Bill', 'BT': 'Bill', 'BV': 'Bill', 'BX': 'Bill',

    'C': 'Tom', 'CB': 'Tom', 'CC': 'Tom', 'CD': 'Tom', 'CE': 'Tom', 'CJ': 'Tom', 'CN': 'Tom', 'CR': 'Tom', 'CS': 'Tom',
    'CT': 'Tom',

    'D': 'Tom', 'DA': 'Tom', 'DAW': 'Tom', 'DB': 'Tom', 'DC': 'Tom', 'DD': 'Tom', 'DE': 'Tom', 'DF': 'Tom',
    'DG': 'Tom', 'DH': 'Tom', 'DJ': 'Tom', 'DJK': 'Tom', 'DK': 'Tom', 'DL': 'Tom', 'DP': 'Tom', 'DQ': 'Tom',
    'DR': 'Tom', 'DS': 'Tom', 'DT': 'Tom', 'DU': 'Tom', 'DX': 'Tom',

    'E': 'Tom',
    'F': 'Tom',
    'G': 'Tom', 'GA': 'Tom', 'GB': 'Tom', 'GC': 'Tom', 'GE': 'Tom', 'GF': 'Tom', 'GN': 'Tom', 'GR': 'Tom', 'GT': 'Tom',

    'GV': 'Jenny',

    'H': 'Tom', 'HA': 'Tom', 'HB': 'Tom', 'HC': 'Tom', 'HD': 'Tom', 'HE': 'Tom', 'HF': 'Tom', 'HG': 'Tom', 'HJ': 'Tom',
    'HM': 'Tom', 'HN': 'Tom', 'HQ': 'Tom', 'HS': 'Tom', 'HT': 'Tom', 'HV': 'Tom', 'HX': 'Tom',

    'J': 'Tom', 'JA': 'Tom', 'JC': 'Tom', 'JF': 'Tom', 'JJ': 'Tom',
    'JK': 'Tom', 'JL': 'Tom', 'JN': 'Tom', 'JQ': 'Tom', 'JS': 'Tom', 'JV': 'Tom', 'JZ': 'Tom',

    'K': 'Tom', 'KB': 'Tom',
    'KBM': 'Tom', 'KBP': 'Tom', 'KBR': 'Tom',
    'KBU': 'Tom', 'KD': 'Tom', 'KDC': 'Tom', 'KDE': 'Tom', 'KDG': 'Tom', 'KDK': 'Tom',
    'KDZ': 'Tom', 'KE': 'Tom', 'KF': 'Tom', 'KG': 'Tom', 'KH': 'Tom', 'KJ': 'Tom',
    'KJA': 'Tom', 'KJC': 'Tom', 'KJE': 'Tom', 'KJG': 'Tom', 'KJH': 'Tom', 'KJJ': 'Tom',
    'KJK': 'Tom', 'KJM': 'Tom', 'KJN': 'Tom', 'KJP': 'Tom', 'KJR': 'Tom', 'KJS': 'Tom',
    'KJT': 'Tom', 'KJV': 'Tom', 'KJW': 'Tom', 'KK': 'Tom', 'KL': 'Tom', 'KM': 'Tom',
    'KN': 'Tom', 'KP': 'Tom', 'KQ': 'Tom', 'KKA': 'Tom', 'KKB': 'Tom', 'KKE': 'Tom',
    'KKF': 'Tom', 'KKG': 'Tom', 'KKH': 'Tom', 'KKI': 'Tom', 'KKJ': 'Tom', 'KKK': 'Tom',
    'KKL': 'Tom', 'KKM': 'Tom', 'KKN': 'Tom', 'KKP': 'Tom', 'KKQ': 'Tom', 'KKR': 'Tom',
    'KKS': 'Tom', 'KKT': 'Tom', 'KKV': 'Tom', 'KKW': 'Tom', 'KKX': 'Tom', 'KKY': 'Tom',
    'KKZ': 'Tom', 'KLA': 'Tom', 'KLB': 'Tom', 'KLD': 'Tom', 'KLE': 'Tom', 'KLF': 'Tom',
    'KLH': 'Tom', 'KLM': 'Tom', 'KLN': 'Tom', 'KLP': 'Tom', 'KLQ': 'Tom', 'KLR': 'Tom',
    'KLS': 'Tom', 'KLT': 'Tom', 'KLV': 'Tom', 'KLW': 'Tom', 'KMC': 'Tom', 'KME': 'Tom',
    'KMF': 'Tom', 'KMG': 'Tom', 'KMH': 'Tom', 'KMJ': 'Tom', 'KMK': 'Tom', 'KML': 'Tom',
    'KMM': 'Tom', 'KMN': 'Tom', 'KMP': 'Tom', 'KMQ': 'Tom', 'KMS': 'Tom', 'KMT': 'Tom',
    'KMU': 'Tom', 'KMV': 'Tom', 'KMX': 'Tom', 'KMY': 'Tom', 'KNC': 'Tom', 'KNE': 'Tom',
    'KNF': 'Tom', 'KNG': 'Tom', 'KNH': 'Tom', 'KNK': 'Tom', 'KNL': 'Tom', 'KNM': 'Tom',
    'KNN': 'Tom', 'KNP': 'Tom', 'KNQ': 'Tom', 'KNR': 'Tom', 'KNS': 'Tom', 'KNT': 'Tom',
    'KNV': 'Tom', 'KNW': 'Tom', 'KNX': 'Tom', 'KNY': 'Tom', 'KPA': 'Tom', 'KPC': 'Tom',
    'KPE': 'Tom', 'KPF': 'Tom', 'KPG': 'Tom', 'KPH': 'Tom', 'KPJ': 'Tom', 'KPK': 'Tom',
    'KPL': 'Tom', 'KPM': 'Tom', 'KPP': 'Tom', 'KPS': 'Tom', 'KPT': 'Tom', 'KPV': 'Tom',
    'KPW': 'Tom', 'KQC': 'Tom', 'KQE': 'Tom', 'KQG': 'Tom', 'KQH': 'Tom', 'KQJ': 'Tom',
    'KQK': 'Tom', 'KQM': 'Tom', 'KQP': 'Tom', 'KQT': 'Tom', 'KQV': 'Tom', 'KQW': 'Tom',
    'KQX': 'Tom', 'KR': 'Tom', 'KS': 'Tom', 'KT': 'Tom', 'KU': 'Tom', 'KV': 'Tom',
    'KW': 'Tom', 'KZ': 'Tom', 'KRB': 'Tom', 'KRC': 'Tom', 'KRE': 'Tom', 'KRG': 'Tom',
    'KRK': 'Tom', 'KRL': 'Tom', 'KRM': 'Tom', 'KRN': 'Tom', 'KRP': 'Tom', 'KRR': 'Tom',
    'KRS': 'Tom', 'KRU': 'Tom', 'KRV': 'Tom', 'KRW': 'Tom', 'KRX': 'Tom', 'KRY': 'Tom',
    'KSA': 'Tom', 'KSC': 'Tom', 'KSE': 'Tom', 'KSG': 'Tom', 'KSH': 'Tom', 'KSK': 'Tom',
    'KSL': 'Tom', 'KSN': 'Tom', 'KSP': 'Tom', 'KSR': 'Tom', 'KSS': 'Tom', 'KST': 'Tom',
    'KSU': 'Tom', 'KSV': 'Tom', 'KSW': 'Tom', 'KSX': 'Tom', 'KSY': 'Tom', 'KSZ': 'Tom',
    'KTA': 'Tom', 'KTC': 'Tom', 'KTD': 'Tom', 'KTE': 'Tom', 'KTF': 'Tom', 'KTG': 'Tom',
    'KTH': 'Tom', 'KTJ': 'Tom', 'KTK': 'Tom', 'KTL': 'Tom', 'KTN': 'Tom', 'KTQ': 'Tom',
    'KTR': 'Tom', 'KTT': 'Tom', 'KTU': 'Tom', 'KTV': 'Tom', 'KTW': 'Tom', 'KTX': 'Tom',
    'KTY': 'Tom', 'KTZ': 'Tom', 'KUA': 'Tom', 'KUB': 'Tom', 'KUC': 'Tom', 'KUD': 'Tom',
    'KUE': 'Tom', 'KUF': 'Tom', 'KUG': 'Tom', 'KUH': 'Tom', 'KUN': 'Tom', 'KUQ': 'Tom',
    'KVB': 'Tom', 'KVC': 'Tom', 'KVE': 'Tom', 'KVH': 'Tom', 'KVL': 'Tom', 'KVM': 'Tom',
    'KVN': 'Tom', 'KVP': 'Tom', 'KVQ': 'Tom', 'KVR': 'Tom', 'KVS': 'Tom', 'KVU': 'Tom',
    'KVW': 'Tom', 'KWA': 'Tom', 'KWC': 'Tom', 'KWE': 'Tom', 'KWG': 'Tom', 'KWH': 'Tom',
    'KWL': 'Tom', 'KWP': 'Tom', 'KWQ': 'Tom', 'KWR': 'Tom', 'KWT': 'Tom', 'KWW': 'Tom',
    'KWX': 'Tom', 'KZA': 'Tom', 'KZD': 'Tom',



    'L': 'Bill', 'LA': 'Bill', 'LB': 'Bill', 'LC': 'Bill', 'LD': 'Bill', 'LE': 'Bill', 'LF': 'Bill', 'LG': 'Bill',
    'LH': 'Bill', 'LJ': 'Bill', 'LT': 'Bill',

    'M': 'Jenny', 'ML': 'Jenny', 'MT': 'Jenny',

    'N': 'Jenny', 'NA': 'Jenny', 'NB': 'Jenny', 'NC': 'Jenny', 'ND': 'Jenny',
    'NE': 'Jenny', 'NK': 'Jenny', 'NX': 'Jenny',

    'P': 'Amanda', 'PA': 'Amanda', 'PB': 'Amanda', 'PC': 'Amanda', 'PD': 'Amanda', 'PE': 'Amanda',
    'PF': 'Amanda', 'PG': 'Amanda', 'PH': 'Amanda', 'PJ': 'Amanda', 'PK': 'Amanda', 'PL': 'Amanda', 'PM': 'Amanda',
    'PN': 'Amanda', 'PQ': 'Amanda', 'PR': 'Amanda', 'PS': 'Amanda', 'PT': 'Amanda', 'PZ': 'Amanda',

    'Q': 'Bill', 'QA': 'Bill', 'QB': 'Bill', 'QC': 'Bill', 'QD': 'Bill', 'QE': 'Bill', 'QH': 'Bill', 'QL': 'Bill',

    'QM': 'Tom', 'QP': 'Tom', 'QR': 'Tom',

    'R': 'Tom', 'RA': 'Tom',
    'RB': 'Tom', 'RC': 'Tom', 'RD': 'Tom', 'RE': 'Tom', 'RF': 'Tom', 'RG': 'Tom',
    'RJ': 'Tom', 'RK': 'Tom', 'RL': 'Tom', 'RM': 'Tom', 'RS': 'Tom', 'RT': 'Tom',
    'RV': 'Tom', 'RX': 'Tom', 'RZ': 'Tom',

    'S': 'Bill', 'SB': 'Bill', 'SD': 'Bill',
    'SF': 'Bill', 'SH': 'Bill', 'SK': 'Bill',

    'TD': 'Bill',
    'TR': 'Jenny',
    'TS': 'Bill',

    'T': 'Bill', 'TA': 'Bill', 'TC': 'Bill', 'TE': 'Bill', 'TF': 'Bill', 'TG': 'Bill', 'TH': 'Bill',
    'TJ': 'Bill', 'TK': 'Bill', 'TL': 'Bill', 'TN': 'Bill', 'TP': 'Bill',

    'TT': 'Jenny', 'TX': 'Jenny',

    'U': 'Freecart', 'UA': 'Freecart', 'UB': 'Freecart', 'UC': 'Freecart', 'UD': 'Freecart', 'UE': 'Freecart',
    'UF': 'Freecart', 'UG': 'Freecart', 'UH': 'Freecart',
    'V': 'Freecart', 'VA': 'Freecart', 'VB': 'Freecart', 'VC': 'Freecart', 'VD': 'Freecart',
    'VE': 'Freecart', 'VF': 'Freecart', 'VG': 'Freecart', 'VK': 'Freecart', 'VM': 'Freecart',

    'Z': 'Bill', 'ZA': 'Bill',


}

##########################################

def is_title(user_input):
    if user_input.isprintable() and not user_input.isdecimal():
        return True
    else:
        return False


def is_isbn(user_input):
    if il.is_isbn10(user_input) or il.is_isbn13(user_input):
        return True
    else:
        return False


def get_isbn(user_input):
    try:
        new_isbn = il.isbn_from_words(user_input)
    except:
        new_isbn = ""
    return new_isbn


def get_lcc(an_isbn):
    try:
        new_lcc = il.classify(an_isbn).get("lcc")
    except:
        new_lcc = ""
    return new_lcc

def get_title(an_isbn):
    try:
        the_title = il.meta(an_isbn, service="goob").get("Title")
    except:
        the_title = ""

    try:
        the_title = il.meta(an_isbn, service="wiki").get("Title")
    except:
        the_title = ""

    try:
        the_title = il.meta(an_isbn, service="openl").get("Title")
    except:
        the_title = ""

    return the_title

def get_results(the_lcc):
    lcc_class = ""

    if the_lcc:

        for char in the_lcc:
            if char.isdecimal():
                break
            else:
                lcc_class += char
        the_code = lcc_class.upper()

        if selector_dict.get(the_code):
            return selector_dict[the_code]
        else:
            return "Unknown Selector"

    else:
        return ""


def find_selector():
    the_title = ""
    if isbn_entry.get():

        u_input = isbn_entry.get().strip()
        isbn = u_input if is_isbn(u_input) else get_isbn(u_input)

        if isbn:
            the_lcc = get_lcc(isbn)
            the_title = get_title(isbn)
            if selector := get_results(the_lcc):
                selector_label["text"] = f"{selector}\n\n{the_lcc}\n\n{isbn}\n\n{the_title}"
            else:
                classify_http = "http://"
                classify_url = f"classify.oclc.org/classify2/ClassifyDemo?search-standnum-txt={isbn}&startRec=0"
                classify_link = classify_http + classify_url
                if the_title:
                    selector_label["text"] = f"CANNOT FIND ANYTHING - on clipboard: \n\n{the_title}"
                    pyperclip.copy(the_title)
                    #clear_text()
                    #isbn_entry.insert(0, the_title)

                else:
                    selector_label["text"] = "CANNOT FIND ANYTHING - try TITLE AUTHOR EDITION words"

        else:
            selector_label["text"] = "CANNOT FIND ANYTHING - try TITLE AUTHOR EDITION words"
    else:
        selector_label["text"] = "enter ISBN or TITLE AUTHOR EDITION words"

    clear_button.focus_set()


def oclc_classify():
    search_term = isbn_entry.get()
    classify_http = "http://"

    if search_term:

        if is_title(search_term):
            classify_url = f"{classify_http}classify.oclc.org/classify2/ClassifyDemo?search-title-txt={search_term}&startRec=0"
            webbrowser.open_new(classify_url)

        elif is_isbn(search_term):
            classify_url = f"{classify_http}classify.oclc.org/classify2/ClassifyDemo?search-standnum-txt={search_term}&startRec=0"
            webbrowser.open_new(classify_url)

        else:
            selector_label["text"] = "CANNOT REACH OCLC CLASSIFY"

    else:
        selector_label["text"] = "enter ISBN or TITLE AUTHOR EDITION words"
        isbn_entry.focus_set()

def one_search():
    search_term = isbn_entry.get()
    onesearch_http = "https://"
    url_2ndchunk = "&tab=Everything&search_scope=MyInst_and_CI&sortby=rank&vid=01MNPALS_MCT:MCT&mode=advanced&offset=0"

    if search_term:

        if is_title(search_term):
            url_1stchunk = "mnpals-mct.primo.exlibrisgroup.com/discovery/search?query=title,exact,"
            onesearch_url = f"{onesearch_http}{url_1stchunk}{search_term}{url_2ndchunk}"
            webbrowser.open_new(onesearch_url)

        elif is_isbn(search_term):
            url_1stchunk = "mnpals-mct.primo.exlibrisgroup.com/discovery/search?query=isbn,exact,"
            onesearch_url = f"{onesearch_http}{url_1stchunk}{search_term}{url_2ndchunk}"
            webbrowser.open_new(onesearch_url)

        else:
            selector_label["text"] = "CANNOT REACH OneSearch"

    else:
        selector_label["text"] = "enter ISBN or TITLE AUTHOR EDITION words"
        isbn_entry.focus_set()

def callnum_lookup():
    the_input = isbn_entry.get()

    tom_codes = ranges_dict["Tom"]
    bill_codes = ranges_dict["Bill"]
    jenny_codes = ranges_dict["Jenny"]
    amanda_codes = ranges_dict["Amanda"]
    freecart_codes = ranges_dict["Freecart"]
    
    if the_input.title() == "Tom":
        selector_label["text"] = f"{the_input.title()}\n\n owns these:\n\n {tom_codes}"

    elif the_input.title() == "Bill":
        selector_label["text"] = f"{the_input.title()}\n\n owns these:\n\n {bill_codes}"

    elif the_input.title() == "Jenny":
        selector_label["text"] = f"{the_input.title()}\n\n owns these:\n\n {jenny_codes}"

    elif the_input.title() == "Amanda":
        selector_label["text"] = f"{the_input.title()}\n\n owns these:\n\n {amanda_codes}"

    elif the_input.lower() == "free cart" or the_input.lower() == "freecart":
        selector_label["text"] = f"{the_input.title()}\n\n owns these:\n\n {freecart_codes}"

    elif the_input.lower() in ['i','o','w','x','y']:
        selector_label["text"] = "NOT A VALID LC CODE"

    else:
        an_lcc = the_input
        an_lcc_class = ""
        a_selector = ""
        if an_lcc:
            for char in an_lcc:
                if char.isdecimal():
                    break
                else:
                    an_lcc_class += char
            a_code = an_lcc_class.upper()

            if a_selector := selector_dict.get(a_code):
                selector_label["text"] = f"{a_code} is {a_selector}"
            else:
                selector_label["text"] = "CANNOT DETERMINE SELECTOR"

        else:
            selector_label["text"] = "enter LC CALL NUMBER or LC CLASS or LC SUBCLASS or SELECTOR NAME"
            isbn_entry.focus_set()

##############################################

def clear_text():
    isbn_entry.delete(0, tk.END)
    selector_label["text"] = ""
    isbn_entry.focus_set()

def quit_app():
    window.destroy()
    quit()

def hit_enter(event):
    find_selector()

################################################
window = tk.Tk()

window.title("Minneapolis College Library")
window.geometry("700x600")
window.resizable(False, False)

title_frame = tk.Frame(master=window)
title_label = tk.Label(
    text="PYTHON SELECTOR PARSER v2.0 © billthelibrarian",
    fg="#707372",
    bg="#ADCB00",
    height=2,
    width=80,
    font="arial",
    #textvariable=selector_data

)

entry_frame = tk.Frame(master=window, width=100, height=150, bg="#489FDF")
isbn_entry = tk.Entry(master=entry_frame, width=30, font="courier", justify="center")
isbn_entry.focus_set()

button_frame = tk.Frame(master=window, relief=tk.RAISED)
lookup_button = tk.Button(
    master=button_frame,
    text="FIND",
    font="arial",
    bg="#B2B4B2",
    height=2,
    width=7,
    command=find_selector

)

classify_button = tk.Button(
    master=button_frame,
    text="OCLC",
    font="arial",
    bg="#B2B4B2",
    height=2,
    width=7,
    command=oclc_classify

)

primo_button = tk.Button(
    master=button_frame,
    text="OneSearch",
    font="arial",
    bg="#B2B4B2",
    height=2,
    width=9,
    command=one_search

)

callnum_button = tk.Button(
    master=button_frame,
    text="LCC Lookup",
    font="arial",
    bg="#B2B4B2",
    height=2,
    width=11,
    command=callnum_lookup

)


clear_button = tk.Button(
    master=button_frame,
    text="CLEAR",
    font="arial",
    bg="#B2B4B2",
    height=2,
    width=7,
    command=clear_text
)

quit_button = tk.Button(
    master=button_frame,
    text="QUIT",
    font="arial",
    bg="#B2B4B2",
    height=2,
    width=7,
    command=quit_app
)

results_frame = tk.Frame(master=window)

selector_data = ""

selector_label = tk.Label(
    text="enter ISBN or TITLE AUTHOR EDITION words",
    fg="white",
    bg="#93328E",
    height=20,
    width=80,
    font="arial",
    wraplength=600
    #textvariable=selector_data

)


title_frame.grid(row=0, column=0)
title_label.grid(row=0, column=0)

entry_frame.grid(row=1, column=0)
isbn_entry.grid(row=1, column=0, padx=5, pady=5)

button_frame.grid(row=2, column=0)
lookup_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")
classify_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")
primo_button.grid(row=2, column=2, padx=10, pady=10, sticky="e")
callnum_button.grid(row=2, column=3, padx=10, pady=10, sticky="e")
clear_button.grid(row=2, column=4, padx=10, pady=10, sticky="e")
quit_button.grid(row=2, column=5, padx=10, pady=10, sticky="e")


results_frame.grid(row=3, column=0)
selector_label.grid(row=3, column=0, sticky="nw")

isbn_entry.bind("<Key-Return>", hit_enter)


window.mainloop()
#####################################################################################