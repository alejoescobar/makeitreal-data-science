# https://gist.github.com/danielmoralesp/17d4212cdf11184dc4845a252d00f99d

# 1 Average

def average(num1, num2):
  return (num1 + num2)/2

print('Average: ', average(1, 2))

# 2 Exponencial

def tenth_power(num):
  return 10 ** num

print('Tenth Power: ', tenth_power(3))

# 3 Bond

def introduction(first_name, last_name):
  return last_name + ', ' + first_name + ' ' + last_name

print('Introduction: ', introduction('Alejo', 'Escobar'))

# 4 Raíz Cuadrada

def square_root(num):
  return num ** (.5)

print('Raíz cuadrada: ', square_root(4))

# 5 Propina

def tip(total, percentage):
  return total * (percentage/100)

print('Porcentaje de ganancias: ', tip(1000, 10))

# 6 Porcentaje de ganancias

def win_percentage(wins, loses):
  total_games = wins + loses
  return wins / total_games

print('Porcentaje de ganancias: ', win_percentage(7, 3))

# 7 Primeros tres múltiples

def first_three_multiples(num):
  multiple = ""
  for i in range(3):
    multiple = (i + 1) * num
    print(multiple)
  return multiple

print('Primeros tres múltiples: ', first_three_multiples(7))

# 8 Año Perruno

def dog_years(name, age):
  dog_age = age * 7
  return name + ", tu tienes " + str(dog_age) + " años en años de perro"

print('Año Perruno: ', dog_years('Lima', 8))


