import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#13-Sektor Kawasan
soup13 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/m-sektor-kawasan/').read()
p_soup13 = bs.BeautifulSoup(soup13,'lxml')
tabel_13 = p_soup13.findAll('table')[0]
tabel_rows13 = tabel_13.findAll('tr')

csvFile = open("SektorKawasan.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row13 in tabel_rows13:
        csvRow13=[]
        for cell13 in row13.findAll('td'):
            
            #print(cell13.text, end = ' ')
            
            csvRow13.append(cell13.get_text().replace(" – ","-"))
        writer.writerow(csvRow13)
finally:
    csvFile.close()