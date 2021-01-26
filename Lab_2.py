# Функція відбору унікальних слів та сортування їх в алфавітному порядку
def unique(text):
    text_lower = text.lower().split() # Розбиваємо рядок на частини, використовуючи спеціальний роздільник, і повертаємо ці частини у вигляді списку
    result=" ".join(sorted(sorted(set(text_lower), key=text_lower.index))) # Відбираємо унікальні слова за індексом слова, сортуємо ці слова за алфавітом і формуємо новий рядок з цих слів
    return result

# Функція підрахунку літер в тексті
def countItems(text):
  from collections import Counter # Використовуємо модуль collections Counter
  return sorted(Counter(text).items()) # Підраховуємо символи і сортуємо у алфавітному порядку

print('Введіть "а" - видалити дуюлюючі слова або "б" - порахувати кількість кожного символа у введено тексті: ')
choice=input()
print("Введіть текст: ")
text=input() # Присвоюємо змінній text значення введеного тексту
if(choice=="a"): # Якшо ввели "а" запускаємо функцію unique
    print(unique(text))
if(choice=="b"): # Якшо ввели "b" виводимо список символів у тексті і їх кількість використовуючи фукнцію countItems
    for letter, count in countItems(text):
        print ('{letter}: {count}'.format(letter=letter, count=count)) # Виводимос отриманий список в зручному для читання форматі


