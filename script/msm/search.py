
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class WebTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(login):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        login.driver = webdriver.Chrome(options=options)
        # login.driver = webdriver.Chrome()  # หรือใช้ webdriver.Firefox(), webdriver.Edge(), etc.
        login.driver.get('https://msm-smarty-cms-staging.hr-impact.co/login')
        login.driver.set_window_size(1600, 1000)
        login.driver.implicitly_wait(10)

    def test_page_title(self):
        driver = self.driver
        self.assertEqual(driver.title, 'Smarty msm | Management units')  # ตรวจสอบว่า title ของหน้าเว็บถูกต้อง

    def test_Login_Smarty(self):
        time.sleep(1)
        driver = self.driver
        
        try:
            search_box = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/input')
            search_box.send_keys('00000')
            Click = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')  # ขอ OTP
            assert search_box.is_displayed() and search_box.is_enabled(), 'Element is not displayed or not enabled!'
            Click.click()  # คลิกขอ OTP

    # รอให้ Element คลิกได้  # คลิกขอ เข้าสู่ระบบ
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert element.is_displayed() and element.is_enabled(), 'Element is not displayed or not enabled!'
            element.click()
        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))

        try:
# ทดสอบการคลิก Element
            result_element = self.driver.find_element(By.XPATH, '/html/body/div/div/main/nav/div/div/div/ul/div[3]/li/div/div[2]')    
            self.assertIsNotNone(result_element)
        except NoSuchElementException as e:
            print(f'Element Not Found :{e}')
            pass

    def test_function(self):
        # หน้า จัดการลูกหนี้
        self.driver.get('https://msm-smarty-cms-staging.hr-impact.co/management/units')
        time.sleep(1)

        try:
            try:
                # คีย์ โครงการ
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/div/input'))
                )
                assert element.is_displayed(), 'element is not dispalyed!'
                assert element.is_enabled(), 'Element is not selected!'
                element.send_keys('อาคาร A1' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.5)            
            except AssertionError as e:
                self.fail(''+ str(e))
                # print(f'Element not Found : {e}')
                
            
            try:
            # คีย์ ชั้น / ห้อง
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
                )
                assert element.is_displayed(), 'element is not dispalyed!'
                assert element.is_enabled(), 'Element is not selected!'
                element.send_keys('01/01' + Keys.ARROW_DOWN + Keys.ENTER)
                time.sleep(0.5)
            except AssertionError as e:
                self.fail('Element not Found'+ str(e))
            
            try:
            # ประเภทs
                self.search_box = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div/div/div')
                assert element.is_displayed(), 'element is not dispalyed!'
                assert element.is_enabled(), 'Element is not selected!'
                self.search_box.click()
                time.sleep(0.1)
                self.search_box = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')
                assert element.is_displayed(), 'element is not dispalyed!'
                assert element.is_enabled(), 'Element is not selected!'
                self.search_box.click()
                time.sleep(0.1)
            except AssertionError as e:
                self.fail('Element not Found'+ str(e))

            try:
            # ค้นหาชื่อ
                self.Key_Text = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/input')
                assert element.is_displayed(), 'element is not dispalyed!'
                assert element.is_enabled(), 'Element is not selected!'
                self.Key_Text.send_keys('นางอำไพ นิมานะ')
                assert 'ค้นหา' in self.driver.find_element(By.XPATH, '//div/div/div/div[1]/div[3]/div[2]/div/div[1]/p').text
                time.sleep(0.3)
            except AssertionError as e:
                self.fail('Element not Found'+ str(e))
            time.sleep(0.1)
            # รอให้ Element ปรากฏ โดยกำหนดเวลาเป็น 10 วินาที
            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div"))  # เปลี่ยนเป็นตัวระบุตำแหน่งของคุณ
            )
            # หลังจาก Element ปรากฏ สามารถทำการขั้นตอนถัดไปได้
            print("Element is visible. Proceeding with the next step.")
            time.sleep(0.1)
            
            try:
            # Refresh
                self.Refresh = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div/div[1]/div[3]/button')
                assert element.is_displayed(), 'element is not dispalyed!'
                assert element.is_enabled(), 'Element is not selected!'
                self.Refresh.click()
                time.sleep(0.5)
            except AssertionError as e:
                self.fail('Element not Found'+ str(e))
                
        except TimeoutException as e : 
            self.fail(f"เกิดข้อผิดพลาดในการโหลดหน้า : {e}")

            

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # print('___Test Pass__')
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Dit54\\Desktop\\Smarty\\6.การบริหาร\\Reports'))



