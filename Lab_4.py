import os

while True:
    # Запит шляху до файлу від користувача
    file_path = input("Введіть шлях до файлу: ")

    # Перевірка чи файл існує
    if not os.path.exists(file_path):
        print("Файл не знайдено.")
        continue

    # Ініціалізація змінних для статистики
    lines_count = 0
    empty_lines_count = 0
    z_lines_count = 0
    z_count = 0
    and_lines_count = 0

    # Читання файлу по рядках
    with open(file_path, 'r') as f:
        for line in f:
            lines_count += 1

            # Перевірка на порожній рядок
            if line.strip() == '':
                empty_lines_count += 1

            # Перевірка на наявність літери "z" у рядку
            if 'z' in line:
                z_lines_count += 1

            # Підрахунок кількості літер "z" у файлі
            z_count += line.count('z')

            # Перевірка на наявність групи символів "and" у рядку
            if 'and' in line:
                and_lines_count += 1

    # Виведення статистики
    print(f"Кількість рядків: {lines_count}")
    print(f"Кількість порожніх рядків: {empty_lines_count}")
    print(f"Кількість рядків з літерою 'z': {z_lines_count}")
    print(f"Кількість літер 'z' у файлі: {z_count}")
    print(f"Кількість рядків з групою символів 'and': {and_lines_count}")

    # Запит на аналіз іншого файлу
    another_file = input("Аналізувати ще один файл? (так/ні): ")
    if another_file.lower() != 'так':
        break
