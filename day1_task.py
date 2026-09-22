# Write a Python script that:
# Loops through numbers 1 to 30
# For multiples of 3, print "Fizz"
# For multiples of 5, print "Buzz"
# For multiples of both 3 and 5, print "FizzBoom"
# Otherwise, print the number itself

num = 0
while num < 30:
  num += 1  
  if num % 3 == 0 and num % 5 == 0:
    print ("FizzBoom")

  elif num % 5 == 0:
    print ("Buzz")

  elif num % 3 == 0:
    print ("Fizz")

  else:
    print (num)