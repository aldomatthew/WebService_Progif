import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#7-Sektor Air Bersih
soup7 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/g-sektor-air-bersih-dan-sanitasi/').read()
p_soup7 = bs.BeautifulSoup(soup7,'lxml')
tabel_7 = p_soup7.findAll('table')[0]
tabel_rows7 = tabel_7.findAll('tr')

csvFile = open("SektorAirdanSanitas.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
    for row7 in tabel_rows7:
        csvRow7=[]
        for cell7 in row7.findAll('td'):
            
            #print(cell7.text, end = ' ')
            
            csvRow7.append(cell7.get_text().replace(" – ","-"))
        writer.writerow(csvRow7)
finally:
	csvFile.close()
