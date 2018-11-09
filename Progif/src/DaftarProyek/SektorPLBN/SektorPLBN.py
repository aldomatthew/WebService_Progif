import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#9-Sektor PLBN
soup9 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/i-sektor-plbn/').read()
p_soup9 = bs.BeautifulSoup(soup9,'lxml')
tabel_9 = p_soup9.findAll('table')[0]
tabel_rows9 = tabel_9.findAll('tr')

csvFile = open("SektorPLBN.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row9 in tabel_rows9:
        csvRow9=[]
        for cell9 in row9.findAll('td'):
            
            #print(cell9.text, end = ' ')
            
            csvRow9.append(cell9.get_text().replace(" – ","-"))
        writer.writerow(csvRow9)
finally:
    csvFile.close()
