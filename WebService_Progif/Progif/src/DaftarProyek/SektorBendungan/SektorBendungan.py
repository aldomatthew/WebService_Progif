import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#10-Sektor Bendungan
soup10 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/j-sektor-bendungan/').read()
p_soup10 = bs.BeautifulSoup(soup10,'lxml')
tabel_10 = p_soup10.findAll('table')[0]
tabel_rows10 = tabel_10.findAll('tr')

csvFile = open("SektorPLBN.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row10 in tabel_rows10:
        csvRow10=[]
        for cell10 in row10.findAll('td'):
            
            #print(cell10.text, end = ' ')
            
            csvRow10.append(cell10.get_text().replace(" – ","-"))
        writer.writerow(csvRow10)
finally:
    csvFile.close()