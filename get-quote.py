import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print(quotes[rnd], end = ' ')

  rnd = random.randint(0, last)
  print(quotes[rnd])

  f = open("quotes.txt", "a")
  quo = input("\nEnter Any Quote: ")
  f.write(quo)
  f.close()

if __name__== "__main__":
  primary()
