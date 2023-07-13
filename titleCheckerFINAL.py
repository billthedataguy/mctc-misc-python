import pandas as pd
import requests
import urllib
import time

##################################################################################################################
def search_primo(title):

    encoded_title = f'{urllib.parse.quote(title)}'

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
    query = f"&q=title,begins_with,{encoded_title},AND;rtype,exact,books,AND"

    primo_url1 = r'https://mnpals-mct.primo.exlibrisgroup.com/discovery/search?query=title,begins_with,'
    primo_url2 = f"{encoded_title},AND&pfilter=rtype,exact,books,AND&tab=Everything&search_scope=MyInst_and_CI&sortby=title&vid=01MNPALS_MCT:MCT&mode=advanced&offset=0"

    r = requests.get(f"{url}{query}", params=payload)

    print("CHECKING ... ", title)

    try:
        json_response = r.json()
        recs_found = json_response["info"]["total"]
        if recs_found > 0:

            print(f"{title.upper()}")
            print(f"{recs_found} records found")
            print(f"{primo_url1}{primo_url2}")
            print(f"JSON: {json_response}\n\n")


    except:
        print(f'CANNOT DETERMINE HOW MANY RECS')

    time.sleep(1)


##################################################################################################################

##################################################################################################################
def getSearchTerms():

    filename = input("Enter filename (no extension): ")
    filepath = f"C:\\Users\\ej2595ht\\Desktop\\COLLECTIONS_2022\\{filename}.txt"

    df = pd.read_csv(filepath, delimiter="\t", encoding="utf-8")

    df = df.fillna("", axis=0)

    search_terms = sorted(df["Title"].tolist())

    print("SEARCH_TERMS: ", search_terms)

    for term in search_terms:

        if term != "":
            full_title = term.replace(":", "").replace(".", "").strip()
            if ";" in full_title:
                full_title = full_title.split(";")[0]
            search_primo(full_title)

##################################################################################################################

getSearchTerms()