import urllib
import urllib.request 
import bs4 as bs
import pandas as pd
import csv

#1-Sektor Jalan
#Melakukan request dan open website yang dituju
soup1 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/a-sektor-jalan/').read()
#BeautifulSoup
p_soup1 = bs.BeautifulSoup(soup1,'lxml')
#Mencari semua tabel dengan index 0 , karena tabel nya cuman satu
tabel_1 = p_soup1.findAll('table')[0]
#Di dalam tabel mencari tr
tabel_rows1 = tabel_1.findAll('tr')

csvFile = open("SektorJalan.csv","wt", newline='')
writer = csv.writer(csvFile)
try:
	#melakukan loop untuk mencari setiap data
	#melakukan loop untuk setiap sektor yang ada sesuai dengan urutan
    #1
    for row1 in tabel_rows1:
        csvRow1=[]
        for cell1 in row1.findAll('td'):
            #
            
            #print(cell3.text, end = ' ')
            #mengambil text yang ada di dalam td dan melakukan replace
            csvRow1.append(cell1.get_text().replace(" – ","-"))
        writer.writerow(csvRow1) #menulis kedalam file csv
        print(csvRow1)
finally:
    csvFile.close()