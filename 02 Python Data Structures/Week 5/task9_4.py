# Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dictionary
# has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

print("Enter a file name:")
try:
    fhandle = open(input())
except:
    print("File not found")
    quit()

#Dictionry declaration
mails = dict()

for line in fhandle:
    if line.startswith("From"):
        spline=line.split()
        if len(spline)>3:
            person = spline[1]
            mails[person]=mails.get(person,0)+1

mailnum = None
mailper = None

for k,v in mails.items():
    if mailnum is None or v>mailnum:
        mailnum = v
        mailper = k

print("email address " + mailper + " has sent the maximum number of emails " + str(mailnum))
