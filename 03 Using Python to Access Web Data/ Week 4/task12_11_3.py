# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

import urllib.request, urllib.parse, urllib.error
charcount = 0

print("Enter the url of the webpage: ")
url = input()
fhandle = urllib.request.urlopen(url)
for line in fhandle:
    charcount = charcount + len(line)
    # print(charcount,len(line))
    if charcount < 3000:
        print(line.decode().strip())
    else:
        print(charcount,len(line))
