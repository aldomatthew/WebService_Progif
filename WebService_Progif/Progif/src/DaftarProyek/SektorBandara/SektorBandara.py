import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#3-Sektor Bandara
soup3 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/c-sektor-bandar-udara/').read()
p_soup3 = bs.BeautifulSoup(soup3,'lxml')
tabel_3 = p_soup3.findAll('table')[0]
tabel_rows3 = tabel_3.findAll('tr')
csvFile = open("SektorKereta.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row3 in tabel_rows3:
        csvRow3=[]
        for cell3 in row3.findAll('td'):
            
            #print(cell3.text, end = ' ')
            
            csvRow3.append(cell3.get_text().replace(" – ","-"))
        writer.writerow(csvRow3)
        #print(csvRow3)
finally:
	csvFile.close()
