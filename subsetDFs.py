import pandas as pd
import openpyxl

mn_first50 = pd.read_excel("Excel\MINNESOTA_FIRST50.xlsx")
mn_all500 = pd.read_excel("Excel\MINNESOTA_ALL500.xlsx")

#mn_all500.update(mn_first50)

#mn_next450 = mn_all500 - mn_first50


#print(mn_next450)

mn_concat = pd.concat([mn_all500, mn_first50], ignore_index = True)
mn_newMASTER = mn_concat.drop_duplicates(subset=["street", "facility"], keep=False)




mn_newMASTER.to_excel("Excel\MN_newMASTER.xlsx")

mn_next450 = mn_newMASTER[mn_newMASTER.street.isin(mn_first50.street) == False]

mn_next450.to_excel("Excel\mn_next450.xlsx")

