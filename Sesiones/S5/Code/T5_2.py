from datetime import datetime

def create_random_dates(qty: int) -> list[datetime]:
    from random import randint
    from datetime import timedelta

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    delta = end_date - start_date

    random_dates = []
    for _ in range(qty):
        random_days = randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        random_dates.append(random_date)

    return random_dates

def esta_entre_fechas(inicial: datetime, final: datetime, fecha: datetime) -> bool:
    return inicial <= fecha <= final

fechas_lista = create_random_dates(100)
print(list(map(lambda x: x.strftime("%Y-%m-%d"), fechas_lista)))

fecha_inicial = "2022-01-01"
fecha_final = "2023-08-12"

fecha_inicial_date = datetime.strptime(fecha_inicial, "%Y-%m-%d")
fecha_final_date = datetime.strptime(fecha_final, "%Y-%m-%d")

filtered = filter(lambda x: esta_entre_fechas(fecha_inicial_date, fecha_final_date, x), fechas_lista)
print(list(map(lambda x: x.strftime("%Y-%m-%d"), filtered)))


#
# def inside_bounds(init_date: datetime, end_date: datetime, date: datetime) -> bool:
#     return init_date <= date <= end_date
#
#
#
# fechas = create_random_dates(10)
# print(list(map(lambda x: x.strftime("%Y-%m-%d"), fechas)))
#
# init_date = "2021-01-01"
# end_date = "2028-12-31"
#
# init_date = datetime.strptime(init_date, "%Y-%m-%d")
# end_date = datetime.strptime(end_date, "%Y-%m-%d")
#
# inside_bounds_func = inside_bounds(init_date, end_date, fechas[0])
#
# filtered_dates = filter(lambda x: inside_bounds(init_date, end_date, x), fechas)
#
# print(list(map(lambda x: x.strftime("%Y-%m-%d"), filtered_dates)))
