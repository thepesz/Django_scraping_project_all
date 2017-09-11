import requests
from bs4 import BeautifulSoup
import re
from ilosc.adress_maker import adress_maker
from ilosc.author_finder import author_finder
import pandas as pd
import os, os.path, sqlite3



baza = os.path.join('C:/Users/310041180/statystyka/db.sqlite3')
conn = sqlite3.connect(baza, check_same_thread=False)

def words_counter():
    """
    Function that counts words and saves them into database.
    """
    start_adress = ['https://teonite.com/blog/', 'https://teonite.com/blog/page/2/', 'https://teonite.com/blog/page/3/']
    # Assign a list of each article's url on the blog to the variable.
    urls = adress_maker(start_adress)

    list_of_author = []
    list_of_tuples = []
    list_of_word = []


    for el in urls:

        r = requests.get(el)
        soup = BeautifulSoup(r.content, "lxml")

        #Finding a list of article authors

        author = soup.find('span', {'class': "author-content"})
        author = (author.find('h4')).text.strip()
        author = author.replace(' ', '_')
        if author not in list_of_author:
            list_of_author.append(author)

        #Creating a list of words from each article
        content = str(soup.find_all("section", class_="post-content"))
        content = re.sub(r'<.+?>', '', content)
        content = re.sub(r'[^\w]', ' ', content)
        content = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', content)
        content = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", content).lower()
        list_of_word = content.split()

        # Creating a list of tuples with parameters: word, author
        for word in list_of_word:
            list_of_tuples.append((word, author))
    # Saving to a database using pandas DataFrames. Table names: Stat
    list_word_author = pd.DataFrame(list_of_tuples, columns=['word', 'author'], index=None)
    list_word_author.to_sql('Stat', conn, if_exists='replace', index=False)

    # Downloading the ten most common words from the database (table Stat) and saving into Word_freq table.
    curr = conn.execute("""SELECT word, COUNT(*) FROM Stat GROUP BY word order by count(*) desc LIMIT 10""")
    w = curr.fetchall()
    w2 = pd.DataFrame(w, columns=['word', 'quantity'], index=None)
    w2.to_sql('Word_freq', conn, if_exists='replace', index=False)

    # Downloading the ten most common words of each author from the database (table Stat) and saving to individual tables.
    for index, user in enumerate(list_of_author):
        user_tuple = (user,)
        curr3 = conn.execute(
            """SELECT word, COUNT(*) FROM Stat WHERE author = ? GROUP BY word, author ORDER BY COUNT(*) DESC LIMIT 10""",user_tuple)
        w = curr3.fetchall()
        w2 = pd.DataFrame(w, columns=['word', 'quantity'], index=None)
        name = 'User'+str(index+1)
        w2.to_sql(name, conn, if_exists='replace', index=False)



