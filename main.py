import os, pandas as pd, numpy as np, pickle, zipfile, shutil, sys
os.chdir("C:\\Github\\HFaaS\\GitHub\\")
sys.path.append("C:\\Github\\HFaaS\\GitHub\\")
import sec2df


cik2ticker = pd.read_csv ("C:\\Github\\HFaaS\\Data\\cik2ticker.csv")[['cik', 'ticker']]
sec = updateSECs()

a = read_sec ("C:\\Github\\HFaaS\\temp\\temp\\", cik2ticker)

b = download_Financials_From_Google("MSFT", "NASDAQ")

######################### END of main program








