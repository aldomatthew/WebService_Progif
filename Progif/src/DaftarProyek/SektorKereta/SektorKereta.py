import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#2-Sektor Kereta
soup2 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/b-sektor-kereta/').read()
p_soup2 = bs.BeautifulSoup(soup2,'lxml')
tabel_2 = p_soup2.findAll('table')[0]
tabel_rows2 = tabel_2.findAll('tr')
csvFile = open("SektorKereta.csv","wt", newline='')
writer = csv.writer(csvFile)
try:

    for row2 in tabel_rows2:
        csvRow2=[]
        for cell2 in row2.findAll('td'):
    
            #print(cell2.text, end = ' ')
            
            csvRow2.append(cell2.get_text().replace(" – ","-"))
        writer.writerow(csvRow2)
        #print(csvRow2)
finally:
  csvFile.close()


