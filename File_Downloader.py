import urllib.request

link = input("enter the link of what do you want to download: ")
adres = input("enter the directory to save: ")
isim = input("enter the name to save: ")
kaydet = (adres+"/"+isim)
urllib.request.urlretrieve(link,kaydet)
