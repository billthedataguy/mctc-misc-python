import requests

req_url = "http://minneapoliscollegestore.com/SelectTermDept/Department?"

params = {
            "termId" : "12889",

            "input name" : "_RequestVerificationToken",

            "type" : "hidden",
            
            "value" : "6KDlCYrG7Vwrmsy4kxBP_42Jswi9Y8MgEDDUDKrxjHE2a3ks53Icifg4VP8_uZj645SR1DfwJ7cXUA6vU6HqhZFkQ2k1"
            


         }

dept = requests.post(req_url, data = params)



print(dept.status_code)           

print(dept.text)

