import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#11-Sektor Irigasi
soup11 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/k-sektor-irigasi/').read()
p_soup11 = bs.BeautifulSoup(soup11,'lxml')
tabel_11 = p_soup11.findAll('table')[0]
tabel_rows11 = tabel_11.findAll('tr')

csvFile = open("SektorIrigasi.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row11 in tabel_rows11:
        csvRow11=[]
        for cell11 in row11.findAll('td'):
            
            #print(cell11.text, end = ' ')
            
            csvRow11.append(cell11.get_text().replace(" – ","-"))
        writer.writerow(csvRow11)
finally:
    csvFile.close()