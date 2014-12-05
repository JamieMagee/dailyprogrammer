from urllib import request

words = set(str.splitlines(request.urlopen('http://www.joereynoldsaudio.com/enable1.txt').read().decode()))


def score(w):
    return sum(w[i:j] in words for i in range(len(w) - 1) for j in range(i + 2, len(w) + 1))


print(max(words, key=score))