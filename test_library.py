
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLibrarySystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://library-demo.com")

    def test_search_book(self):
        # 搜索《Python编程》
        self.driver.find_element(By.ID, "search_input").send_keys("Python编程")
        self.driver.find_element(By.ID, "search_btn").click()
        results = self.driver.find_elements(By.CLASS_NAME, "book-item")
        self.assertGreater(len(results), 0)

    def test_login_failure(self):
        # 错误密码测试
        self.driver.find_element(By.ID, "username").send_keys("test_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_pass")
        self.driver.find_element(By.ID, "login_btn").click()
        error_msg = self.driver.find_element(By.CLASS_NAME, "error-tips").text
        self.assertIn("密码错误", error_msg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()