from selenium import webdriver
import time

username = "franfegu.5"
password = "franjyy9977777"

driver = webdriver.Chrome('/home/fran/PycharmProjects/SelDrivers/chromedriver77')

driver.get('http://facebook.com/login')

username_box = driver.find_element_by_id('email')

pass_box = driver.find_element_by_id('pass')

username_box.send_keys(username)

pass_box.send_keys(password)

button = driver.find_element_by_id('loginbutton')

button.submit()

driver.maximize_window()

message = 'Drop your Links I will Listen to You ' \
          ' And Inbox me for 100k Youtube/Spotify/Shazam views/plays/streams in a week.'

group_links = [
    "https://www.facebook.com/groups/1701698006781966",
    "https://www.facebook.com/groups/773571142705684",
    'https://www.facebook.com/groups/60976542975/?ref=group_browse',
    'https://www.facebook.com/groups/46741744505/?ref=group_browse',
    'https://www.facebook.com/groups/1180019522012355/?ref=group_browse',
    'https://www.facebook.com/groups/294515154031720/?ref=group_browse',
    'https://www.facebook.com/groups/56741375896/?ref=group_browse',
    'https://www.facebook.com/groups/598684963539330/?ref=group_browse',
    'https://www.facebook.com/groups/842956785820956/?ref=group_browse',
    'https://www.facebook.com/groups/315363668553307/?ref=group_browse',
    'https://www.facebook.com/groups/2204558278/?ref=group_browse',
    'https://www.facebook.com/groups/1429348253963874/?ref=group_browse',
    'https://www.facebook.com/groups/995159300515447/?ref=group_browse',
    'https://www.facebook.com/groups/274046702610000/?ref=group_browse',
    'https://www.facebook.com/groups/118060402203025/?ref=group_browse',
    'https://www.facebook.com/groups/1520456464898845/?ref=group_browse',
    'https://www.facebook.com/groups/756175754409379/?ref=group_browse',
    'https://www.facebook.com/groups/562339780505323/?ref=group_browse',
    'https://www.facebook.com/groups/370686902980465/?ref=group_browse',
    'https://www.facebook.com/groups/305449069496343/?ref=group_browse',
    'https://www.facebook.com/groups/219992471357737/?ref=group_browse',
    'https://www.facebook.com/groups/182859051784788/?ref=group_browse',
    'https://www.facebook.com/groups/150434338331179/?ref=group_browse',
    'https://www.facebook.com/groups/451516811618657/?ref=group_browse',
    'https://www.facebook.com/groups/327504364089280/?ref=group_browse',
    'https://www.facebook.com/groups/232455230140930/?ref=group_browse',
    'https://www.facebook.com/groups/2241496955/?ref=group_browse',
    'https://www.facebook.com/groups/287171594635131/?ref=group_browse',
    'https://www.facebook.com/groups/396320260456180/?ref=group_browse',
    'https://www.facebook.com/groups/649140485253920/?ref=group_browse',

]

for group in group_links:

    # Go to the Facebook Group
    driver.get(group)

    time.sleep(3)

    # Click the post box
    post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

    # Enter the text we want to post to Facebook
    post_box.send_keys(message)

    time.sleep(3)

    post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")

    clickable = False

    while not clickable:

        cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")

        if cursor == "pointer":

            clickable = True

            break

    post_button.click()

    time.sleep(8)

driver.close()