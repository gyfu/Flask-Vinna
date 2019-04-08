#Höfundur: Huginn Þór Jóhannsson
import sqlite3
conn=sqlite3.connect("database.db")
c=conn.cursor()
c.execute('''CREATE TABLE if not exists users(
        user varchar(32) NOT NULL,
        pass varchar(32) NOT NULL,
        nafn varchar(32) NOT NULL
        );
        '''
        )
c.execute('''INSERT or ignore INTO users(
    user,
    pass,
    nafn
    )
    VALUES
    (
    "admin",
    "password",
    "huginn"
    );
        ''')
c.execute('''SELECT * FROM users
''')
print(c.fetchone())
conn.commit()
conn.close()
