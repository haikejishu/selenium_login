from time import sleep
from selenium import webdriver


def login(name, passwd):

    driver = webdriver.Chrome()
    # 智能等待
    driver.implicitly_wait(10)

    url = 'https://pan.baidu.com/'
    driver.get(url)

    driver.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn').click()
    driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys(name)
    driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys(passwd)

    sleep(3)
    driver.find_element_by_id('TANGRAM__PSP_4__submit').click()

    # 暂停10秒便于观察,接着结束
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    login_name = "test"
    login_passwd = "123456"
    login(login_name, login_passwd)
