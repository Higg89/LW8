import csv

log = open('log.txt', 'w')


def webcc_analis(i):
  name = i[0]
  device_type = i[1]
  browser = i[2]
  sex = i[3]
  age = i[4]
  bill = i[5]
  region = i[6]

  def gender(sex):
    if sex == 'male':
      return 'мужского пола'
    else:
      return 'женского пола'

  def years(age):
    if age.isdigit() == 1:
      age = int(age)
    else:
      age = float(age)
    suffix = 'лет'
    if (age // 10) % 10 != 1:
      if age % 10 == 1:
        suffix = 'год'
      elif age % 10 in (2, 3, 4):
        suffix = 'года'
    return f'{age} {suffix}'

  def gender2(sex):
    if sex == 'male':
      return 'совершил'
    else:
      return 'совершила'

  def device(device_type):
    if device_type == 'mobile':
      return 'с мобильного браузера'
    else:
      return 'с десктопного браузера'

  return (
      f'Пользователь {name} {gender(sex)}, {years(age)} {gender2(sex)} покупку на '
      f'{bill} у.е. {device(device_type)} {browser}. '
      f'Регион, из которого совершалась покупка: {region}.\n')


with open("web_clients_correct.csv", encoding='utf-8') as webcc_file:
  webcc_reader = csv.reader(
      webcc_file,
      delimiter=",")  # Создаем объект reader, указываем символ-разделитель ","
  next(webcc_reader)
  for i in webcc_reader:  # Считывание данных из CSV файла
    log.write(webcc_analis(i))