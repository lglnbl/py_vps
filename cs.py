from selenium import webdriver

 

url = 'http://www.baidu.com'

 

#  创建配置对象

opt = webdriver.ChromeOptions()

 

#  添加配置参数

opt.add_argument('--headless')

opt.add_argument('--disable-gpu')

 

#  创建浏览器对象的时候添加配置对象

driver = webdriver.Chrome(chrome_options=opt)

driver.get(url)

driver.save_screenshot('baidu_views.png')
1 = 1
