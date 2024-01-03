import datetime
def reg(name, surname, patronymic, age):
    year = datetime.datetime.now().year
    birth = year - int(age)
    ans = f'{name} {surname} {patronymic} {birth} г.р. зарегистрирован'
    return (ans)