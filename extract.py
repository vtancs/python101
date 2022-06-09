# Extraction script
from bs4 import BeautifulSoup
import requests

#-------------------------------------------------------------------------------
url = "https://commodore.bombjack.org/apple/apple-books.htm"

print("URL: " + url)
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

total = 0
# open a (new) file to write
outF = open("get.bat", "w")
ok = False

#print("The href links are :")
for link in soup.find_all('a'):
    string = link.get('href')
    try:
        if "http" in string:
            ok = True
        if string[0] == '/':
            string = "https://commodore.bombjack.org" + string
            ok = True
    except:
        print("Error ", string)

    if ok == True:
        print(str(total) + "\t" + string)
        try:
            total += 1
            outF.write("wget --no-check-certificate " + "\"" + string + "\"")
            outF.write("\n")
        except:
            print("Error with: " + string)
    ok = False

print("Extracted total # " + str(total))
print("End.")
