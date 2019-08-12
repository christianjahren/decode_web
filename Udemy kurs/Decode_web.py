############# E17 Decode a web page ############
#updated 12.08
from bs4 import BeautifulSoup
import requests
def decode(url):
    # requests the website
    r = requests.get(url)
    # store the text from the website as a variable to make it easier to read
    r_html = r.text

    # run the text through BeautifulSoup with the "html.parser", as well as store this in a variable
    soup = BeautifulSoup(r_html, 'html.parser')

    #
    for item in soup.find_all("h3"):
        print(item.text)
decode("https://www.vg.no/")