from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


class WebTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(login):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        login.driver = webdriver.Chrome(options=options)
        login.driver.get('https://backoffice-staging.hr-impact.co/login')
        login.driver.set_window_size(1600, 1000)
        login.driver.implicitly_wait(15)

    def test_page_title(self):
        driver = self.driver
        self.assertEqual(driver.title, 'Admin Events Management')  # ตรวจสอบว่า title ของหน้าว็บถูกต้อง
        
    def test_login_impact(self):
        result = None
        time.sleep(1)
        driver = self.driver

        try:
        # ป้อนรหัสผ่าน
            Check_messages = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[1]/p')
            expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
            assert Check_messages.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{Check_messages.text}'"
            time.sleep(0.1)
        
            Key_Passwprd = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
            Key_Passwprd.send_keys('0800000000')

            input_password = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
            input_value = input_password.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

            textbox_element = driver.find_element(By.XPATH, "//div/div/div[2]/div[1]/div/div[2]/div/div/input")  
            textbox_value = textbox_element.get_attribute("value")
            text_to_check = "0800000000"
            assert text_to_check in textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ"
        
            Click_Otp = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/button')
            assert Click_Otp.is_displayed(), 'Element is not displayed!'
            assert Click_Otp.is_enabled(), 'Element is not enabled!'
            Click_Otp.click() 
            if Click_Otp:
                print('กดคลิกขอ Otp สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Otp ไม่สำเร็จ : Fail')

            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div[2]/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert element.is_displayed(), 'Element is not displayed!'
            assert element.is_enabled(), 'Element is not enabled!'
            element.click()
            if element:
                print('กดคลิกเข้าสู่ระบบสำเร็จ : Pass')
            else:
                print('กดคลิกขอเข้าสูาระบบไม่สำเร็จ : Fail')


        # จับข้อผิดพลาดนี้เมื่อไม่พบองค์ประกอบ และเรียกใช้ self.fail() เพื่อบอกว่าการทดสอบล้มเหลว
        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')
        
        try:
        # ทดสอบการคลิก Element
            result_elemet = self.driver.find_element(By.XPATH, '//div[1]/div/main/div/div/div[1]/button')    
            self.assertIsNotNone(result_elemet)
        except NoSuchElementException as e:
            self.fail('Element not Found')
            self.driver.implicitly_wait(10)
        return result

    def test_page_evement(self):
        
        self.driver.get('https://backoffice-staging.hr-impact.co/events')
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

        result = None
        try: 

            Url =  self.driver.current_url == 'https://backoffice-staging.hr-impact.co/events'
            if Url:
                print('URL Show on page : Pass')
            else:
                print('URL is not Show on page! : Fail')

            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="MuiContainer-root MuiContainer-maxWidthLg mui-style-5gxgaq"]/div[1]/div[1]//button'))
            )
            print('รอปุ่ม Add Event จนปรากฏขึ้น')

            Add_Event = self.driver.find_element(By.XPATH, '//div[@class="MuiContainer-root MuiContainer-maxWidthLg mui-style-5gxgaq"]/div[1]/div[1]//button')
            assert Add_Event.is_displayed(), 'Element is not displayed!'
            assert Add_Event.is_enabled(), 'Element is not enabled!'
            Add_Event.click()
            if Add_Event:
                print('กดคลิก Add Event สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Add Event ไม่สำเร็จ : Fail')


            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, 'name'))
            )
            print('รอจนสามารถกรอกข้อมความได้')

            pyautogui.click(x=743, y=445)
            time.sleep(0.5)
            pyautogui.click(x=484, y=528)
            time.sleep(0.5)
            pyautogui.click(x=629, y=411)
            pyautogui.press('enter')
            
            # current_position = pyautogui.position()
            # print(f"The current mouse position is: {current_position}")


            Key_Name_Event = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[2]/div/div[2]/div/div/input')
            Key_Name_Event.send_keys('Test')

            input_key = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[2]/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')        

            wait_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[3]/div/div/div/div/div/div[1]/div/div/div'))
            )
            print('key_Type_for_something')

            click_type = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[3]/div/div/div/div/div/div[1]/div/div/div')
            click_type.click() 

            key_Type_for_something = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[3]/div/div/div/div/div/div[1]/div/div/div')
            key_Type_for_something.send_keys(
            'ระบุทรัพยากรเป้าหมายของคำขอเมื่อรวมกับข้อมูลที่ให้ไว้ในHostส่วนหัว นี่คือเส้นทางสัมบูรณ์ (เช่น/path/to/file.html) ในคำขอไปยังเซิร์ฟเวอร์ต้นทาง และ URL สัมบูรณ์ในคำขอไปยังพร็อกซี')

            element_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
            time.sleep(1)

            key_location = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input')
            key_location.send_keys('Impact')

            input_key = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}') 

            key_Specify_quantity = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[2]/div/div[2]/div/div/input')
            key_Specify_quantity.send_keys('90')

            input_key = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[2]/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}') 

            try:
                start_date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[5]/div[1]/div/div/div/div/button')
                assert start_date.is_displayed(), 'Element is not displayed!'
                assert start_date.is_enabled(), 'Element is not enabled!'
                start_date.click()

                date_28 = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[4]/button[7]')
                assert start_date.is_displayed(), 'Element is not displayed!'
                assert start_date.is_enabled(), 'Element is not enabled!'
                date_28.click()  

                # autogui เลือกเวลา วันที่เริ่ม
                pyautogui.moveTo(x=637, y=335) 
                pyautogui.scroll(-15)
                time.sleep(0.5)
                pyautogui.click(x=637, y=335)
                pyautogui.click(x=701, y=338)

                if start_date:
                    print('คลิกเลือกวันที่เริ่มต้นสำเร็จ : Pass')
                    if date_28:
                        print('คลิกเลือกวันที่ 28 สำเร็จ : Pass')
                    else:
                        print('คลิกเลือกวันที่ 28 ไม่สำเร็จ : Fail')
                else:
                    print('คลิกเลือกวันที่เริ่มต้นไม่สำเร็จ : Fail')

                time.sleep(0.5)
                
                End_date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[5]/div[2]/div/div/div/div/button')
                End_date.click()

                date_29 = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[1]')
                assert start_date.is_displayed(), 'Element is not displayed!'
                assert start_date.is_enabled(), 'Element is not enabled!'
                date_29.click()  

                # autogui เลือกเวลา วันที่สิ้นสุด
                pyautogui.moveTo(x=991, y=292) 
                pyautogui.scroll(15)
                time.sleep(0.5)
                pyautogui.click(x=991, y=292)
                pyautogui.click(x=1044, y=308)

                if End_date:
                    print('คลิกเลือกวันที่สิ้นสุดต้นสำเร็จ : Pass')
                    if date_29:
                        print('คลิกเลือกวันที่ 29 สำเร็จ : Pass')
                    else:
                        print('คลิกเลือกวันที่ 29 ไม่สำเร็จ : Fail')
                else:
                    print('คลิกเลือกวันที่สิ้นสุดไม่สำเร็จ : Fail')

                time.sleep(0.5)

                port_date = self.driver.find_element(By.XPATH, '//div[3]/div/div/div/div/button')
                port_date.click()

                date_30 = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[2]')
                assert start_date.is_displayed(), 'Element is not displayed!'
                assert start_date.is_enabled(), 'Element is not enabled!'
                date_30.click()  

                # autogui เลือกเวลา วันที่แผร่เผย
                pyautogui.moveTo(x=1355, y=315) 
                pyautogui.scroll(-15)
                time.sleep(0.5)
                pyautogui.click(x=1355, y=315)
                pyautogui.click(x=1412, y=550)

                if port_date:
                    print('คลิกเลือกวันที่แผร่เผยสำเร็จ : Pass')
                    if date_30:
                        print('คลิกเลือกวันที่ 30 สำเร็จ : Pass')
                    else:
                        print('คลิกเลือกวันที่ 30 ไม่สำเร็จ : Fail')
                else:
                    print('คลิกเลือกวันที่เผยแผร่ไม่สำเร็จ : Fail')

                time.sleep(0.5)

            except ArithmeticError as e:
                self.fail(f'ตรวจสอบไม่สำเร็จ: {e}')
            except NoSuchElementException as b:
                self.fail(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
            except Exception as n:
                self.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
            except TimeoutException:
                self.fail('การรอองค์ประกอบล้มเหลว')


            type_of_work = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[6]/div/div[2]/div/div/div')
            assert type_of_work.is_displayed(), 'Element is not displayed!'
            assert type_of_work.is_enabled(), 'Element is not enabled!'
            type_of_work.click()

            if type_of_work:
                print('คลิกประเภทงานสำเร็จ : Pass')
            else:
                print('คลิกประเภทงานไม่สำเร็จ : Fail')

            wait_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/ul/li[1]'))
            )
            print('รอจนสามารถพิมได้ : Event')

            event = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/ul/li[1]')
            assert event.is_displayed(), 'Element is not displayed!'
            assert event.is_enabled(), 'Element is not enabled!'
            event.click()

            if event:
                print('คลิกเลือกกิจกรรมสำเร็จ : Pass')
            else:
                print('คลิกเลือกกิจกรรมไม่สำเร็จ : Fail')

            add_tags = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div/button')
            assert add_tags.is_displayed(), 'Element is not displayed!'
            assert add_tags.is_enabled(), 'Element is not enabled!'
            add_tags.click()

            if add_tags:
                print('คลิก Add Tage สำเร็จ : Pass')
            else:
                print('คลิก Add Tage ไม่สำเร็จ : Fail')

            wait_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
            )
            print('รอจนสามารถพิมได้ : Tags')

            key_tage = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input')
            key_tage.send_keys('Internship Activity' + Keys.ARROW_DOWN + Keys.ENTER)    

            input_key = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

            creditAmount = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div/input')
            creditAmount.send_keys('1')

            input_key = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div/input')
            input_value = input_key.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

            credit_age = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[3]/div/div/div/div/button')
            assert credit_age.is_displayed(), 'Element is not displayed!'
            assert credit_age.is_enabled(), 'Element is not enabled!'
            credit_age.click()

            date_30 = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[2]')
            assert start_date.is_displayed(), 'Element is not displayed!'
            assert start_date.is_enabled(), 'Element is not enabled!'
            date_30.click()

            if credit_age:
                print('คลิกเลือกวันที่หมดอายุเครดิตสำเร็จ : Pass')
                if date_30:
                    print('คลิกเลือกวันที่ 30 สำเร็จ : Pass')
                else:
                    print('คลิกเลือกวันที่ 30 ไม่สำเร็จ : Pass')
            else:
                print('คลิกเลือกวันที่หมดอายุเครดิตไม่สำเร็จ : Fail')


            # autogui เลือกเวลา อายุเครดิต
            pyautogui.moveTo(x=1266, y=620) 
            pyautogui.scroll(-15)
            time.sleep(0.5)
            pyautogui.click(x=1266, y=620)
            pyautogui.click(x=1317, y=641)
            # time.sleep(3)
            # current_position = pyautogui.position()
            # print(f"The current mouse position is: {current_position}")
            time.sleep(0.3)

            try:

                Add_Permissions = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[1]/button')
                assert Add_Permissions.is_displayed(), 'Element is not displayed!'
                assert Add_Permissions.is_enabled(), 'Element is not enabled!'
                Add_Permissions.click()


                element_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
                time.sleep(1)

                wait_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
                )
                print('รอจนสามารถพิมได้ : company')

                Company = self.driver.find_element(by=By.XPATH, value=
                '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input')
                Company.send_keys('TEST Company' + Keys.ARROW_DOWN + Keys.ENTER)   

                try:    

                    Department = self.driver.find_element(by=By.XPATH, value=
                    '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/input')
                    Department.send_keys('Food and Beverage' + Keys.ARROW_DOWN + Keys.ENTER)

                    wait_element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/div/input'))
                    )
                    print('รอจนสามารถพิมได้ : levels')

                    levels = self.driver.find_element(by=By.XPATH, value=
                    '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/div/input')
                    levels.send_keys('5' + Keys.ARROW_UP + Keys.ENTER + Keys.ESCAPE)


                    save = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/button')
                    assert save.is_displayed(), 'Element is not displayed!'
                    assert save.is_enabled(), 'Element is not enabled!'
                    save.click()
                    time.sleep(1)
                    # if save:
                    #     print('คลิก save สำเร็จ : Pass')
                    # else:
                    #     print('คลิก save ไม่สำเร็จ : Fail') s

                    wait_element = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.ID, 'notistack-snackbar'))
                    )
                    print('รอจนสร้าง Event สำเร็จ : Pass')
                except:
                    print()

 
            except NoSuchElementException as o:
                self.fail(f'ไม่พบองค์ประกอบของ Elenemt')
            except TimeoutException:
                self.fail('การรอองค์ประกอบล้มเหลว')
            except Exception as n:
                self.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง :' + str(n))

                


        except ArithmeticError as e:
            self.fail(f'ตรวจสอบไม่สำเร็จ' + str(e))
        except NoSuchElementException as s:
            self.fail(f'ไม่พบองค์ประกอบของ Elenemt')
        except Exception as n:
            self.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง :' + str(n))
        except TimeoutException:
            self.fail('การรอองค์ประกอบล้มเหลว')
        return result
    
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Impact/page event management'))


