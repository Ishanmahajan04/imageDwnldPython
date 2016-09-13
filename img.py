import random
import urllib.request

def img_dwnld(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)


img_dwnld("http://consultadd.com/wp-content/uploads/Final_logo.png")