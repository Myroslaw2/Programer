from num2words import num2words

# Вітання користувача
name = input("Як вас звати? ")
print("Привіт, " + name + "! Ця програма переведе введене вами число в словесне представлення.")

# Запит номера телефону
phone_num = input("Будь ласка, введіть номер телефону: ")
print("Ви ввели номер", phone_num)

# Запит числа, яке потрібно перетворити
num = int(input("Введіть число, яке потрібно перевести в словесне представлення: "))

# Перетворення числа у словесне представлення
num_word = num2words(num, lang='uk')
# Виведення результату
print("Число", num, "у словесному вигляді:", num_word)