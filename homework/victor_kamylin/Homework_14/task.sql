-- Добавляем студента
INSERT INTO students (name, second_name, group_id) 
VALUES ('Mikhas', 'Barabanov')

-- Добавляем группу
INSERT INTO `groups` (title, start_date, end_date) 
VALUES ('Астроном', '2026.09.03', 'Не определенно')

UPDATE students set group_id = 22105 where id = 22422

-- Добавляем книги
INSERT INTO books (title, taken_by_student_id)
SELECT 'Как собрать телескоп', id
FROM students s
WHERE s.id  = 22422

-- Дабывляем предметы
INSERT INTO subjects (title)
VALUES 
('Физика черных дыр'),
('Звездочетство'),
('Биология инопланетян');


-- Добавляем занятия 
INSERT INTO lessons (title, subject_id)
VALUES 
('Квантовая физика', 14108),
('Физика антиматерии', 14108),
('Ночное небо', 14109),
('Небесные тела', 14109),
('Космическая фауна', 14110),
('Космическая флора', 14110);


-- Оценки
INSERT INTO marks (value, lesson_id, student_id)
VALUES 
('3', 75341, 22422),
('5', 75342, 22422),
('4', 75343, 22422),
('5', 75344, 22422),
('4', 75345, 22422),
('5', 75346, 22422);

-- Все оценки студента
SELECT `value` FROM marks m where m.student_id = 22422

-- Все книги, которые находятся у студента
SELECT title FROM books b  where b.taken_by_student_id  = 22422

-- Всё одним запросом с использованием Join
SELECT * FROM students s 
join books b on s.id = b.taken_by_student_id 
join `groups` g on s.group_id = g.id 
join marks m on s.id = m.student_id 
join lessons l on m.lesson_id = l.id
join subjects s2 on s2.id = l.subject_id 
WHERE s.id  = 22422