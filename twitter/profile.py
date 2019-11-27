import re
import requests
from bs4 import BeautifulSoup


class Profile:
    """
    Parse twitter profile

    returns:
        name
        username
        bio
        website
        date_joined
        birthdate
        tweets_count
        following_count
        followers_count
        likes_count
    """

    def __init__(self):
        pass

    def _parse(self, res):
        if res is None:
            return

        soup = BeautifulSoup(res.content, 'html.parser')

        # side bar section
        name = soup.select('.ProfileHeaderCard h1.ProfileHeaderCard-name a.ProfileHeaderCard-nameLink')
        self.name = name[0].get_text()

        username = soup.select('.ProfileHeaderCard h2.ProfileHeaderCard-screenname')
        self.username = ''.join(username[0].get_text().split())

        bio = soup.select('.ProfileHeaderCard p.ProfileHeaderCard-bio')
        self.bio = bio[0].get_text()

        location = soup.select('.ProfileHeaderCard div.ProfileHeaderCard-location span.ProfileHeaderCard-locationText')
        self.location = ''.join(location[0].get_text().split())

        website = soup.select('.ProfileHeaderCard div.ProfileHeaderCard-url span.ProfileHeaderCard-urlText')
        self.website = ''.join(website[0].get_text().split())

        date_joined = soup.select('.ProfileHeaderCard div.ProfileHeaderCard-joinDate span.ProfileHeaderCard-joinDateText')
        self.date_joined = date_joined[0].get_text()

        birthdate = soup.select('.ProfileHeaderCard div.ProfileHeaderCard-birthdate span.ProfileHeaderCard-birthdateText')
        self.birthdate = birthdate[0].get_text()
        if self.birthdate == '\n':
            self.birthdate = None

        # number of tweets
        tweets_count = soup.select('.ProfileNav-list .ProfileNav-item--tweets .ProfileNav-value')[0].get_text()
        # tweets_count = tweets_count[0].get_text()
        self.tweets_count = re.search(r'\d+', tweets_count).group()

        # number of followers
        following_count = soup.select('.ProfileNav-list .ProfileNav-item--following .ProfileNav-value') 
        self.following_count = following_count[0].get_text()

        # number of followers
        followers_count = soup.select('.ProfileNav-list .ProfileNav-item--followers .ProfileNav-value')
        self.followers_count = followers_count[0].get_text()

        # number of likes
        likes_count = soup.select('.ProfileNav-list .ProfileNav-item--favorites .ProfileNav-value')
        self.likes_count = likes_count[0].get_text()

    def parse_username(self, username):
        link = 'https://www.twitter.com/{}'.format(username)
        res = requests.get(link)

        if res.status_code != 200:
            print('wrong username')
            res = None
            return None

        self._parse(res)

        return self.__dict__
