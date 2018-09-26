# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

print("Enter a file name:")
try:
    fhandle = open(input())
except:
    print("File does not exists!")
    quit()

mailing_hour = dict()

for line in fhandle:
    if line.startswith("From"):
        sline = line.split()
        if len(sline)> 5:
            time = sline[5]
            colon = time.find(":")
            hour = time[:colon]
            mailing_hour[hour] = mailing_hour.get(hour,0)+1

mailing_hour_ls = list()
for k,v in mailing_hour.items():
    mailing_hour_ls.append((k,v))

mailing_hour_ls = sorted(mailing_hour_ls)

for k,v in mailing_hour_ls:
    print(str(k)+" "+str(v))
