#pip install requests
import requests
url = "https://www.allegro.pl/"
r1 = requests.get(url + "archive/v1")
r2 = requests.get(url + "archive/v2")
r3 = requests.get(url + "archive/v3")

#git add .
# git commit -m "lab1"
#git push