import random

allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@£$%^&*()_+=-{}][:\|';'?><,./~`§±"
repeat = "Y"
while repeat == "Y":
  for y in range(0, 10):
    # Generate a password
    password = ""
    for x in range(0, 12):
      r = random.randint(0, len(allowed_chars) - 1)
      c = allowed_chars[r]
      password = password + c
    print(password)
  repeat = input("Generate 10 more? (Y/N) ")
  repeat = repeat.upper()
print("Have a nice day")
