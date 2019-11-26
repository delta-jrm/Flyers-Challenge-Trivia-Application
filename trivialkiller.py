import sys
import requests
import bs4
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Trivial Killer V1.0")
print(ascii_banner)

res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))

res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text,"lxml")
elems = wiki.select('p')
for i in range(len(elems)):
    print(elems[i].getText())