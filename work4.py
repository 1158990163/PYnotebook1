import mysql.connector
import re
import sys


def connMysql():
    mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="552163",  # 数据库密码
        database="first"
    )
    return mydb


def insertsql(filename):
    sql = []
    with open(filename, 'r', encoding="utf-8")as f:
        text = f.read()
        f.close()
    year = re.findall(r'<input type="text" name="year" id="yob" size="4" value="(.*?)">', text)  # 该html的年份
    step1 = re.findall(r'<tr align="right"><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>', text)  # 排名  男名  女名
    for i in step1:
        tempsql = "insert into babynamerank(babyname,onyear,onrank) values ('" + i[1] + "','" + year[0] + "','" + i[
            0] + "')"
        sql.append(tempsql)
    return sql  # 返回插入sql语句集


def main():
    args = sys.argv[1:]

    if not args:
        print(r'usage: [-mo/-my] [-s/-q] [filename]/[name]')
        sys.exit(1)

    if args[0] == '-mo':
        pass
    if args[0] == '-my':
        mydb = connMysql()
        cursor = mydb.cursor()
        if args[1] == '-s':
            sqls = insertsql(args[2])
            for i in sqls:
                cursor.execute(i)
            mydb.commit()

        elif args[1] == '-q':
            print("编号    名字   年号   排名")
            sql = "select id ,babyname , onyear , onrank from babynamerank where babyname = '" + args[2] + "' "
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)


if __name__ == '__main__':
    main()
