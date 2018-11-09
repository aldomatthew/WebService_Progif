import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#15-Sektor Pertanian
soup15 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/o-sektor-pertanian-kelautan/').read()
p_soup15 = bs.BeautifulSoup(soup15,'lxml')
tabel_15 = p_soup15.findAll('table')[0]
tabel_rows15 = tabel_15.findAll('tr')

csvFile = open("SektorPertanian.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row15 in tabel_rows15:
        csvRow15=[]
        for cell15 in row15.findAll('td'):
            
            #print(cell15.text, end = ' ')
            
            csvRow15.append(cell15.get_text().replace(" – ","-"))
        writer.writerow(csvRow15)
finally:
    csvFile.close()
