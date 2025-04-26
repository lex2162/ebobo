# def sample(name):
#     print(f"Привет, {name}!")
#
# sample("Роберт")  # → Привет, Аня!
# sample("Макс") # → Привет, Макс!
#
# def greet_user(name, age):
#     print(f"Привет, {name}! Тебе {age} лет.")
#     if age < 25:
#         print("Ты пиздюк")
#     if age>= 25:
#         print("Ты подходишь")
# greet_user(name="Стив", age=25)
# greet_user(name="Чипинкос", age=13)
#
#
# for i in range(10):
#     print(i)
#     i = 5
# print(i)
#     # for i in range(4):
#     #     print(i)
#     # else:
#     #     print("Я молодец")


# n = int(input("Введите число: "))
#
# if n < 2:
#     print(f"{n} — не простое число.")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} — не простое число.")
#             break
#     else:
#         print(f"{n} — простое число.")

# print("Простые числа от 1 до 100:")
#
# for n in range(2, 101):  # начинаем с 2, потому что 1 — не простое
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n)

# def find_primes(start, end):
#     print(f"Простые числа от {start} до {end}:")
#
#     for n in range(start, end + 1):
#         if n < 2:
#             continue  # пропускаем 0 и 1
#         for i in range(2, int(n**0.5) + 1):  # делители до корня из n
#             if n % i == 0:
#                 break
#         else:
#             print(n)
# find_primes(1, 100)

import gender_guesser.detector as gender

# Учащиеся по языкам
english_students = {
    "Иван Петров",
    "Alexey",
    "Мария Смирнова",
    "Алексей Иванов",
    "Светлана Орлова"
}

french_students = {
    "Светлана Орлова",
    "Анна Кузнецова",
    "Алексей Иванов",
    "Дмитрий Никифоров"
}

# Инициализируем детектор пола
d = gender.Detector()


# Функция для определения пола по имени
def detect_gender(name):
    first_name = name.split()[0]  # Берем только первое имя
    gender_prediction = d.get_gender(first_name)

    if gender_prediction in ["male", "mostly_male"]:
        return "м"  # Мужской
    elif gender_prediction in ["female", "mostly_female"]:
        return "ж"  # Женский
    else:
        return "неопределённый"  # В случае неопределенности


# Вспомогательная функция для разделения по полу
def split_by_gender(students):
    boys = sorted([s for s in students if detect_gender(s) == "м"])
    girls = sorted([s for s in students if detect_gender(s) == "ж"])
    return boys, girls


# Расчёт групп
both_languages = english_students & french_students
only_one_language = english_students ^ french_students
all_students = english_students | french_students


# 🔽 Функция для красивого вывода с полом
def print_group(title, group):
    print(f"\n{title}:")
    boys, girls = split_by_gender(group)

    print("  👨 Мальчики:")
    for boy in boys:
        print(f"    — {boy}")

    print("  👩 Девочки:")
    for girl in girls:
        print(f"    — {girl}")


# 🔽 Вывод
print_group("Ученики, изучающие только один язык", only_one_language)
print_group("Ученики, изучающие оба языка", both_languages)
print_group("Все ученики в классе", all_students)

