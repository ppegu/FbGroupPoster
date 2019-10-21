from selenium import webdriver
import time

username = "yourfbusernameoremail"
password = "yourfbpassword"

driver = webdriver.Chrome('chromedriverpath')

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
#     //group links one by one
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
