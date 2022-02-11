#this script is for taking some of the files in /Data and turning them into the import-table format. Also helped write the Macro for rolling from the names tables
import csv
from mailbox import linesep
name = "spells"
f = open(name+".txt",'w')
for x in range(10):
    f.write("!import-table --"+name+str(x)+" --hide\n")
    with open("C:\\Users\\Chris\\Downloads\\All 5e spells - Sheet"+str(x+1)+".csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in spamreader:
            f.write("!import-table-item --"+name+str(x)+" --"+row[0]+" --1 --\n")
    
f.close()
fw = open("names.txt","w")
fd = open("dump.txt",'w')
files = ('dragonborn_female','dragonborn_male','dwarf_female','dwarf_male','elf_female','elf_male','halfling_female','halfling_male','halforc_female','halforc_male','human_female','human_male','tiefling_female','tiefling_male')
for y in files:
    f = open("data\\"+y+".txt",'r')
    fw.write("!import-table --"+y+" --hide\n")
    data = f.readlines()
    for line in data:
        fw.write("!import-table-item --"+y+" --"+line[:-1]+" --1 --\n")
    f.close()
    fd.write("{{"+y+"=[[1t["+y+"]]]}}")
fw.close()
fd.close


    