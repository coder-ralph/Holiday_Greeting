# Python Philippines - Python Coding Challenge
import random
# holiday greetings
def holiday_greeting(name, holiday):
  greetings = ["Merry", "Happy", "Joyous", "Cheerful", "Festive"]
  feelings = ["love", "joy", "peace", "happiness", "warmth"]
  actions = ["spreading", "sharing", "bringing", "sending"]

  greeting = random.choice(greetings) + " " + holiday + ","
  feeling = "filled with " + random.choice(feelings) + ","
  action = "and " + random.choice(actions) + " " + random.choice(feelings) + " to all!"

  return greeting + " " + name + "! We hope your holiday is " + feeling + " " + action

print(holiday_greeting("PythonPH Fam", "Holidays"))
print(holiday_greeting("PythonPH Fam", "Christmas"))
print(holiday_greeting("PythonPH Fam", "Hanukkah"))
print(holiday_greeting("PythonPH Fam", "Kwanzaa"))
