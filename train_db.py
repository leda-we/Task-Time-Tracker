import sqlite3
import random
import re
import string
# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def generate_random_word(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))



for i in range(50):
    word = generate_random_word()
    age_random = random.randint(10,100)
    cursor.execute('INSERT INTO Users (username, email, age) VALUES(?, ?, ?)', (word, word + '@gmail.com', age_random))
# # cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
# results = cursor.fetchall()

# for row in results:
#     print(row)

# cursor.execute('DELETE FROM Users WHERE id > ?', (0,))

# cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
# filtered_results = cursor.fetchall()
# for row in filtered_results:
#     print(row)
# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()