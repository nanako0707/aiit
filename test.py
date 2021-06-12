def fb(n):
  if i % 15 == 0:
      print("FizzBuzz")
  elif i % 3 == 0:
      print("Fizz")
  elif i % 5 == 0:
      print("Buzz")

i = 1
while i <= 20:
print(i, fb(i))
i = i + 1