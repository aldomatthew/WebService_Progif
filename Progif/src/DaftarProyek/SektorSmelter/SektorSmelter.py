import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#14-Sektor Smelter
soup14 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/n-sektor-smelter/').read()
p_soup14 = bs.BeautifulSoup(soup14,'lxml')
tabel_14 = p_soup14.findAll('table')[0]
tabel_rows14 = tabel_14.findAll('tr')

csvFile = open("SektorSmelter.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row14 in tabel_rows14:
        csvRow14=[]
        for cell14 in row14.findAll('td'):
            
            #print(cell14.text, end = ' ')
            
            csvRow14.append(cell14.get_text().replace(" – ","-"))
        writer.writerow(csvRow14)
finally:
    csvFile.close()