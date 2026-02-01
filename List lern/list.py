

students = ['Семен', 'Виталий', 'Илья', 'Артем', 'Михаил']

def student_list(list):
    for name in list:
        print(name)
    print('------------конец списка-----------')



# список студентов
student_list(students)
# третий студент
print(students[2])
# последний студент из списка
print(students[-1])
# Добавляем Свету в список студентов
students.append('Света')
# вызываем фунцию что бы напечтать список с новым студентом 
student_list(students)
# добавляпем студента на вторую позицию
students.insert(1, 'Дрон')
# вызываем фунцию что бы напечтать список с новым студентом 
student_list(students)
# удаление первого студента из списка
delited = students.pop(0)
# вызываем фунцию что бы напечтать список с новым студентом 
student_list(students)
# новый список со 2 по 4 
new_student = students[1:3]
# вызываем фунцию что бы напечтать список с новым студентом 
student_list(new_student)
# сортируем по убыванию
new_student.sort(reverse=True)
# вызываем фунцию что бы напечтать список с новым студентом 
student_list(new_student)
# сорировка студентов по алфавиту
sorted_rus = sorted(students)
# вызываем фунцию что бы напечтать список с новым студентом 
student_list(sorted_rus)
print(len(sorted_rus))

