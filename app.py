#coding=utf-8
import time

from selenium import webdriver
import selenium

opt = webdriver.ChromeOptions()  # 创建浏览器
# opt.headless = True  # 无窗口模式 可注释此行查看chrome运行情况
driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
driver.get('https://xgbxscwx.seu.edu.cn/#/')  # 打开网页
time.sleep(3)

driver.find_element_by_xpath("//input[@id='username']").send_keys("账号")  # 填入你的一卡通号
driver.find_element_by_xpath("//input[@id='password']").send_keys("密码")  # 填入你的密码
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

print(driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/h2").text)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div[1]").click()
time.sleep(2)

try:
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div/form/div[9]/div/button").click()
except selenium.common.exceptions.NoSuchElementException:
    print('今日已上报')
else:
    print('上报成功！')