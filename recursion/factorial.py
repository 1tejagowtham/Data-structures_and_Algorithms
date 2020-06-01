def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)

print(factorial(1256))

# This gets a stack_over_flow