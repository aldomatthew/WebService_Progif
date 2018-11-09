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

#2-Sektor Kereta
soup2 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/b-sektor-kereta/').read()
p_soup2 = bs.BeautifulSoup(soup2,'lxml')
tabel_2 = p_soup2.findAll('table')[0]
tabel_rows2 = tabel_2.findAll('tr')

#3-Sektor Bandara
soup3 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/c-sektor-bandar-udara/').read()
p_soup3 = bs.BeautifulSoup(soup3,'lxml')
tabel_3 = p_soup3.findAll('table')[0]
tabel_rows3 = tabel_3.findAll('tr')
#4-Sektor Pelabuhan
soup4 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/d-sektor-pelabuhan/').read()
p_soup4 = bs.BeautifulSoup(soup4,'lxml')
tabel_4 = p_soup4.findAll('table')[0]
tabel_rows4 = tabel_4.findAll('tr')
#5-Sektor Perumahan
soup5 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/e-sektor-perumahan/').read()
p_soup5 = bs.BeautifulSoup(soup5,'lxml')
tabel_5 = p_soup5.findAll('table')[0]
tabel_rows5 = tabel_5.findAll('tr')

#6-Sektor Energi
soup6 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/f-sektor-energi/').read()
p_soup6 = bs.BeautifulSoup(soup6,'lxml')
tabel_6 = p_soup6.findAll('table')[0]
tabel_rows6 = tabel_6.findAll('tr')

#7-Sektor Air Bersih
soup7 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/g-sektor-air-bersih-dan-sanitasi/').read()
p_soup7 = bs.BeautifulSoup(soup7,'lxml')
tabel_7 = p_soup7.findAll('table')[0]
tabel_rows7 = tabel_7.findAll('tr')

#8-Sektor Tanggul Laut
soup8 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/h-sektor-tanggul-laut/').read()
p_soup8 = bs.BeautifulSoup(soup8,'lxml')
tabel_8 = p_soup8.findAll('table')[0]
tabel_rows8 = tabel_8.findAll('tr')

#9-Sektor PLBN
soup9 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/i-sektor-plbn/').read()
p_soup9 = bs.BeautifulSoup(soup9,'lxml')
tabel_9 = p_soup9.findAll('table')[0]
tabel_rows9 = tabel_9.findAll('tr')

#10-Sektor Bendungan
soup10 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/j-sektor-bendungan/').read()
p_soup10 = bs.BeautifulSoup(soup10,'lxml')
tabel_10 = p_soup10.findAll('table')[0]
tabel_rows10 = tabel_10.findAll('tr')

#11-Sektor Irigasi
soup11 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/k-sektor-irigasi/').read()
p_soup11 = bs.BeautifulSoup(soup11,'lxml')
tabel_11 = p_soup11.findAll('table')[0]
tabel_rows11 = tabel_11.findAll('tr')
#12-Sektor Teknologi
soup12 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/l-sektor-teknologi/').read()
p_soup12 = bs.BeautifulSoup(soup12,'lxml')
tabel_12 = p_soup12.findAll('table')[0]
tabel_rows12 = tabel_12.findAll('tr')
#13-Sektor Kawasan
soup13 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/m-sektor-kawasan/').read()
p_soup13 = bs.BeautifulSoup(soup13,'lxml')
tabel_13 = p_soup13.findAll('table')[0]
tabel_rows13 = tabel_13.findAll('tr')
#14-Sektor Smelter
soup14 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/n-sektor-smelter/').read()
p_soup14 = bs.BeautifulSoup(soup14,'lxml')
tabel_14 = p_soup11.findAll('table')[0]
tabel_rows14 = tabel_14.findAll('tr')
#15-Sektor Pertanian
soup15 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/o-sektor-pertanian-kelautan/').read()
p_soup15 = bs.BeautifulSoup(soup15,'lxml')
tabel_15 = p_soup15.findAll('table')[0]
tabel_rows15 = tabel_15.findAll('tr')

#16-Sektor Ketenagalistrikan
soup16 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/p-program-ketenagalistrikan/').read()
p_soup16 = bs.BeautifulSoup(soup16,'lxml')
tabel_16 = p_soup16.findAll('table')[0]
tabel_rows16 = tabel_16.findAll('tr')
#17-Sektor Industri Pesawat
soup17 = urllib.request.urlopen('https://kppip.go.id/proyek-strategis-nasional/q-program-industri-pesawat/').read()
p_soup17 = bs.BeautifulSoup(soup17,'lxml')
tabel_17 = p_soup17.findAll('table')[0]
tabel_rows17 = tabel_17.findAll('tr')

#########
#membuat file csv
#open file csv dan melakukan write terhadap file tersebut
csvFile = open("DaftarProyek.csv","wt", newline='')
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
    #2
    for row2 in tabel_rows2:
        csvRow2=[]
        for cell2 in row2.findAll('td'):
    
            #print(cell2.text, end = ' ')
            
            csvRow2.append(cell2.get_text().replace(" – ","-"))
        writer.writerow(csvRow2)
        print(csvRow2)
        
    #3
    for row3 in tabel_rows3:
        csvRow3=[]
        for cell3 in row3.findAll('td'):
            
            #print(cell3.text, end = ' ')
            
            csvRow3.append(cell3.get_text().replace(" – ","-"))
        writer.writerow(csvRow3)
        print(csvRow3)
        
    #4
    
    for row4 in tabel_rows4:
        csvRow4=[]
        for cell4 in row4.findAll('td'):
            
            #print(cell4.text, end = ' ')
            
            csvRow4.append(cell4.get_text().replace(" – ","-"))
        writer.writerow(csvRow4)
        print(csvRow4)
    #5
    for row5 in tabel_rows5:
        csvRow5=[]
        for cell5 in row5.findAll('td'):
            
            #print(cell5.text, end = ' ')
            
            csvRow5.append(cell5.get_text().replace(" – ","-"))
        writer.writerow(csvRow5)
        print(csvRow5)
    #
    for row6 in tabel_rows6:
        csvRow6=[]
        for cell6 in row6.findAll('td'):
            
            #print(cell6.text, end = ' ')
            
            csvRow6.append(cell6.get_text().replace(" – ","-"))
        writer.writerow(csvRow6)
        print(csvRow6)
    #
    for row7 in tabel_rows7:
        csvRow7=[]
        for cell7 in row7.findAll('td'):
            
            #print(cell7.text, end = ' ')
            
            csvRow7.append(cell7.get_text().replace(" – ","-"))
        writer.writerow(csvRow7)
    #
    for row8 in tabel_rows8:
        csvRow8=[]
        for cell8 in row8.findAll('td'):
            
            #print(cell8.text, end = ' ')
            
            csvRow8.append(cell8.get_text().replace(" – ","-"))
        writer.writerow(csvRow8)
    #
    for row9 in tabel_rows9:
        csvRow9=[]
        for cell9 in row9.findAll('td'):
            
            #print(cell9.text, end = ' ')
            
            csvRow5.append(cell5.get_text().replace(" – ","-"))
        writer.writerow(csvRow5)

    #
    for row10 in tabel_rows10:
        csvRow10=[]
        for cell10 in row1.findAll('td'):
            
            #print(cell10.text, end = ' ')
            
            csvRow10.append(cell10.get_text().replace(" – ","-"))
        writer.writerow(csvRow10)
    #
    for row11 in tabel_rows11:
        csvRow11=[]
        for cell11 in row11.findAll('td'):
            
            #print(cell11.text, end = ' ')
            
            csvRow11.append(cell11.get_text().replace(" – ","-"))
        writer.writerow(csvRow11)
    #
    for row12 in tabel_rows12:
        csvRow12=[]
        for cell12 in row12.findAll('td'):
            
            #print(cell12.text, end = ' ')
            
            csvRow12.append(cell12.get_text().replace(" – ","-"))
        writer.writerow(csvRow12)
    #
    
    for row13 in tabel_rows13:
        csvRow13=[]
        for cell13 in row13.findAll('td'):
            
            #print(cell13.text, end = ' ')
            
            csvRow13.append(cell13.get_text().replace(" – ","-"))
        writer.writerow(csvRow13)
    #
    for row14 in tabel_rows14:
        csvRow14=[]
        for cell14 in row14.findAll('td'):
            
            #print(cell14.text, end = ' ')
            
            csvRow14.append(cell4.get_text().replace(" – ","-"))
        writer.writerow(csvRow14)
    #
    for row15 in tabel_rows15:
        csvRow15=[]
        for cell15 in row15.findAll('td'):
            
            #print(cell15.text, end = ' ')
            
            csvRow15.append(cell15.get_text().replace(" – ","-"))
        writer.writerow(csvRow15)
    #
    for row16 in tabel_rows16:
        csvRow16=[]
        for cell16 in row16.findAll('td'):
            
            #print(cell16.text, end = ' ')
            
            csvRow16.append(cell16.get_text().replace(" – ","-"))
        writer.writerow(csvRow16)
    #
    for row17 in tabel_rows17:
        csvRow17=[]
        for cell17 in row17.findAll('td'):
            
            #print(cell17.text, end = ' ')
            
            csvRow17.append(cell17.get_text().replace(" – ","-"))
        writer.writerow(csvRow17)

finally:
    csvFile.close()

#########THE END############# 

    


