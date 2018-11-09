import urllib
import urllib.request 
import bs4 as bs
import pandas 
import csv
#1
#
soup1 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/transportasi-perkotaan/mrt-jakarta-jalur-selatan-utara/').read()
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


#
soup2 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/transportasi-perkotaan/lrt-jakarta-bogor-depok-bekasi/').read()
p_soup2 = bs.BeautifulSoup(soup2,'lxml')
title_2 = p_soup2.findAll('div',class_='container')[3]
get_title_2 = title_2.h1.text
print(get_title_2)
mylist.append(get_title_2)
print(mylist)
tabel_2 = p_soup2.findAll('table')[0]
get_tbody_2 = tabel_2.findAll('tbody')[0]
get_tr_2 = get_tbody_2.findAll('tr')[0]
get_invest2 = get_tr_2.findAll('td')[2].get_text()
print(get_invest2)
mylist2.append(get_invest2)
print(mylist)

#

soup3 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/transportasi-perkotaan/lrt-jakarta-bogor-depok-bekasi/').read()
p_soup3 = bs.BeautifulSoup(soup3,'lxml')
title_3 = p_soup3.findAll('div',class_='container')[3]
get_title_3 = title_3.h1.text
print(get_title_3)
tabel_3 = p_soup3.findAll('table')[0]
get_tbody_3 = tabel_3.findAll('tbody')[0]
get_tr_3 = get_tbody_3.findAll('tr')[0]
get_invest3 = get_tr_3.findAll('td')[2].get_text()
print(get_invest3)
mylist.append(get_title_3)
mylist2.append(get_invest3)


df = pandas.DataFrame(data={"nama_proyek": mylist, "nilai_investasi": mylist2})
df.to_csv("ProyekTransportasiKota", sep=',',index=False)


#mylist.append(get_invest1)

