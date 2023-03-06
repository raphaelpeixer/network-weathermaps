#!/usr/bin/env python
import os

files = []

ls = os.listdir("/var/www/html/Weathermap/configs/")

contador = 0
while contador < len(ls):
    if ls[contador][-5:] != ".conf" or ls[contador] == "simple.conf":
        ls.pop(contador)
    else:
        files.append(ls[contador][:-5])
        contador+=1

for each in range(len(files)):
    os.system("cd /var/www/html/Weathermap && php weathermap --config configs/%s.conf --output %s.png --htmloutput output/%s.html --no-warn WMRRD02" % (files[each],files[each],files[each]))
    os.system("cd /var/www/html/Weathermap && mv %s.png output/" % (files[each]))
