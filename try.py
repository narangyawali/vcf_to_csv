import os

files = os.listdir()
for f in files:
    if f[-3:] == "vcf":
    	print(f)