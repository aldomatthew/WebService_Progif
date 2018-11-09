import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#5-Sektor Perumahan
soup5 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/e-sektor-perumahan/').read()
p_soup5 = bs.BeautifulSoup(soup5,'lxml')
tabel_5 = p_soup5.findAll('table')[0]
tabel_rows5 = tabel_5.findAll('tr')
csvFile = open("SektorPerumahan.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row5 in tabel_rows5:
        csvRow5=[]
        for cell5 in row5.findAll('td'):
            
            #print(cell5.text, end = ' ')
            
            csvRow5.append(cell5.get_text().replace(" – ","-"))
        writer.writerow(csvRow5)
        #print(csvRow5)
finally:
	csvFile.close()