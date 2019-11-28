import requests
from bs4 import BeautifulSoup

class Profile:
    def __init__(self):
        pass 

    def _request_url(self, username):
        url = 'https://www.instagram.com/{}'.format(username)
        res = requests.get(url)
        if res.status_code != 200:
            return None
        else:
            return res
    
    def _parse(self, res):
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'})
        text = data[0].get('content').split()
        self.followers = text[0]
        self.following = text[2]
        self.posts = text[4]

    def parse_username(self, username):
        res = self._request_url(username)
        if res is None:
            return

        self._parse(res)
        return self.__dict__
