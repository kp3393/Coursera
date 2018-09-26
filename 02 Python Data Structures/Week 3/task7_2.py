# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence
#values from these lines. When you reach the end of the file, print out
#the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.

# x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x

#Variable declaration
linerep = 0
floattot = 0

#Prompt user to enter file name. fname is the file handler
print ("Enter the file name: ")
try:
    fname = open(input())
except:
    print('File cannot be opened:',fname)
    exit()

#Search for X-DSPAM-Confidence
for line in fname:
    if line.startswith("X-DSPAM-Confidence:"):
        linerep = linerep + 1
        colon=line.find(":")
        slice = line[colon+1:].rstrip()
        fslice = float(slice)
        floattot=floattot+fslice

print("Average spam confidence:",floattot/linerep)
