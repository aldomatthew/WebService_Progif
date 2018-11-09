import urllib
import urllib.request 
import bs4 as bs
import pandas 
import csv
#1
#
soup1 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/teknologi-informasi/palapa-ring-broadband-2/').read()
#
p_soup1 = bs.BeautifulSoup(soup1,'lxml')
#
title_1 = p_soup1.findAll('div',class_='container')[3]
get_title_1 = title_1.h1.text
print(get_title_1)

mylist = []
mylist2=[]


mylist.append(get_title_1)
print(mylist)
tabel_1 = p_soup1.findAll('table')[0]
get_tbody_1 = tabel_1.findAll('tbody')[0]
get_tr_1 = get_tbody_1.findAll('tr')[0]
get_invest1 = get_tr_1.findAll('td')[2].get_text()
print(get_invest1)

mylist2.append(get_invest1)
print (mylist2)


df = pandas.DataFrame(data={"nama_proyek": mylist, "nilai_investasi": mylist2})
df.to_csv("ProyekTeknologiInformasi.csv", sep=',',index=False)



