from selenium import webdriver
from Reto3.time_util import sleep
from selenium.common.exceptions import NoSuchElementException

# get login credentials
email = input(print('Enter email: '))
password = input(print('Enter password: '))

# get post url
post_url = input(print('Enter post url: '))

# create a new Chrome session
chromedriver_location = "../bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.maximize_window()

# log in
driver.get("https://www.facebook.com")
search_field = driver.find_element_by_id("email")
search_field.send_keys(email)
search_field = driver.find_element_by_id("pass")
search_field.send_keys(password)
search_field.submit()

print("Logged in as " + email)

# navigate to the post url
driver.get(post_url)
engagement_div = driver.find_element_by_css_selector("#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.buofh1pr.dp1hu0rb.ka73uehy > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.dp1hu0rb > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.cxgpxx05 > div > div.rq0escxv.l9j0dhe7.du4w35lb.qmfd67dx.hpfvmrgz.gile2uim.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5 > div.dp1hu0rb.d2edcug0.taijpn5t.j83agx80.gs1a9yip > div > div > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(5) > div > div > div:nth-child(1) > div > div.l9j0dhe7 > div > div.bp9cbjyn.j83agx80.buofh1pr.ni8dbmo4.stjgntxs > div > span > div > span.gpro0wi8.cwj9ozl2.bzsjyuwj.ja2t1vim > span > span")
driver.execute_script("arguments[0].click();", engagement_div)

# switch to all engagement - not working
engagement_all = driver.find_element_by_css_selector("#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div.q5bimw55.rpm2j7zs.k7i0oixp.gvuykj2m.j83agx80.cbu4d94t.ni8dbmo4.eg9m0zos.l9j0dhe7.du4w35lb.ofs802cu.pohlnb88.dkue75c7.mb9wzai9.l56l04vs.r57mb794.kh7kg01d.c3g1iek1.otl40fxz.cxgpxx05.rz4wbd8a.sj5x9vvc.a8nywdso > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7")
driver.execute_script("arguments[0].click();", engagement_div)

# click see more until there no such option
print("Loading all the users.")

while True:
    try:
        viewMoreButton = driver.find_element_by_css_selector("a[href*='/ufi/reaction/profile/browser/fetch']")
        driver.execute_script("arguments[0].click();", viewMoreButton)
        sleep(2)
    except NoSuchElementException:
        break

# invite users
print("Inviting the users.")
users = driver.find_elements_by_css_selector("a[ajaxify*='/pages/post_like_invite/send/']")
invitedUsers = 0

for i in users:
    user = driver.find_element_by_css_selector("a[ajaxify*='/pages/post_like_invite/send/']")
    driver.execute_script("arguments[0].click();", user)
    invitedUsers = invitedUsers + 1
    sleep(1)

print('My job is done here. I have invited: ' + str(invitedUsers))

# close the browser window
driver.quit()