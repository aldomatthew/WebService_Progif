import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#12-Sektor Teknologi
soup12 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/l-sektor-teknologi/').read()
p_soup12 = bs.BeautifulSoup(soup12,'lxml')
tabel_12 = p_soup12.findAll('table')[0]
tabel_rows12 = tabel_12.findAll('tr')

csvFile = open("SektorTeknologi.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row12 in tabel_rows12:
        csvRow12=[]
        for cell12 in row12.findAll('td'):
            
            #print(cell12.text, end = ' ')
            
            csvRow12.append(cell12.get_text().replace(" – ","-"))
        writer.writerow(csvRow12)
finally:
    csvFile.close()