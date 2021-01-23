from selenium import webdriver
import time
import sys

driver = webdriver.Chrome(executable_path = "C:/Users/Luis/Desktop/Integradora/NodalRetos/bin/chromedriver.exe")
driver.get(sys.argv[1])
time.sleep(3)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass

#  By4nA loading class
try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    #wait_more_comment = driver.find_element_by_css_selector('.MGdpg > div')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed():# and i < int(sys.argv[2]):
        """
        if  not driver.find_element_by_css_selector('.MGdpg > div.By4nA').isEmpty():
            print('wait')
            time.sleep(3)
            break
        """
        load_more_comment.click()
        time.sleep(3)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
        print(i)
except Exception as e:
    print("hola")
    print(e)
    pass
user_names = []
user_comments = []
user_comments_date = []
user_comments_likes = []
comments_id = []
comments_id_child = []
post = driver.find_element_by_xpath("//meta[@property='og:url']").get_attribute('content')
#print(post)
comment = driver.find_elements_by_class_name('gElp9 ')
first = 0
id = 0
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
#    Post, Caption, Date, likesComment, IdFatherComment, IdChildComment, Username

    name = container.find_element_by_class_name('_6lAjh').text
    if 'Verified' in name:
        name = name.replace('\n', '').replace('"','').replace('Verified','')
    if first == 0:
        first = 1
        content = container.find_element_by_css_selector('span:nth-child(2)').text
    else:
        content = container.find_elements_by_tag_name('span')
        print(len(content))
        if len(content) == 1:
            content = content[0].text
        else:
            content = content[1].text
    content = content.replace('\n', ' ').strip().rstrip()
    date = container.find_element_by_tag_name('time').get_attribute('datetime')

    #likes = container.find_element_by_class_name('_7UhW9')
    like_html = c.get_attribute('innerHTML')
    index_f = like_html.rindex('button')
    #print(index_f)
    like_sub_str = like_html[index_f - 50:index_f]
    like = '0'
    if 'like' in like_sub_str:
        index_like = like_sub_str.index('like')
        like = like_sub_str[index_like - 2:index_like]

    user_names.append(name)
    user_comments.append(content)
    user_comments_date.append(date)
    user_comments_likes.append(like)
    comments_id.append(str(id))
    # SCRAP CHILD COMMENTS


    comments_id_child.append('')
    id += 1

    #print("-", end='')
#print('\n')
user_names.pop(0)
caption = user_comments.pop(0)
user_comments_date.pop(0)
user_comments_likes.pop(0)
comments_id.pop(0)
comments_id_child.pop(0)
from Reto2 import csv_exporter

csv_exporter.export(post,
                    caption,
                    user_comments_date,
                    user_comments_likes,
                    comments_id,
                    comments_id_child,
                    user_comments,
                    user_names)

driver.close()

