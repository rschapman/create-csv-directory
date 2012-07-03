#!/usr/bin/env python
import os
import csv
write = csv.writer(open("directory.csv","wb"))
itemslist = os.listdir(os.getcwd())
for items in itemslist:
	write.writerow([items])
