from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time

#Webdriver
browser = webdriver.Chrome(executable_path='[chromedriver.exeのパス]')

#URL
MAIN_URL = "https://www.instagram.com/"
TAG_SEARCH_URL = MAIN_URL + "explore/tags/{}/?hl=ja"

#selectors
LOGIN_PATH = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
LIKE_PATH = "//button/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']"
LIKE_BUTTON_PATH = "//button[@class='dCJp8 afkep _0mzm-']"

MEDIA_SELECTOR = 'div._9AhH0' #表示されているメディアのwebelement
NEXT_PAGE_SELECTOR = 'a.coreSpriteRightPaginationArrow' #次へボタン

#USER INFO
username = "[username]"
password = "[password]"
#params
tagName = "[タグ名]"
likedCounter = 0
likedMax = 500

if __name__ == '__main__':

    #login 
    browser.get(MAIN_URL)
    time.sleep(3)
    browser.find_element_by_xpath(LOGIN_PATH).click()
    time.sleep(3)
    usernameField = browser.find_element_by_name('username')
    usernameField.send_keys(username)
    passwordField = browser.find_element_by_name('password')
    passwordField.send_keys(password)
    passwordField.send_keys(Keys.RETURN)

    #tag search
    time.sleep(3)
    encodedTag = urllib.parse.quote(tagName) #普通にURLに日本語は入れられないので、エンコードする
    encodedURL = TAG_SEARCH_URL.format(encodedTag)
    print("encodedURL:{}".format(encodedURL))
    browser.get(encodedURL)

    #media click
    time.sleep(3)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector(MEDIA_SELECTOR).click()
    
    #次へボタンが表示されないか、いいねが一定数いくまで
    while likedCounter < likedMax:
        time.sleep(3)
        try:
            browser.find_element_by_xpath(LIKE_PATH)
            browser.find_element_by_xpath(LIKE_BUTTON_PATH).click()
            likedCounter += 1
            print("liked {}".format(likedCounter))
        except:
            #読み込まれなかったり既にいいねしているならパス
            print("pass")
            pass

        #次へ
        try:
            browser.find_element_by_css_selector(NEXT_PAGE_SELECTOR).click()
        except:
            break

    print("You liked {} media".format(likedCounter))