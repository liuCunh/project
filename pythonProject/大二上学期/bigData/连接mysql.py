import pymysql


def look():
    sql = "select * from student"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)


db = pymysql.connect(host="localhost", user="root", password="", db="school")
cursor = db.cursor()
look()

# 添加一条记录
sql = "insert into student values('006', 'tom', 'male', 59)"
cursor.execute(sql)
look()

# 插入多条
sql = "insert into student values(%s, %s, %s, %s)"
cursor.executemany(sql, [('007', 'Jerry', 'male', 85), ('008', 'Lucy', 'female', 59)])
look()

# 成绩减少5
sql = 'update student set score = score-5'
cursor.execute(sql)
look()

# 删除70以下
sql = "delete from student where score<70"
cursor.execute(sql)
look()

# 删除85以上
sql = "delete from student where score>85"
cursor.execute(sql)
look()
