from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL = (By.ID,"User_Name")
    PASSWORD = (By.ID,"Password")
    LOGIN_INPUT = (By.ID,"loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT,"Sign up")
    
    def __int__(self,driver):
        super().__int__(driver)
        self.driver.get(TestData.Base_URL)
        
    def get_login_page_title(self,title):
        return self.get_title(title)
 
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)
    
    def do_login(self,User_Name,Password):
        self.do_send_keys(self.EMAIL,User_Name)
        self.do_send_keys(self.PASSWORD,Password)
        self.do_click(self.LOGIN_INPUT)
    