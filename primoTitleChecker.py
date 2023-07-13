import pandas as pd
import requests
import urllib
import time

#############################################################################################
encoded_title = ""
author_lastname = ""

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
    "q" : f"title,begins_with,{encoded_title},AND;creator,contains,{author_lastname},AND;rtype,exact,books,AND,",
    "qExclude" : "",
    "qInclude" : "",
    "rapido" : False,
    "refEntryActive" : False,
    "rtaLinks" : True,
    "scope" : "MyInst_and_CI",
    "searchInFulltextUserSelection" : False,
    "skipDelivery" : "Y",
    "sort" : "title",
    "tab" : "Everything",
    "vid" : "01MNPALS_MCT:MCT",
}

url = r"https://mnpals-mct.primo.exlibrisgroup.com/primaws/rest/pub/pnxs?"
#############################################################################################


def search_primo(main_title, author_lastname):
    encoded_title = f'{urllib.parse.quote(main_title)}'
    encoded_author_lastname = f'{urllib.parse.quote(author_lastname)}'

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
        "q": f"title,begins_with,{encoded_title},ANDcreator,contains,{encoded_author_lastname},AND;rtype,exact,books,AND,",
        "qExclude": "",
        "qInclude": "",
        "rapido": False,
        "refEntryActive": False,
        "rtaLinks": True,
        "scope": "MyInst_and_CI",
        "searchInFulltextUserSelection": False,
        "skipDelivery": "Y",
        "sort": "title",
        "tab": "Everything",
        "vid": "01MNPALS_MCT:MCT",
                }

    url = r"https://mnpals-mct.primo.exlibrisgroup.com/primaws/rest/pub/pnxs?"


    r = requests.get(url, params=payload)

    primo_url1 = r'https://mnpals-mct.primo.exlibrisgroup.com/discovery/search?'

    primo_url2 = f'query=title,begins_with,{encoded_title},AND&query=creator,contains,{encoded_author_lastname},AND&pfilter=rtype,exact,books,AND&tab=Everything&search_scope=MyInst_and_CI&sortby=title&vid=01MNPALS_MCT:MCT&mode=advanced&offset=0'

    print(f'<a href="{primo_url1}{primo_url2}">link</a><br>')

    print(f'TOTAL RECS FOUND= {r.json()["info"]["total"]}')

    time.sleep(3)


df_Z = pd.read_csv("C:\\Users\\ej2595ht\\Desktop\\COLLECTIONS_2022\\Bill_Z_2022_FINAL.txt", delimiter="\t")

Z = list(zip(df_Z["Title"].dropna(axis=0).tolist(), df_Z["Author"].dropna(axis=0).tolist()))

Z_sort = sorted(Z)

for tup in Z_sort[5:10]:
    title, author = tup

    main_title = title.split(":", 1)[0].replace(".", "").strip()
    author_lastname = author.split(",", 1)[0].strip()
    # print(main_title)
    # print(author_lastname)
    new_tup = (main_title, author_lastname)
    print(new_tup)
    search_primo(main_title, author_lastname)
    print("\n\n")