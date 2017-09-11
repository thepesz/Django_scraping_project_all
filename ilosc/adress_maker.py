import requests
from bs4 import BeautifulSoup
import re



def adress_maker(start_adress):
    """
    Function that creates the urls of all the articles on the blog
    :param start_adress:
    :return: list_read_more
    """
    list_read_more = []
    for start_url in start_adress:
        r = requests.get(start_url)
        soup = BeautifulSoup(r.content, "lxml")
        read_more_adress = [tag['href'] for tag in
                            soup.find_all('a', {'class': "read-more"})]  # finding href tags with class read-more
        for url in read_more_adress:
            list_read_more.append('https://teonite.com' + url)
    return list_read_more
