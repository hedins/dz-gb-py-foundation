staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee in staff:
    print("Привет, {}!".format(employee.split(" ").pop().capitalize()))
