import string    
import random 
from urllib.parse import urlparse

def getshorterlink(url):
    ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 14))    
    final = url+ran
    return str(final)

def getsitename(url):
    parse_object = urlparse(url)
    return parse_object.netloc

