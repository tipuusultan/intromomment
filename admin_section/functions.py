# from requests_html import HTMLSession   
# from bs4 import BeautifulSoup
# from youtubesearchpython import Channel

# session = HTMLSession()  
# url = 'https://www.youtube.com/watch?v=Ze3t5Z7ODbQ'
# r = session.get(url)  
# ok = r.html.render(timeout=123234)  
# print(ok)

def GetSubscribersCount(ChannelURL):
    from pytube import Channel, YouTube
    import requests
    import json

    YT_API = 'AIzaSyArAj0JJdaetxKRJokWujiabzrmJ2jFZI8'
    c = Channel(ChannelURL)
    channelID = c.channel_id
    # Video1 = c[0]
    r = requests.get(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channelID}&key={YT_API}')
    data = r.text
    JsonData = json.loads(data)
    return JsonData['items'][0]['statistics']['subscriberCount']

def ConvertStringNumberToNumber(value):
    if value:
        # determine multiplier
        multiplier = 1
        if value.endswith('K'):
            multiplier = 1000
            value = value[0:len(value)-1] # strip multiplier character

        elif value.endswith('k'):
            multiplier = 1000
            value = value[0:len(value)-1] # strip multiplier character

        elif value.endswith('M'):
            multiplier = 1000000
            value = value[0:len(value)-1] # strip multiplier character
        
        elif value.endswith('m'):
            multiplier = 1000000
            value = value[0:len(value)-1] # strip multiplier character

        # convert value to float, multiply, then convert the result to int
        return int(float(value) * multiplier)

    else:
        return 0

def GetTop20YTChannels(condition='mostsubscribed'):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")
    driver = webdriver.Chrome("C:\chromedriver.exe" , chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(f"https://socialblade.com/youtube/top/country/hk/{condition}")
    one=driver.find_elements("xpath", "//div[@style='width: 860px; background: #fafafa; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;']/div[@style]")
    two=driver.find_elements("xpath", "//div[@style='width: 860px; background: #f8f8f8;; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;']/div[@style]")
    three=driver.find_elements("xpath", "//div[@style='width: 860px; background: #fafafa; padding: 0px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 30px;']/div[@style]")
    four = driver.find_elements("xpath", "//div[@style='width: 860px; background: #f8f8f8;; padding: 0px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 30px;']/div[@style]")
    link = driver.find_elements("xpath", "/html[1]/body[1]/div[11]/div[2]//div[3]/a[1]")
    onelist=[]
    twolist=[]
    threelist=[]
    fourlist=[]
    linklist=[]
    ###########################################
    count=0
    for i in link:
        linklist.append(i.get_attribute("href"))
        count=count+1
        if count == 20:
            break
    ##########################################
    userlink = ["Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link","Link"]
    file5 = list(zip(userlink,linklist))
    ###########################################
    for i in one:
        onelist.append(i.text)
    ############################################
    for j in two:
        twolist.append(j.text)
    ###########################################
    for k in three:
        if k.text == "21st":
            break
        else:
            threelist.append(k.text)
    #####################################################
    for l in four:
        if l.text == "22nd":
            break
        else:
            fourlist.append(l.text)
    ###############################################################################################
    for i in onelist:
        if i == "1st" or i == "3rd" or i == "5th" or i == "7th" or i == "9th":
            onelist.remove(i)
    for i in onelist:
        if i == '':
            onelist.remove(i)
    for i in onelist:
        if i == "B-" or i == "B+" or i == "A-" or i == "A+":
            onelist. remove(i)
    ##############################################################
    for i in twolist:
        if i == "2nd" or i == "4th" or i == "6th" or i == "8th" or i == "10th":
            twolist.remove(i)
    for i in twolist:
        if i == '':
            twolist.remove(i)
    for i in twolist:
        if i == "B-" or i == "B+" or i == "A-" or i == "A+" or i == "B":
            twolist. remove(i)
    ###############################################################
    for i in threelist:
        if i == "11th" or i == "13th" or i == "15th" or i == "17th" or i == "19th":
            threelist.remove(i)
    for i in threelist:
        if i == '':
            threelist.remove(i)
    for i in threelist:
        if i == "B-" or i == "B+" or i == "A-" or i == "A+" or i == "B":
            threelist. remove(i)
    ####################################################################
    for i in fourlist:
        if i == "12th" or i == "14th" or i == "16th" or i == "18th" or i == "20th":
            fourlist.remove(i)
    for i in fourlist:
        if i == '':
            fourlist.remove(i)
    for i in fourlist:
        if i == "B-" or i == "B+" or i == "A-" or i == "A+" or i == "B":
            fourlist.remove(i)
    ######################################################################
    onefront = ["Username", "Uploads", "Subscribers", "Video Views","Username", "Uploads", "Subscribers", "Video Views", "Username", "Uploads", "Subscribers", "Video Views","Username", "Uploads", "Subscribers", "Video Views","Username", "Uploads", "Subscribers", "Video Views"]
    file1=list(zip(onefront,onelist))
    u1 = file1[0],file1[1],file1[2],file1[3], file5[0]
    u3 = file1[4],file1[5],file1[6],file1[7], file5[1]
    u5 = file1[8],file1[9],file1[10],file1[11], file5[2]
    u7 = file1[12],file1[13],file1[14],file1[15], file5[3]
    u9 = file1[16],file1[17],file1[18],file1[19], file5[4]

    ########################################################################
    file2=list(zip(onefront,twolist))
    u2 = file2[0],file2[1],file2[2],file2[3], file5[5]
    u4 = file2[4],file2[5],file2[6],file2[7],file5[6]
    u6 = file2[8],file2[9],file2[10],file2[11],file5[7]
    u8 = file2[12],file2[13],file2[14],file2[15],file5[8]
    u10 = file2[16],file2[17],file2[18],file2[19],file5[9]
    ########################################################################
    file3 = list(zip(onefront,threelist))
    u11 = file3[0],file3[1],file3[2],file3[3],file5[10]
    u13 = file3[4],file3[5],file3[6],file3[7],file5[11]
    u15 = file3[8],file3[9],file3[10],file3[11],file5[12]
    u17 = file3[12],file3[13],file3[14],file3[15],file5[13]
    u19 = file3[16],file3[17],file3[18],file3[19],file5[14]
    #######################################################################
    file4 = list(zip(onefront,fourlist))
    u12 = file4[0],file4[1],file4[2],file4[3],file5[15]
    u14 = file4[4],file4[5],file4[6],file4[7],file5[16]
    u16 = file4[8],file4[9],file4[10],file4[11],file5[17]
    u18 = file4[12],file4[13],file4[14],file4[15],file5[18]
    u20 = file4[16],file4[17],file4[18],file4[19],file5[19]

    user = 'user'
    user1 = dict(u1)
    user2 = dict(u2)
    user3 = dict(u3)
    user4 = dict(u4)
    user5 = dict(u5)
    user6 = dict(u6)
    user7 = dict(u7)
    user8 = dict(u8)
    user9 = dict(u9)
    user10 = dict(u10)
    user11 = dict(u11)
    user12 = dict(u12)
    user13 = dict(u13)
    user14 = dict(u14)
    user15 = dict(u15)
    user16 = dict(u16)
    user17 = dict(u17)
    user18 = dict(u18)
    user19 = dict(u19)
    user20 = dict(u20)

    Top20Channels = [user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12,user13,user14,user15,user16,user17,user18,user19,user20]
    return Top20Channels
    

def GetTop20InstaPages(url='https://www.noxinfluencer.com/instagram-channel-rank/top-100-hk-all-sorted-by-followers-weekly'):

    from selenium import webdriver
    from packaging import __version__
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    opt = Options()
    opt.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
    driver.get(url)
    driver.implicitly_wait(20)
    s = driver.find_elements("xpath", "//a[@class='link clearfix']")
    b = driver.find_elements("xpath", "//div[@id='table-body']/div/span")
    mlist = ["Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers" ]
    linkbox = []
    totallist = []
    count = 0
    for i in b:
        totallist.append(i.text)
        count = count+1
        if count == 120:
            break
    for i in totallist:
        if i == "":
            totallist.remove(i)
    for i in range(0,80,4):
        totallist.pop(i)

    file = list(zip(mlist, totallist))

    c = 0
    for i in s:
        linkbox.append(i.get_attribute("href"))
        c = c+1
        if c == 20:
            break
    linkbox2=["Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link"]
    file2 = list(zip(linkbox2, linkbox))



    u1 = file[0],file[1],file[2],file[3],file2[0]
    u2 = file[4],file[5],file[6],file[7],file2[1]
    u3 = file[8],file[9],file[10],file[11],file2[2]
    u4 = file[12],file[13],file[14],file[15],file2[3]
    u5 = file[16],file[17],file[18],file[19],file2[4]
    u6 = file[20],file[21],file[22],file[23],file2[5]
    u7 = file[24],file[25],file[26],file[27],file2[6]
    u8 = file[28],file[29],file[30],file[31],file2[7]
    u9 = file[32],file[33],file[34],file[35],file2[8]
    u10 = file[36],file[37],file[38],file[39],file2[9]
    u11= file[40],file[41],file[42],file[43],file2[10]
    u12= file[44],file[45],file[46],file[47],file2[11]
    u13= file[48],file[49],file[50],file[51],file2[12]
    u14= file[52],file[53],file[54],file[55],file2[13]
    u15 = file[56],file[57],file[58],file[59],file2[14]
    u16 = file[60],file[61],file[62],file[63],file2[15]
    u17= file[64],file[65],file[66],file[67],file2[16]
    u18= file[68],file[69],file[70],file[71],file2[17]
    u19= file[72],file[73],file[74],file[75],file2[18]
    u20= file[76],file[77],file[78],file[79],file2[19]
    user1 = dict(u1)
    user2 = dict(u2)
    user3 = dict(u3)
    user4 = dict(u4)
    user5 = dict(u5)
    user6 = dict(u6)
    user7 = dict(u7)
    user8 = dict(u8)
    user9 = dict(u9)
    user10 = dict(u10)
    user11= dict(u11)
    user12= dict(u12)
    user13= dict(u13)
    user14= dict(u14)
    user15= dict(u15)
    user16= dict(u16)
    user17= dict(u17)
    user18= dict(u18)
    user19= dict(u19)
    user20= dict(u20)
    Top20Pages = [user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12,user13,user14,user15,user16,user17,user18,user19,user20]
    return Top20Pages

def SeliniumInit():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    driverPath = ChromeDriverManager().install()

    driver = webdriver.Chrome(driverPath,chrome_options=options)

    return driver
    
def GetAllVideos_From_YTChannel_Selenium(ids,driver,time):
    # from selenium import webdriver
    # from webdriver_manager.chrome import ChromeDriverManager
    # import time
    # from selenium.webdriver.chrome.options import Options
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    # driverPath = ChromeDriverManager().install()

    # driver = webdriver.Chrome(driverPath,chrome_options=options)

    for id in ids:
        url = f'https://www.youtube.com/channel/{id}/videos'

        driver.get(url)

        height = driver.execute_script("return document.documentElement.scrollHeight")
        previousHeight = -1

        while previousHeight < height:
            previousHeight = height
            driver.execute_script(f'window.scrollTo(0,{height + 10000})')
            time.sleep(1)
            height = driver.execute_script("return document.documentElement.scrollHeight")

        vidElements = driver.find_elements_by_id('thumbnail')
        vid_urls = []
        for v in vidElements:
            link = str(v.get_attribute('href'))
            if 'youtube.com' in link:
                vid_urls.append(v.get_attribute('href'))

    return vid_urls

def GetNumbersOfComments(url=''):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager

    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driverPath = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=options, executable_path=driverPath)
    driver.get("https://www.youtube.com/watch?v=N0lxfilGfak")
    driver.execute_script("return scrollBy(0, 1000);")
    subscribe = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//yt-formatted-string[text()='Subscribe']")))
    driver.execute_script("arguments[0].scrollIntoView(true);",subscribe)
    # using xpath and text attribute
    # print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//h2[@id='count']/yt-formatted-string"))).text)
    # using cssSelector and get_attribute()
    print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h2#count>yt-formatted-string"))).get_attribute("innerHTML"))

def InstaSeliniumInit():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    import pickle
    driver = webdriver.Chrome('C://chromedriver.exe')
    return driver



    # USING SELENIUM........

# def GetInstaPageDetails(username, cookiePath, driver):
#     from selenium.webdriver.common.keys import Keys
#     from selenium.webdriver.support import expected_conditions as EC
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.wait import WebDriverWait
#     import pickle
#     from time import sleep
    

#     page = username
#     driver.get("http://www.instagram.com")
#     # first trying to login with cookies file
#     try:
#         cookies = pickle.load(open(cookiePath, "rb"))
#         for cookie in cookies:
#             driver.add_cookie(cookie)
#         driver.get("https://www.instagram.com/")

#     except:
#         username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
#         password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
#         username.clear()
#         username.send_keys("de.vilseye")
#         password.clear()
#         password.send_keys("9707@TIPUsultan")
#         button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#     #dismiss NOT NOW
#     try:
#         not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
#         not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
#     except:
#         pass

#     wait = WebDriverWait(driver, 5)
#     sleep(2)
#     posts = []
#     PageURL = f'https://www.instagram.com/{page}'
#     driver.get(PageURL)
#     sleep(4)
#     Fullname = driver.find_element(By.XPATH, "//*[@class='_aacl _aacp _aacw _aacx _aad7 _aade']")
#     Data = driver.find_elements(By.XPATH, "//*[@class='x78zum5 x1q0g3np xieb3on']")
#     Datas = Data[0].text
#     Posts_Followers_Follwoings = Datas.splitlines()
#     Number_of_Posts = Posts_Followers_Follwoings[0]
#     Number_of_Followers = Posts_Followers_Follwoings[1]
#     Number_of_Followings =  Posts_Followers_Follwoings[2]

#     return Number_of_Posts, Number_of_Followers

# WITHOUT USING SELENIUM..
def GetInstaPageDetails(username):
    import requests
    import urllib.request
    import urllib.parse
    import urllib.error
    from bs4 import BeautifulSoup
    import ssl

    url = f'https://www.instagram.com/{username}'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('meta', attrs={'property': 'og:description'
                            })
    text = data[0].get('content').split()
    user = '%s %s %s' % (text[-3], text[-2], text[-1])
    followers = text[0]
    following = text[2]
    posts = text[4]
    info={}
    info["User"] = user
    info["Followers"] = followers
    info["Following"] = following
    info["Posts"] = posts
    return followers, posts


def GetAllPostsInstagram(username, cookiePath, driver):
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    import pickle
    from time import sleep
    

    page = username
    driver.get("http://www.instagram.com")
    # first trying to login with cookies file
    try:
        cookies = pickle.load(open(cookiePath, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://www.instagram.com/")

    except:
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username.clear()
        username.send_keys("de.vilseye")
        password.clear()
        password.send_keys("9707@TIPUsultan")
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #dismiss NOT NOW
    try:
        not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
        not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    except:
        pass

    wait = WebDriverWait(driver, 5)
    sleep(2)
    posts = []
    PageURL = f'https://www.instagram.com/{page}'
    driver.get(PageURL)
    sleep(4)
    Links = []
    article = driver.find_element_by_tag_name('article')
    height = driver.execute_script("return document.documentElement.scrollHeight")
    import time
    previousHeight = -1
    while previousHeight < height:
        previousHeight = height
        driver.execute_script(f'window.scrollTo(0,{height + 10000})')
        a = article.find_elements_by_tag_name('a')
        print(a)
        for link in a:
            if link not in Links:
                Links.append(link)
        time.sleep(5)
        height = driver.execute_script("return document.documentElement.scrollHeight")

    return Links