# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number
# of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

print("Enter a file name:")
try:
    fhandle = open(input())
except:
    print("File does not exists!")
    quit()

mail = dict()

for line in fhandle:
    if line.startswith("From"):
        sline = line.split()
        if len(sline)> 5:
            mailadd = sline[1]
            mail[mailadd] = mail.get(mailadd,0)+1

maillist = list()
for k,v in mail.items():
    maillist.append((v,k))

maillist = sorted(maillist, reverse = True)

for k,v in maillist[:1]:
    print(v,k)
