def person_input(name, surname, years_old, city_live, email, number):
   """ Вывод данных о пользователе одной строкой

   Именованные параметры:
   name, surname, years_old, city_live, email, number

   """

   return ', '.join([name, surname, years_old, city_live, email, number])
name_1 = input('Введите имя: ')


print(person_input(name=name_1, years_old='1991', surname='Mik', city_live='town', email='2x2@gmail.com', number='8-925-445-78-78'))
