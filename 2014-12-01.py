from collections import Counter
from urllib import request
import re

words = re.findall(r'\w+', request.urlopen('http://www.gutenberg.org/cache/epub/47498/pg47498.txt').read().lower().decode())
print(Counter(words))