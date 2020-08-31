#The project is based on the instagram's "follow and unfollow and like" process. In one sense its an Instagram Bot.

#It makes use of functions and classes to carry out the task.

#We are using selenium webdriver in order to scrap and parse the information we are getting.

#Here, what exactly we are doing is that we first made the class InstagramBots, and then we are initializing the username
 and password details to be entered.

#When the login function is called, it prompts the user to enter its login details like username and password.

#When the login details are entererd, the for loop actiavtes and opens the account of the user.

#Further the user is prompted whether he wants to like/unlike the pic when the function like_pic is called.

#Similarly when the follow and unfollow functions are called the user is prompted and asked whether they want to follow or 
 unfollow the particular person's Insta account.

#Its like a third party application that fetches the data from instagram and then carries out the basic work that Instagram carries out. 



from selenium import webdriver
from selenium.webdriver.common import keys  #use it to press regular keys like return etc
import time

class Instagram_Bot(object):

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        usr = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        usr.clear()
        usr.send_keys(self.username)

        passw = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        passw.clear()
        passw.send_keys(self.password)
        time.sleep(1)

        log = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
        log.click()
        time.sleep(3)

        not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        not_now.click()
        time.sleep(3)

    def like_pic(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+'/')

        pic_hrefs = []
        for i in range(1,7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)

                hrefs_in_view = driver.find_elements_by_tag_name('a')
                #print(hrefs_in_view)
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if ".com/p/" in elem.get_attribute('href')]
                #print(hrefs_in_view)
                for href in hrefs_in_view:
                    if href not in pic_hrefs:
                        pic_hrefs.append(href)
            except Exception as e:
                continue
        #print(len(pic_hrefs))

        for link in pic_hrefs:
            driver.get(link)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            like_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg/path')
            like_button.click()
            time.sleep(3)

    def follow(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+'/')

        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # print(hrefs_in_view)
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if".com/p/" in elem.get_attribute('href')]
                # print(hrefs_in_view)
                for href in hrefs_in_view:
                    if href not in pic_hrefs:
                        pic_hrefs.append(href)
            except Exception as e:
                continue

        users = []
        for link in pic_hrefs:
            driver.get(link)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            try:
                profile = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/a")
                if profile.get_attribute('title') not in users:
                    users.append(profile.get_attribute('title'))
                    follow_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
                    follow_button.click()
                    time.sleep(7)
                else:
                    continue

            except Exception:
                continue

    def like_follow(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + '/')

        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # print(hrefs_in_view)
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if".com/p/" in elem.get_attribute('href')]
                # print(hrefs_in_view)
                for href in hrefs_in_view:
                    if href not in pic_hrefs:
                        pic_hrefs.append(href)
            except Exception as e:
                continue
        # print(len(pic_hrefs))
        users = []
        for link in pic_hrefs:
            driver.get(link)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            try:
                like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]')
                like_button.click()
                time.sleep(5)
                profile = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/a")
                if profile.get_attribute('title') not in users:
                    users.append(profile.get_attribute('title'))
                    follow_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")
                    follow_button.click()
                    time.sleep(7)
                else:
                    continue
            except Exception as e :
                continue



if __name__ == "__main__":

    while True:

        usr_input = int(input("What Do You Want t do:\n1.Like Photos\n2.Follow People\n3.Like and Follow People\n[1,2,3]:"))

        hastag = []
        usr = input("Enter Your IG username:")
        pss = input("Enter you IG Password:")
        hastag = input("Enter a Hashtag[if more than one enter using commas]:")

        if usr_input == 1:
            ib = Instagram_Bot(usr, pss)

            print("Opening Browser and loging into your account...")
            ib.login()
            ib.like_pic(hastag)
            ib.close_browser()

        elif usr_input == 2:
            ib = Instagram_Bot(usr, pss)

            print("Opening Browser and loging into your account...")
            ib.login()
            ib.follow(hastag)
            ib.close_browser()

        elif usr_input == 3:
            ib = Instagram_Bot(usr, pss)

            print("Opening Browser and loging into your account...")
            ib.login()
            ib.like_follow(hastag)
            ib.close_browser()

        elif usr_input == 0:
            break

        else:
            print("Enter a valid option")
        continue
