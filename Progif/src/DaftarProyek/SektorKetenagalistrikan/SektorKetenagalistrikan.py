import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#16-Sektor Ketenagalistrikan
soup16 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/p-program-ketenagalistrikan/').read()
p_soup16 = bs.BeautifulSoup(soup16,'lxml')
tabel_16 = p_soup16.findAll('table')[0]
tabel_rows16 = tabel_16.findAll('tr')

csvFile = open("SektorKetenagalistrikan.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row16 in tabel_rows16:
        csvRow16=[]
        for cell16 in row16.findAll('td'):
            
            #print(cell16.text, end = ' ')
            
            csvRow16.append(cell16.get_text().replace(" – ","-"))
        writer.writerow(csvRow16)
finally:
    csvFile.close()