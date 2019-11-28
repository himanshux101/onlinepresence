# Online Presence 

There is no tool that gives you the digital footprint of a user under a single API. The social media company doesn't even provide all the info under their API's. This tool does it's best to solve this problem by giving you the online presence of a user. 

## Requirements 

- requests 
- Beautifulsoup4

## Usage 

see test.py for examples 

#### Twitter
```
from twitter.profile import Profile

show = Profile()
# returns dict 
info = show.parse_username('himanshux101')
```

#### Instagram
```
from instagram.profile import Profile

show = Profile()
info = show.parse_username('himanshux1')
print(info)
```

## ToDo

- add google page search crawler 

## Contribute to Online Presence 

1. fork this repo 
2. create a pull request 

## Contact 

if you have any questions. contact me at himanshux101@gmail.com

## Licence 

This project uses the MIT Licence. 

