from twitter.profile import Profile

show = Profile()
info = show.parse_username('himanshux101')
print(info)

from instagram.profile import Profile
show = Profile()
info = show.parse_username('himanshux1')
print(info)
