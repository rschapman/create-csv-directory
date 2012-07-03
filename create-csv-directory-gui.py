#!/usr/bin/env python
import os
import csv
import easygui

directory = easygui.diropenbox()
write = csv.writer(open("directory.csv","wb"))
itemslist = os.listdir(directory)
for items in itemslist:
	write.writerow([items])
