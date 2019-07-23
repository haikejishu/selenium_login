from selenium import webdriver
from time import sleep


def login(name, passwd):
    driver = webdriver.Chrome()
    # 智能等待
    driver.implicitly_wait(10)

    url = 'https://login.sina.com.cn/signup/signin.php'
    driver.get(url)

    driver.find_element_by_name('username').send_keys(name)
    driver.find_element_by_name('password').send_keys(passwd)

    sleep(3)
    driver.find_element_by_xpath('//*[@id="vForm"]/div[2]/div/ul/li[7]/div[1]/input').click()
    # 暂停10秒便于观察,接着结束
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    acount_num = "test"
    passwd_str = "123456"
    login(acount_num, passwd_str)
