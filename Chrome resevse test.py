#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver_path = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(driver_path)
browser.get("https://app.tzuchi.com.tw/tchw/OpdReg/OpdTimeShow.aspx?Depart=%e9%97%9c%e7%af%80%e4%b8%ad%e5%bf%83&HospLoc=1")
while 1:
    try:
        WebDriverWait(browser,1 , 0.4).until(EC.presence_of_element_located((By.LINK_TEXT, '呂紹睿')))
        search = browser.find_element(By.LINK_TEXT,'呂紹睿').click()
        print(search)
        print('已定位到元素')
        break
    except:
        print('尚未定位到元素')
        browser.refresh()
browser.find_element(By.ID,'rblRegFM_0').click()
browser.find_element(By.NAME,'txtMRNo').send_keys('E123456123')
browser.find_element(By.NAME,'txtTel').send_keys('0916150713')
browser.find_element(By.NAME,'txtVCode').click()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




