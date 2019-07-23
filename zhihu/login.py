from selenium import webdriver
from time import sleep


def login(name, passwd):
    driver = webdriver.Chrome()
    # 智能等待
    driver.implicitly_wait(10)

    url = 'https://www.zhihu.com/signin'
    driver.get(url)

    driver.find_element_by_name('username').send_keys(name)
    driver.find_element_by_name('password').send_keys(passwd)

    sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()
    # 暂停10秒便于观察,接着结束
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    acount_num = "test2"
    passwd_str = "123456"
    login(acount_num, passwd_str)
