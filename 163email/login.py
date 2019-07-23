from selenium import webdriver
from time import sleep


def login(name, passwd):

    driver = webdriver.Chrome()
    # 智能等待
    driver.implicitly_wait(10)

    url = 'https://mail.163.com/'
    driver.get(url)
    driver.find_element_by_id("lbNormal").click()

    # 163登陆框是使用iframe进行嵌套的，所以需要先切换到该iframe
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    driver.find_element_by_name('email').send_keys(name)
    driver.find_element_by_name('password').send_keys(passwd)

    sleep(3)
    driver.find_element_by_id('dologin').click()
    # 暂停10秒便于观察,接着结束
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    login_name = "test"
    login_passwd = "123456"
    login(login_name, login_passwd)
