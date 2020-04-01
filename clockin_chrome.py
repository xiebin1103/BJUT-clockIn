import os
import time
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.chrome.options import Options

account='18013121'
password='103311'
userhour,userminute=[12,55]

def clockIn():
    chrome_options=Options()

    #   浏览器不提供可视化页面
    # chrome_options.add_argument("--user-data-dir=C:/Users\dell/AppData/ocal/Google/Chrome/User Data/Default")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(r"https://www.baidu.com/s?ie=UTF-8&wd=%E6%9C%AC%E6%9C%BAIP")
    time.sleep(100)
    driver.get(r"https://itsapp.bjut.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fitsapp.bjut.edu.cn%2Fsite%2FapplicationSquare%2Findex%3Fsid%3D1")
    time.sleep( 2 )
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/input").send_keys(account)  # 输入账号
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/input").send_keys(password)  # 输入密码
    driver.find_element_by_class_name("btn").click()  # 点击登陆
    print('正在登陆...')
    time.sleep( 2 )
    driver.get(r"https://itsapp.bjut.edu.cn/ncov/wap/default/index")
    time.sleep( 5 )
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input").click()  # 获取地理位置
    print('正在获取地理位置...请等待')
    time.sleep( 10 )
#    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[5]/div/a").click()
    driver.find_element_by_class_name("wapcf-btn-qx").click() # 提交信息
    time.sleep( 5 )
    driver.close()
    print("打卡完成！按Y重新打卡,关闭窗口即可退出 ")

if __name__ == '__main__':
#    scheduler = BlockingScheduler()
#    scheduler.add_job(clockIn, 'cron', hour=(userhour),minute=(userminute))
    clockIn()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass