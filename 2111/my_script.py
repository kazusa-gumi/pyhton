f = open("test.csv","w")
f.write("name,department,birthday month.\n")
f.write("John Smith,Accounting,November.\n")
f.write("Erica Meyers,IT,March.\n")
f.write("Vinay Michael,IT,April.\n")
f.write("Max ,IT,March.\n")
f.close()
g = open("test.csv","r")
s = g.read()
g.close()