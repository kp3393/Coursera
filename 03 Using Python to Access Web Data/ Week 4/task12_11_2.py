# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire document
# and count the total number of characters and display the count
# of the number of characters at the end of the document.

import socket

print("Enter the url of the webpage: ")
url = input()
surl = url.split('/')
host = surl[2]
charcount = 0

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    website = 'GET '+url+' HTTP/1.0\r\n\r\n'
    cmd = website.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(3000)
        if len(data) < 1:
            break
        charcount = charcount + len(data)
        if charcount < 3000:
            print(data.decode())
            print(charcount)
        print(charcount)
    mysock.close()

except:
    print("Invalid website. Please check again!")
