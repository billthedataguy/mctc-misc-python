import easygui as g

import isbnlib as il

import sys

# U, V no longer collected

# TR848-TR861 jenny CINEMATOGRAPHY

selector_dict = {

    'C': 'Tom', 'CB': 'Tom', 'CC': 'Tom', 'CD': 'Tom', 'CE': 'Tom', 'CJ': 'Tom', 'CN': 'Tom', 'CR': 'Tom', 'CS': 'Tom',
    'CT': 'Tom', 'D': 'Tom', 'DA': 'Tom', 'DAW': 'Tom', 'DB': 'Tom', 'DC': 'Tom', 'DD': 'Tom', 'DE': 'Tom', 'DF': 'Tom',
    'DG': 'Tom', 'DH': 'Tom', 'DJ': 'Tom', 'DJK': 'Tom', 'DK': 'Tom', 'DL': 'Tom', 'DP': 'Tom', 'DQ': 'Tom', 'DR': 'Tom',
    'DS': 'Tom', 'DT': 'Tom', 'DU': 'Tom', 'DX': 'Tom', 'E': 'Tom', 'F': 'Tom', 'G': 'Tom', 'GA': 'Tom', 'GB': 'Tom',
    'GC': 'Tom', 'GE': 'Tom', 'GF': 'Tom', 'GN': 'Tom', 'GR': 'Tom', 'GT': 'Tom', 'H': 'Tom', 'HA': 'Tom', 'HB': 'Tom',
    'HC': 'Tom', 'HD': 'Tom', 'HE': 'Tom', 'HF': 'Tom', 'HG': 'Tom', 'HJ': 'Tom', 'HM': 'Tom', 'HN': 'Tom', 'HQ': 'Tom',
    'HS': 'Tom', 'HT': 'Tom', 'HV': 'Tom', 'HX': 'Tom', 'J': 'Tom', 'JA': 'Tom', 'JC': 'Tom', 'JF': 'Tom', 'JJ': 'Tom',
    'JK': 'Tom', 'JL': 'Tom', 'JN': 'Tom', 'JQ': 'Tom', 'JS': 'Tom', 'JV': 'Tom', 'JZ': 'Tom', 'B': 'Bill', 'BC': 'Bill',
    'BD': 'Bill', 'BF': 'Bill', 'BH': 'Bill', 'BJ': 'Bill', 'BL': 'Bill', 'BM': 'Bill', 'BP': 'Bill', 'BQ': 'Bill',
    'BR': 'Bill', 'BS': 'Bill', 'BT': 'Bill', 'BV': 'Bill', 'BX': 'Bill', 'L': 'Bill', 'LA': 'Bill', 'LB': 'Bill',
    'LC': 'Bill', 'LD': 'Bill', 'LE': 'Bill', 'LF': 'Bill', 'LG': 'Bill', 'LH': 'Bill', 'LJ': 'Bill', 'LT': 'Bill',
    'QA': 'Bill', 'T': 'Bill', 'TA': 'Bill', 'TC': 'Bill', 'TE': 'Bill', 'TF': 'Bill', 'TG': 'Bill', 'TH': 'Bill', 'TJ': 'Bill',
    'TK': 'Bill', 'TL': 'Bill', 'TN': 'Bill', 'TP': 'Bill', 'Z': 'Bill', 'ZA': 'Bill', 'M': 'jenny', 'ML': 'jenny',
    'MT': 'jenny', 'P': 'jenny', 'PA': 'jenny', 'PB': 'jenny', 'PC': 'jenny', 'PD': 'jenny', 'PE': 'jenny', 'PF': 'jenny',
    'PG': 'jenny', 'PH': 'jenny', 'PJ': 'jenny', 'PK': 'jenny', 'PL': 'jenny', 'PM': 'jenny', 'PN': 'jenny', 'PQ': 'jenny',
    'PR': 'jenny', 'PS': 'jenny', 'PT': 'jenny', 'PZ': 'jenny', 'TT': 'jenny', 'TX': 'jenny', 'A': 'Kathleen',
    'GV': 'Kathleen', 'K': 'Kathleen', 'KB': 'Kathleen', 'KBM': 'Kathleen', 'KBP': 'Kathleen', 'KBR': 'Kathleen',
    'KBU': 'Kathleen', 'KD': 'Kathleen', 'KDC': 'Kathleen', 'KDE': 'Kathleen', 'KDG': 'Kathleen', 'KDK': 'Kathleen',
    'KDZ': 'Kathleen', 'KE': 'Kathleen', 'KF': 'Kathleen', 'KG': 'Kathleen', 'KH': 'Kathleen', 'KJ': 'Kathleen',
    'KJA': 'Kathleen', 'KJC': 'Kathleen', 'KJE': 'Kathleen', 'KJG': 'Kathleen', 'KJH': 'Kathleen', 'KJJ': 'Kathleen',
    'KJK': 'Kathleen', 'KJM': 'Kathleen', 'KJN': 'Kathleen', 'KJP': 'Kathleen', 'KJR': 'Kathleen', 'KJS': 'Kathleen',
    'KJT': 'Kathleen', 'KJV': 'Kathleen', 'KJW': 'Kathleen', 'KK': 'Kathleen', 'KL': 'Kathleen', 'KM': 'Kathleen',
    'KN': 'Kathleen', 'KP': 'Kathleen', 'KQ': 'Kathleen', 'KKA': 'Kathleen', 'KKB': 'Kathleen', 'KKE': 'Kathleen',
    'KKF': 'Kathleen', 'KKG': 'Kathleen', 'KKH': 'Kathleen', 'KKI': 'Kathleen', 'KKJ': 'Kathleen', 'KKK': 'Kathleen',
    'KKL': 'Kathleen', 'KKM': 'Kathleen', 'KKN': 'Kathleen', 'KKP': 'Kathleen', 'KKQ': 'Kathleen', 'KKR': 'Kathleen',
    'KKS': 'Kathleen', 'KKT': 'Kathleen', 'KKV': 'Kathleen', 'KKW': 'Kathleen', 'KKX': 'Kathleen', 'KKY': 'Kathleen',
    'KKZ': 'Kathleen', 'KLA': 'Kathleen', 'KLB': 'Kathleen', 'KLD': 'Kathleen', 'KLE': 'Kathleen', 'KLF': 'Kathleen',
    'KLH': 'Kathleen', 'KLM': 'Kathleen', 'KLN': 'Kathleen', 'KLP': 'Kathleen', 'KLQ': 'Kathleen', 'KLR': 'Kathleen',
    'KLS': 'Kathleen', 'KLT': 'Kathleen', 'KLV': 'Kathleen', 'KLW': 'Kathleen', 'KMC': 'Kathleen', 'KME': 'Kathleen',
    'KMF': 'Kathleen', 'KMG': 'Kathleen', 'KMH': 'Kathleen', 'KMJ': 'Kathleen', 'KMK': 'Kathleen', 'KML': 'Kathleen',
    'KMM': 'Kathleen', 'KMN': 'Kathleen', 'KMP': 'Kathleen', 'KMQ': 'Kathleen', 'KMS': 'Kathleen', 'KMT': 'Kathleen',
    'KMU': 'Kathleen', 'KMV': 'Kathleen', 'KMX': 'Kathleen', 'KMY': 'Kathleen', 'KNC': 'Kathleen', 'KNE': 'Kathleen',
    'KNF': 'Kathleen', 'KNG': 'Kathleen', 'KNH': 'Kathleen', 'KNK': 'Kathleen', 'KNL': 'Kathleen', 'KNM': 'Kathleen',
    'KNN': 'Kathleen', 'KNP': 'Kathleen', 'KNQ': 'Kathleen', 'KNR': 'Kathleen', 'KNS': 'Kathleen', 'KNT': 'Kathleen',
    'KNV': 'Kathleen', 'KNW': 'Kathleen', 'KNX': 'Kathleen', 'KNY': 'Kathleen', 'KPA': 'Kathleen', 'KPC': 'Kathleen',
    'KPE': 'Kathleen', 'KPF': 'Kathleen', 'KPG': 'Kathleen', 'KPH': 'Kathleen', 'KPJ': 'Kathleen', 'KPK': 'Kathleen',
    'KPL': 'Kathleen', 'KPM': 'Kathleen', 'KPP': 'Kathleen', 'KPS': 'Kathleen', 'KPT': 'Kathleen', 'KPV': 'Kathleen',
    'KPW': 'Kathleen', 'KQC': 'Kathleen', 'KQE': 'Kathleen', 'KQG': 'Kathleen', 'KQH': 'Kathleen', 'KQJ': 'Kathleen',
    'KQK': 'Kathleen', 'KQM': 'Kathleen', 'KQP': 'Kathleen', 'KQT': 'Kathleen', 'KQV': 'Kathleen', 'KQW': 'Kathleen',
    'KQX': 'Kathleen', 'KR': 'Kathleen', 'KS': 'Kathleen', 'KT': 'Kathleen', 'KU': 'Kathleen', 'KV': 'Kathleen',
    'KW': 'Kathleen', 'KZ': 'Kathleen', 'KRB': 'Kathleen', 'KRC': 'Kathleen', 'KRE': 'Kathleen', 'KRG': 'Kathleen',
    'KRK': 'Kathleen', 'KRL': 'Kathleen', 'KRM': 'Kathleen', 'KRN': 'Kathleen', 'KRP': 'Kathleen', 'KRR': 'Kathleen',
    'KRS': 'Kathleen', 'KRU': 'Kathleen', 'KRV': 'Kathleen', 'KRW': 'Kathleen', 'KRX': 'Kathleen', 'KRY': 'Kathleen',
    'KSA': 'Kathleen', 'KSC': 'Kathleen', 'KSE': 'Kathleen', 'KSG': 'Kathleen', 'KSH': 'Kathleen', 'KSK': 'Kathleen',
    'KSL': 'Kathleen', 'KSN': 'Kathleen', 'KSP': 'Kathleen', 'KSR': 'Kathleen', 'KSS': 'Kathleen', 'KST': 'Kathleen',
    'KSU': 'Kathleen', 'KSV': 'Kathleen', 'KSW': 'Kathleen', 'KSX': 'Kathleen', 'KSY': 'Kathleen', 'KSZ': 'Kathleen',
    'KTA': 'Kathleen', 'KTC': 'Kathleen', 'KTD': 'Kathleen', 'KTE': 'Kathleen', 'KTF': 'Kathleen', 'KTG': 'Kathleen',
    'KTH': 'Kathleen', 'KTJ': 'Kathleen', 'KTK': 'Kathleen', 'KTL': 'Kathleen', 'KTN': 'Kathleen', 'KTQ': 'Kathleen',
    'KTR': 'Kathleen', 'KTT': 'Kathleen', 'KTU': 'Kathleen', 'KTV': 'Kathleen', 'KTW': 'Kathleen', 'KTX': 'Kathleen',
    'KTY': 'Kathleen', 'KTZ': 'Kathleen', 'KUA': 'Kathleen', 'KUB': 'Kathleen', 'KUC': 'Kathleen', 'KUD': 'Kathleen',
    'KUE': 'Kathleen', 'KUF': 'Kathleen', 'KUG': 'Kathleen', 'KUH': 'Kathleen', 'KUN': 'Kathleen', 'KUQ': 'Kathleen',
    'KVB': 'Kathleen', 'KVC': 'Kathleen', 'KVE': 'Kathleen', 'KVH': 'Kathleen', 'KVL': 'Kathleen', 'KVM': 'Kathleen',
    'KVN': 'Kathleen', 'KVP': 'Kathleen', 'KVQ': 'Kathleen', 'KVR': 'Kathleen', 'KVS': 'Kathleen', 'KVU': 'Kathleen',
    'KVW': 'Kathleen', 'KWA': 'Kathleen', 'KWC': 'Kathleen', 'KWE': 'Kathleen', 'KWG': 'Kathleen', 'KWH': 'Kathleen',
    'KWL': 'Kathleen', 'KWP': 'Kathleen', 'KWQ': 'Kathleen', 'KWR': 'Kathleen', 'KWT': 'Kathleen', 'KWW': 'Kathleen',
    'KWX': 'Kathleen', 'KZA': 'Kathleen', 'KZD': 'Kathleen', 'N': 'Kathleen', 'NA': 'Kathleen', 'NB': 'Kathleen',
    'NC': 'Kathleen', 'ND': 'Kathleen', 'NE': 'Kathleen', 'NK': 'Kathleen', 'NX': 'Kathleen', 'Q': 'Kathleen',
    'QB': 'Kathleen', 'QC': 'Kathleen', 'QD': 'Kathleen', 'QE': 'Kathleen', 'QH': 'Kathleen',
    'QL': 'Kathleen', 'QM': 'Kathleen', 'QP': 'Kathleen', 'QR': 'Kathleen', 'R': 'Kathleen', 'RA': 'Kathleen',
    'RB': 'Kathleen', 'RC': 'Kathleen', 'RD': 'Kathleen', 'RE': 'Kathleen', 'RF': 'Kathleen', 'RG': 'Kathleen',
    'RJ': 'Kathleen', 'RK': 'Kathleen', 'RL': 'Kathleen', 'RM': 'Kathleen', 'RS': 'Kathleen', 'RT': 'Kathleen',
    'RV': 'Kathleen', 'RX': 'Kathleen', 'RZ': 'Kathleen', 'S': 'Kathleen', 'SB': 'Kathleen', 'SD': 'Kathleen',
    'SF': 'Kathleen', 'SH': 'Kathleen', 'SK': 'Kathleen', 'TD': 'Kathleen', 'TR': 'Kathleen', 'TS': 'Kathleen'


                }

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

def get_results(the_lcc):
    lcc_class = ""
    cinematography = ["TR848", "TR849", "TR850", "TR851", "TR852", "TR853", "TR854", "TR855", "TR856", "TR857",
    "TR858", "TR859", "TR860", "TR861"]

    if the_lcc:
        if the_lcc in cinematography:
            #print(the_lcc, "jenny")
            g.msgbox(the_lcc, "jenny")

        else:

            for char in the_lcc:
                if char.isdecimal():
                    break
                else:
                    lcc_class += char
            the_code = lcc_class.upper()
            #print(f"{the_lcc}\n{the_code}")
            #g.msgbox(the_lcc, the_code)

            if selector_dict.get(the_code):
                #print(selector_dict[the_code])
                g.msgbox(the_code + " ---> " + selector_dict[the_code])
            else:
                #print("Unknown Collector")
                g.msgbox("Unknown Collector")

    else:
        #print("No lcc found.")
        g.msgbox("No lcc found.")


# TR848-TR861 jenny CINEMATOGRAPHY

msg = "Enter ISBN or title words: "
title = "Selector Sorter"






while True:

    u_input = g.enterbox(msg, title)
    #g.egdemo()

    if u_input is None:
        sys.exit()


    elif is_title(u_input):

        if (new_isbn := il.isbn_from_words(u_input)) and \
                (lcc := il.classify(new_isbn).get("lcc")):
            #print("Found lcc: ", lcc)
            #g.msgbox(str(new_isbn) + str(lcc))
            get_results(lcc)
        else:
            g.msgbox("Haven't the foggiest idea ...")


    elif is_isbn(u_input):

        lcc = il.classify(u_input).get("lcc")
        get_results(lcc)

    else:
        break




