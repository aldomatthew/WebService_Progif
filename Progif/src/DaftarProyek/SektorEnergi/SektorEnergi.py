import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#6-Sektor Energi
soup6 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/f-sektor-energi/').read()
p_soup6 = bs.BeautifulSoup(soup6,'lxml')
tabel_6 = p_soup6.findAll('table')[0]
tabel_rows6 = tabel_6.findAll('tr')

csvFile = open("SektorEnergi.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row6 in tabel_rows6:
        csvRow6=[]
        for cell6 in row6.findAll('td'):
            
            #print(cell6.text, end = ' ')
            
            csvRow6.append(cell6.get_text().replace(" – ","-"))
        writer.writerow(csvRow6)
        #print(csvRow6)
finally:
	csvFile.close()

