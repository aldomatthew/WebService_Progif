import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#17-Sektor Industri Pesawat
soup17 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/q-program-industri-pesawat/').read()
p_soup17 = bs.BeautifulSoup(soup17,'lxml')
tabel_17 = p_soup17.findAll('table')[0]
tabel_rows17 = tabel_17.findAll('tr')

csvFile = open("SektorIndustriPesawat.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row17 in tabel_rows17:
        csvRow17=[]
        for cell17 in row17.findAll('td'):
            
            #print(cell17.text, end = ' ')
            
            csvRow17.append(cell17.get_text().replace(" – ","-"))
        writer.writerow(csvRow17)
finally:
    csvFile.close()