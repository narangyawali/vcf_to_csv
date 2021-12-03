import os

def writeCSV(singleContact):
    copiedContacts = open('contacts.csv', "a")
    index = 0
    for line in singleContact:
        index += 1
        #print("not this one")
        if index == 3:
            nam = line[3:-4]
            # print(nam)
            #print(f"{index}  => {line}")
        elif index == 4:
            # print(line)
            print(nam)
            tel = line[15:-1]
            print(tel)
            copiedContacts.writelines(f"\"{nam}\",\"{tel}\"\n")
    copiedContacts.close()



files = os.listdir()
for singleFile in files:
    if singleFile[-3:] == "vcf":
    	file = open(singleFile, "r")
        writeCSV(file)

