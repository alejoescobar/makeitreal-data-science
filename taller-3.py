# https://gist.github.com/danielmoralesp/17d4212cdf11184dc4845a252d00f99d

# 1 Average

def average(num1, num2):
  return (num1 + num2)/2

print('Average: ', average(1, 2))

# 2 Exponencial

def tenth_power(num):
  return num ** 10

print('Tenth Power: ', tenth_power(3))

# 3 Bond, James Bond

def introduction(first_name, last_name):
  text = last_name + ', ' + first_name + ' ' + last_name # Es keyword en python?
  return text

print('Introduction: ', introduction('Alejo', 'Escobar'))

# 4 Raíz Cuadrada

def square_root(num):
  return num ** .5

print('Raíz cuadrada: ', square_root(4))

# 5 Propina

def tip(total, percentage):
  return total * (percentage/100)

print('Tip: ', tip(1000, 10))

# 6 Porcentaje de ganancias

def win_percentage(wins, loses):
  total_games = wins + loses
  return str((wins / total_games) * 100) + "%"

print('Porcentaje de ganancias: ', win_percentage(7, 3))

# 7 Primeros tres múltiples

def first_three_multiples(num):
  # multiple = ""
  # for i in range(3):
  #   multiple = (i + 1) * num
  #   print(multiple)
  print(num * 1)
  print(num * 2)
  last_multiple = num * 3
  print(last_multiple)
  return last_multiple

print('Primeros tres múltiples: ', first_three_multiples(7))

# 8 Año Perruno

def dog_years(name, age):
  dog_age = age * 7
  text = name + ", tu tienes " + str(dog_age) + " años en años de perro"
  return text

print('Año Perruno: ', dog_years('Lima', 8))


