import sqlite3

def init_db():
    # 创建或打开一个数据库文件
    conn = sqlite3.connect('local_database.db')
    
    # 创建一个 cursor 对象来帮助执行 SQL 语句
    cursor = conn.cursor()
    
    # 创建一个新表 'brc-420'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "brc-420" (
            rank INTEGER,
            inscription_id CHAR(66)
        )
    ''')
    
    # 提交事务
    conn.commit()
    
    # 关闭连接
    conn.close()

# 调用初始化函数
if __name__ == '__main__':
    init_db()
