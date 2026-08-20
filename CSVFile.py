

import csv
import openpyxl
import pandas as pd
from tabulate import tabulate
# import webbrowser   
# import requests

# # response = requests.get("https://www.google.com")

# # print(response.status_code)


# url = "https://www.google.com"

# webbrowser.open(url)




class CSV():
   
   def READCSVFILE():
       
       with open(r"C:\Users\KIMAYA\Desktop\Projects.xlsx", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


   def READEXELFILE():
      file = r"C:\Users\KIMAYA\Desktop\Projects.xlsx";
      df = pd.read_excel(file)
      print(df.columns)

      print(tabulate(df, headers="keys", tablefmt="grid"))





class CSV_JASON(CSV):
    pass
   

c=CSV_JASON
#c.READCSVFILE()
c.READEXELFILE()


