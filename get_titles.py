import csv
import pandas as pd


def clean_title(a_ser):
    return a_ser.str.replace(":", "").str.replace(".", "")


filename = "title_list.txt"

df = pd.read_csv(filename, delimiter="\t")
df = df.dropna(subset=["Title"])
clean_title_list = clean_title(df["Title"])

for clean in clean_title_list:
    print(clean)

print(len(clean_title_list))

joined_list = "\n".join(clean_title_list)

print(f"Here's the reconstituted list as one big string:\n\n{joined_list.strip()}")
