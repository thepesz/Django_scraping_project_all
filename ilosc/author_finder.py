from ilosc.adress_maker import adress_maker
import requests
from bs4 import BeautifulSoup
import requests



list_of_author = []


def author_finder(adress_urls):
    """
    Function that finds authors for each article on the blog
    :param adress_urls:
    :return list_of_author:
    """
    for adress in adress_urls:
        r = requests.get(adress)
        soup = BeautifulSoup(r.content, "lxml")
        author = soup.find('span', {'class': "author-content"})
        author = (author.find('h4')).text.strip()
        author = author.replace(' ', '_')
        if author not in list_of_author:
            list_of_author.append(author)

    return(list_of_author)