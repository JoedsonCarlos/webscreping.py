import requests # requisições http
from bs4 import BeautifulSoup # na requisioes xml e html que vem das pg web

url="https://news.ycombinator.com/"
response=requests.get(url)#requisição para trazer as coisa para pagina

if response.status_code==200:
    soup= BeautifulSoup(response.text,"html.parser")
    heandings=soup.select(".titleline a")
    

    for heanding in heandings:
        print(heanding.text)
        
else:
    print("Failed to load web page")
    
    
