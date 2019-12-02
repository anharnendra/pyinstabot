from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


webdriver = webdriver.Firefox(executable_path='/home/vinay/Downloads/geck/geckodriver')
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('vinayummadi')
password = webdriver.find_element_by_name('password')
password.send_keys('TFxtcnqpxTFYP88')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

#notnow = webdriver.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
#notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

hashtag_list = ['foradult']

prev_user_list = [] #- #if it's the first time you run it, use this line and comment the two below
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath('/html/body/span/section/main/article/div[1]/div/div/div[1]/div[1]')
    #
    #//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div
    first_thumbnail.click()
    sleep(randint(1,2))    

    for x in range(1,200):
            print("In for loop")
            #/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button
            username = webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            #/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a
            
                # If we already follow, do not unfollow
                                             #
                    
            webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    
            new_followed.append(username)
            followed += 1

                    # Liking the picture
                    #/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span
                    #/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span
           # button_like = webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button')
            #button_like.click()
            #likes += 1
            sleep(randint(0,10))
            webdriver.find_element_by_link_text('Next').click()
            sleep(randint(0,10))

    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next


for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))



#/html/body/span/section/main/article/div[1]/div/div/div[1]/div[1]
