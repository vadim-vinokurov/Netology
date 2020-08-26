import psycopg2 as ps
from psycopg2 import sql

def create_db(): # создает таблицы
    with ps.connect(database='s2i', user='s2i', password='1q2w3e', host='pg.codecontrol.ru', port=59432) as con:
        cursor = con.cursor()
        # cursor.execute('''drop table COURSE;''')
        # cursor.execute('''drop table STUDENT;''')
        # cursor.execute('''
        # create table if not exists student(
        #      id serial primary key,
        #      name character varying (100) not null,
        #      gpa numeric (10, 2),
        #      birth timestamp with time zone
        #      );
        # create table if not exists course(
        #      id serial primary key references student(id),
        #      name character varying (100) not null
        #      );''')

        cursor.execute('''insert into student(name) values ('Иван');''')
        cursor.execute('''select id from student;''')
        id =cursor.fetchall()
        print(str(id).strip('[').strip('(').strip(',', ''))
        # cursor.execute('''insert into course values ("{id}",'js');''')
        # cursor.execute('''select * from student''')
        # cursor.execute('''select * from course''')
        # print(cursor.fetchall())



def get_students(course_id): # возвращает студентов определенного курса
    con = ps.connect(database='s2i', user='s2i', password='1q2w3e', host='pg.codecontrol.ru', port=59432)
    cursor = con.cursor()
    # cursor.execute('''select * from student''')
    # # cursor.execute('select * from course where name like {}'.format(course_id,));
    # cursor.fetchall()
    cursor.execute('''select * from STUDENT''')
    print(cursor.fetchall())
#
#

def add_students(course_id, students): # создает студентов и записывает их на курс
    with ps.connect(database='s2i', user='s2i', password='1q2w3e', host='pg.codecontrol.ru', port=59432) as con:
        cursor = con.cursor()
        cursor.execute("""INSERT INTO course(name) values (%s);INSERT INTO student(name) values (%s)""",
                       (course_id, students))
        cursor.execute('''select * from STUDENT''')
        print(cursor.fetchall())


#
#
# def add_student(name, age, course): # просто создает студента
#     with ps.connect(database='s2i', user='s2i', password='1q2w3e', host='pg.codecontrol.ru', port=59432) as con:
#         cursor = con.cursor()
#         cursor.execute("""select course_id from ids where COURSE_DICT like '{}';""".format(course))
#         course_id = cursor.fetchall()
#         for i in course_id:
#             cursor.execute("""
#                     INSERT INTO student(name, age, course_id) values (%s, %s, %s);
#                     """.format(course_id), (name, age, i[0]))
#     #
    #     cursor.execute("""select course_id from student""")
    #     cursor.fetchall()
#
#
# def get_student(student_id):
#     with ps.connect(database='s2i', user='s2i', password='1q2w3e', host='pg.codecontrol.ru', port=59432) as con:
#         cursor = con.cursor()
#         cursor.execute("""select student_id from student where name like '{}';""".format(student_id))
#         cursor.fetchall()
#
# def add_course():
#     with ps.connect(database='s2i', user='s2i', password='1q2w3e', host='pg.codecontrol.ru', port=59432) as con:
#         cursor = con.cursor()
#         cursor.execute("""select * from student""")
#         return cursor.fetchall()



if __name__ == '__main__':
    # add_students(course_id=input("Введите название курса: "), students=input('Введите Имя: '))
    # get_students(course_id=input('Введите название курса: '))

    # print(add_course())
    # print(get_students(1))
    create_db()