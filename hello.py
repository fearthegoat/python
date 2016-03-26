print("Hello World")

x = list(range(2,21))
evens = [x for x in range(2,21) if x % 2 == 0]
greater_than_8 = [x for x in evens if x >= 8]

def sleep_in(weekday, vacation):

  if not weekday or vacation:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  if a_smile & b_smile:
    return True
  if not a_smile & not b_smile:
    return True
  else:
    return False
