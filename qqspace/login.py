from selenium import webdriver
from time import sleep


def login(name, passwd):
    driver = webdriver.Chrome()
    # 智能等待
    driver.implicitly_wait(10)

    url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?daid=5&appid=549000912&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone'
    driver.get(url)

    driver.find_element_by_id("switcher_plogin").click()

    driver.find_element_by_name('u').send_keys(name)
    driver.find_element_by_name('p').send_keys(passwd)

    sleep(3)
    driver.find_element_by_id('login_button').click()
    # 暂停10秒便于观察,接着结束
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    acount_num = "test"
    passwd_str = "123456"
    login(acount_num, passwd_str)
