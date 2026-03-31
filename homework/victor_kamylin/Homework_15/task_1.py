import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Добавляем студента
add_students = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(add_students, ('Федяйка', 'Карвалолавна'))
student_id = cursor.lastrowid

# Добавляем группу
add_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(add_group, ('Астронавт', '2026.09.03', 'Не известно'))
group_id = cursor.lastrowid

# Добавляем группу в таблицу студенты
updade_stidents = "UPDATE students set group_id = %s where id = %s"
cursor.execute(updade_stidents, (group_id, student_id))

# Добавляем книги
add_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    add_books, [
        ('Как собрать ракету', student_id),
        ('Психология космонавта', student_id)
    ]
)

# Дабывляем предметы
add_subjects = "INSERT INTO subjects (title) VALUES (%s)"
cursor.execute(add_subjects, ('Звездочетство',))
first_subject = cursor.lastrowid

add_subjects = "INSERT INTO subjects (title) VALUES (%s)"
cursor.execute(add_subjects, ('Невесомоведение',))
second_subject = cursor.lastrowid

# Добавляем занятия

lessons = [
    ('Физика', first_subject),
    ('Химия', first_subject),
    ('Физкультура', second_subject),
    ('Акробатика', second_subject)
]

lesson_id = []
for lesson in lessons:
    cursor.execute(
        "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", lesson)
    lesson_id.append(cursor.lastrowid)

# Добавляем оценки
    marks_values = [3, 5, 4, 5]
    for i in range(len(lesson_id)):
        cursor.execute(
            "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
            (marks_values[i], lesson_id[i], student_id)
        )

db.commit()

# Все оценки студента
all_marks = "SELECT `value` FROM marks m where m.student_id = %s"
cursor.execute(all_marks, (student_id,))
marks = cursor.fetchall()
print(marks)

# Все книги, которые находятся у студента
all_books = "SELECT title FROM books b  where b.taken_by_student_id  = %s"
cursor.execute(all_books, (student_id,))
books = cursor.fetchall()
print(books)


# Всё одним запросом с использованием Join
all_requests = '''
SELECT * FROM students s
join books b on s.id = b.taken_by_student_id
join `groups` g on s.group_id = g.id
join marks m on s.id = m.student_id
join lessons l on m.lesson_id = l.id
join subjects s2 on s2.id = l.subject_id
WHERE s.id  = %s
'''
cursor.execute(all_requests, (student_id,))
data = cursor.fetchall()
for i in data:
    print(i)

db.close()
