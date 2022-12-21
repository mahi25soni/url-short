
from urllib.parse import urlparse
url = 'http://127.0.0.1:8000/showurls/'
parse_object = urlparse(url)
print(parse_object.netloc)