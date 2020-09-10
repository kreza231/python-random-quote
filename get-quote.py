import random

def maaain():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1 #13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  maaain()
