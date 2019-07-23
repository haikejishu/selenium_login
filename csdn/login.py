from time import sleep
from selenium import webdriver

# 这个例子用多种方式定位元素,实际并不一定需要,仅供学习例子


def login(name, passwd):

    driver = webdriver.Chrome()
    # 智能等待
    driver.implicitly_wait(10)

    url = 'https://passport.csdn.net/login'
    driver.get(url)

    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div/div[2]/div[5]/ul/li[2]/a').click()

    driver.find_element_by_name('all').send_keys(name)
    driver.find_element_by_id('password-number').send_keys(passwd)

    sleep(3)
    driver.find_element_by_css_selector('.btn.btn-primary').click()

    # 暂停10秒便于观察,接着结束
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    login_name = "test"
    login_passwd = "123456"
    login(login_name, login_passwd)
