import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#8-Sektor Tanggul Laut
soup8 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/h-sektor-tanggul-laut/').read()
p_soup8 = bs.BeautifulSoup(soup8,'lxml')
tabel_8 = p_soup8.findAll('table')[0]
tabel_rows8 = tabel_8.findAll('tr')

csvFile = open("SektorTanggulLaut.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row8 in tabel_rows8:
        csvRow8=[]
        for cell8 in row8.findAll('td'):
            
            #print(cell8.text, end = ' ')
            
            csvRow8.append(cell8.get_text().replace(" – ","-"))
        writer.writerow(csvRow8)
finally:
	csvFile.close()                    
