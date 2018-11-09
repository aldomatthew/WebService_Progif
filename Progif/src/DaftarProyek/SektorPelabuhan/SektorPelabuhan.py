import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#4-Sektor Pelabuhan
soup4 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/d-sektor-pelabuhan/').read()
p_soup4 = bs.BeautifulSoup(soup4,'lxml')
tabel_4 = p_soup4.findAll('table')[0]
tabel_rows4 = tabel_4.findAll('tr')
csvFile = open("SektorPelabuhan.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
	    
    for row4 in tabel_rows4:
        csvRow4=[]
        for cell4 in row4.findAll('td'):
            
            #print(cell4.text, end = ' ')
            
            csvRow4.append(cell4.get_text().replace(" – ","-"))
        writer.writerow(csvRow4)
        #print(csvRow4)
finally:
	csvFile.close()