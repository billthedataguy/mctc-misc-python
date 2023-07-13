import pandas as pd
import openpyxl

mn_first50 = pd.read_excel("Excel\mn_first50.xlsx")
mn_therest = pd.read_excel("Excel\mn_THEREST_9_1_2021.xlsx")

# mn_all = mn_therest.update(mn_first50)

print(mn_first50)
print(mn_therest)

mn_all = mn_therest.append(mn_first50)

print(mn_all.sort_values(by="facility"))

mn_all.to_excel("mn_ALL_9_1_2021.xlsx")

# mn_concat = pd.concat([mn_all500, mn_first50], ignore_index = True)
# mn_newMASTER = mn_concat.drop_duplicates(subset=["street", "facility"], keep=False)
#
#
#
#
# mn_newMASTER.to_excel("MN_newMASTER.xlsx")
#
# mn_next450 = mn_newMASTER[mn_newMASTER.street.isin(mn_first50.street) == False]
#
# mn_next450.to_excel("mn_next450.xlsx")

