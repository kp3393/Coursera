# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}
#x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x

print("Enter a file name:")
try:
    fhandle = open(input())
except:
    print("File not found")
    quit()

#Dictionry declaration
days = dict()

for line in fhandle:
    if line.startswith("From"):
        spline=line.split()
        if len(spline)>3:
            day = spline[2]
            days[day]=days.get(day,0)+1
print(days)
