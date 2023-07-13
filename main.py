import pandas as pd
import openpyxl

mn_first50 = pd.read_excel("MINNESOTA_FIRST50.xlsx")
mn_all500 = pd.read_excel("MINNESOTA_ALL500.xlsx")

mn_all500.update(mn_first50)
print(mn_all500)

mn_all500.to_excel("MN_UPDATED_500.xlsx")

