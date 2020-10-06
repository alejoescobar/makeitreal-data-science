# https://gist.github.com/danielmoralesp/adbc46bef5120bb8072c0222050e800a

# 1. In Range
def in_range(num, lower, upper):
  return num >= lower and num <= upper

print("In Range:", in_range(10, 5, 20))

# 2. Move Review
def movie_review(rating):
  if rating >= 9:
    return "Outstanding"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  elif rating <= 5:
    return "Avoid at all costs!"

print("Movie Review:", movie_review(3))

# 3. Twice as large
def twice_as_large(num1, num2):
  double_num2 = num2 * 2
  return num1 > double_num2

print("Twice as large:", twice_as_large(5, 2))

# 4. Power
def large_power(base, exponent):
  result = base ** exponent
  return result > 5000

print("Power:", large_power(10, 20))

# 5. Divisible por 10
def divisible_by_ten(num):
  return num % 10 == 0

print("Divisible por 10:", divisible_by_ten(10))

# 6. Número Máximo
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else
    return "es un empate!"

print("Número máximo:", max_num(2, 1, 1))

# 7. Over Budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  total = food_bill + electricity_bill + internet_bill + rent
  return budget < total

print("Over Budget:", over_budget(10, 1, 1, 1, 1))
