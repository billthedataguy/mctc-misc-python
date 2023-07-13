import isbnlib as il


while True:
    u_input = input("Enter data or q: ")
    if u_input == "q":
        break
    elif u_input == "":
        continue
    else:
        isbn13 = get_isbn(u_input.strip())
        try:
            bookcover_url = il.cover(isbn13).get("thumbnail", "/no_image_available.png")
        except:
            bookcover_url = "/no_image_available.png"

        print(bookcover_url)

        api_dict = get_api_data(isbn13)

        if all(v for v in api_dict.values() if v is not None):
            #print(f"API FINAL DICT: {api_dict}")
            pp.pprint(make_links(api_dict))
        else:
            #print(f"INCOMPLETE API DICT {api_dict}")
            scrape_dict = code_dispatch(api_dict)

            #print(len([v for k,v in scrape_dict.items() if scrape_dict[k]]))

            print(f"SCRAPE FINAL DICT: {scrape_dict}")
            pp.pprint(make_links(scrape_dict))

        continue