import pymysql
db = pymysql.connect(host="localhost", user="root", password="", db="stu")
cursor = db.cursor()

# 查看结果集
cursor.execute("select * from stu")
data = cursor.fetchall()
print(data)

# 插入单行数据
sql = "insert into stu values('050101', 'leslie', 81)"
cursor.execute(sql)

# 插入多行数据
sql = "insert into stu values(%s, %s, %s)"
cursor.executemany(sql, [('050102', 'tom', 67), ('050103', 'lucy', 86)])

# 修改记录
sql = "update stu set score = score - 10"
cursor.execute(sql)

# 删除结果集
sql = "delete from stu where id='050103'"
cursor.execute(sql)

# 查看结果集
cursor.execute("select * from stu")
data = cursor.fetchall()
print(data)


db.commit()
cursor.close()
db.close()

