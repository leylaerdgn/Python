#5'ten geriye doğru sayan basit bir özyinelemeli fonksiyon:
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)
#countdown(5)

#Faktöriyel
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))