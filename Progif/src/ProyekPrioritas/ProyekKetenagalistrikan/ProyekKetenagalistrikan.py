import urllib
import urllib.request 
import bs4 as bs
import pandas 
import csv
#1
#
soup1 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/ketenaga-listrikan/pltu-mulut-tambang/').read()
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
soup2 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/ketenaga-listrikan/transmisi-sumatera-500-kv/').read()
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
'''
df = pandas.DataFrame(data={"proyek_jalan": mylist, "nilai_investasi": mylist2})
df.to_csv("./file.csv", sep=',',index=False)
'''
#

soup3 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/ketenaga-listrikan/central-west-java-transmission-line-500-kv/').read()
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

#
soup4 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/ketenaga-listrikan/pltu-indramayu/').read()
p_soup4 = bs.BeautifulSoup(soup4,'lxml')
title_4 = p_soup4.findAll('div',class_='container')[3]
get_title_4 = title_4.h1.text
print(get_title_4)
tabel_4 = p_soup4.findAll('table')[0]
get_tbody_4 = tabel_4.findAll('tbody')[0]
get_tr_4 = get_tbody_4.findAll('tr')[1]
get_td_4 = get_tr_4.findAll('td')[2].get_text()
print(get_td_4)

#
soup5 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/ketenaga-listrikan/pltu-batang/').read()
p_soup5 = bs.BeautifulSoup(soup5,'lxml')
title_5 = p_soup5.findAll('div',class_='container')[3]
get_title_5 = title_5.h1.text
print(get_title_5)
tabel_5 = p_soup5.findAll('table')[0]
get_tbody_5 = tabel_5.findAll('tbody')[0]
get_tr_5 = get_tbody_5.findAll('tr')[1]
get_invest5 = get_tr_5.findAll('td')[2].get_text()
print(get_invest5)

mylist.append(get_title_5)
mylist2.append(get_invest5)

#
soup6 = urllib.request.urlopen('https://kppip.go.id/proyek-prioritas/ketenaga-listrikan/energi-asal-sampah-kota-kota-besar-semarang-makassar-tangerang/').read()
p_soup6 = bs.BeautifulSoup(soup6,'lxml')
title_6 = p_soup6.findAll('div',class_='container')[3]
get_title_6 = title_6.h1.text
print(get_title_6)
tabel_6 = p_soup6.findAll('table')[0]
get_tbody_6 = tabel_6.findAll('tbody')[0]
get_tr_6 = get_tbody_6.findAll('tr')[1]
get_invest6 = get_tr_6.findAll('td')[2].get_text()
print(get_invest6)

mylist.append(get_title_6)
mylist2.append(get_invest6)

#

#

df = pandas.DataFrame(data={"nama_proyek": mylist, "nilai_investasi": mylist2})
df.to_csv("ProyekKetenagalistrikan", sep=',',index=False)


#mylist.append(get_invest1)

