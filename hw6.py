from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl 

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')



#tags = soup('a')
#for tag in tags:
   # Look at the parts of a tag
   #print('TAG:',tag)
   #print('URL:',tag.get('href', None))
  # print('Contents:',tag.contents[0])
   #print('Attrs:',tag.attrs)

tags = soup('span')
print(tags)

L =[]
for tag in tags:
	L.append(int((tag.contents[0])))
print(sum(L))
