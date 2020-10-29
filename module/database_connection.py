import pymysql


def fun_connect():
    mydb = pymysql.connect(host='database.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                           user='root',
                           password='yskumar775',
                           db='sql_flask_excel'
                           )

    return mydb

