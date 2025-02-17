
import sqlite3


class StudentManager:
    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """创建学生表"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                class TEXT,
                score REAL
            )
        ''')
        self.conn.commit()

    def add_student(self, name, class_name, score):
        """添加学生记录"""
        self.cursor.execute('''
            INSERT INTO students (name, class, score)
            VALUES (?, ?, ?)
        ''', (name, class_name, score))
        self.conn.commit()
        print(f"成功添加学生：{name}")

    # 更多方法：delete_student, update_score, get_statistics...


if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student("张三", "计算机1班", 85.5)