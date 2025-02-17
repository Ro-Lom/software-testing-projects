import sqlite3
import unittest
from student_manager import StudentManager


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager(':memory:')  # 使用内存数据库

    def test_add_student(self):
        self.manager.add_student("李四", "软件2班", 92.0)
        # 验证数据库记录数
        self.manager.cursor.execute("SELECT COUNT(*) FROM students")
        count = self.manager.cursor.fetchone()[0]
        self.assertEqual(count, 1)

    def test_invalid_score(self):
        with self.assertRaises(sqlite3.InterfaceError):
            self.manager.add_student("王五", "网络3班", "九十")  # 分数类型错误

    def tearDown(self):
        self.manager.conn.close()


if __name__ == '__main__':
    unittest.main()