import requests
import search
from search import get_html
from search import _get_name
from search import _get_search_url
from search import _get_link
from search import _get_google_link
from search import _get_description
from search import _get_thumb
from search import _get_cached
from bs4 import BeautifulSoup
from search import *

filePath = "lena.jpg"
searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
#print("fetchUrl", fetchUrl)
html = get_html(fetchUrl)
soup = BeautifulSoup(html, "html.parser")
divs = soup.findAll("div", attrs={"class": "g"})
#results_div = soup.find("div", attrs={"id": "resultStats"})
#number_of_results = _get_number_of_results(results_div)
#elapsed = time()-start
#print(elapsed)
j = 0
void = True
results = []
#void = True
for li in divs:
    res = GoogleResult()

    res.page = 0
    res.index = j

    res.name = _get_name(li)
    res.link = _get_link(li)
    res.google_link = _get_google_link(li)
    res.description = _get_description(li)
    res.thumb = _get_thumb()
    res.cached = _get_cached(li)
    #res.number_of_results = number_of_results

    if void is True:
        if res.description is None:
            continue
    results.append(res)
    j += 1
for resultado in results:
    print(resultado.description)
