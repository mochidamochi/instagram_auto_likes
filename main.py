from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time

#Webdriver
browser = webdriver.Chrome(executable_path='[chromedriver.exeのパス]')

#URL
loginURL = "https://www.instagram.com/"
tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja"

#selectors
loginPath = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
likePath = "//button/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']"
likeButtonPath = "//button[@class='dCJp8 afkep _0mzm-']"

mediaSelector = 'div._9AhH0' #表示されているメディアのwebelement
nextPagerSelector = 'a.coreSpriteRightPaginationArrow' #次へボタン

#USER INFO
username = "[username]"
password = "[password]"
#params
tagName = "[タグ名]"
likedCounter = 0
likedMax = 500

if __name__ == '__main__':

    #login 
    browser.get(loginURL)
    time.sleep(3)
    browser.find_element_by_xpath(loginPath).click()
    time.sleep(3)
    usernameField = browser.find_element_by_name('username')
    usernameField.send_keys(username)
    passwordField = browser.find_element_by_name('password')
    passwordField.send_keys(password)
    passwordField.send_keys(Keys.RETURN)

    #tag search
    time.sleep(3)
    encodedTag = urllib.parse.quote(tagName) #普通にURLに日本語は入れられないので、エンコードする
    encodedURL = tagSearchURL.format(encodedTag)
    print("encodedURL:{}".format(encodedURL))
    browser.get(encodedURL)

    #media click
    time.sleep(3)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector(mediaSelector).click()
    
    #次へボタンが表示されないか、いいねが一定数いくまで
    while likedCounter < likedMax:
        time.sleep(3)
        try:
            browser.find_element_by_xpath(likePath)
            browser.find_element_by_xpath(likeButtonPath).click()
            likedCounter += 1
            print("liked {}".format(likedCounter))
        except:
            #読み込まれなかったり既にいいねしているならパス
            print("pass")
            pass

        #次へ
        try:
            browser.find_element_by_css_selector(nextPagerSelector).click()
        except:
            break

    print("You liked {} media".format(likedCounter))