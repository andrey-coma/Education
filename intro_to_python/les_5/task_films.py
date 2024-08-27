films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон",\
         "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]

res_films = []
k = int(input("Сколько фильмов хотите добавить? "))

while k:
    t = input("Введите название фильма: ")
    if t in films:
        if t not in res_films:
            res_films.append(t)
            k -= 1
        else:
            print(f'{t} Такой фильм уже есть')
    else:
        print(f"Ошибка: фильма {t} у нас нет :( ")

print(res_films)
