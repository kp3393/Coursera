# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

print("Enter a file name:")
try:
    fhandle = open(input())
except:
    print("File not found")
    quit()

#Dictionry declaration
addresses = dict()

for line in fhandle:
    if line.startswith("From"):
        spline=line.split()
        if len(spline)>3:
            person = spline[1]
            sperson = str(person)
            atrate = sperson.find("@")
            slperson = sperson[atrate+1:]
            addresses[slperson]=addresses.get(slperson,0)+1

print(addresses)
