import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
pyautogui.PAUSE = 2
driver = webdriver.Firefox()
driver.get("https://yopmail.com/en/")
#trohixikixi-8575@yopmail.com
#migribessabrou-3094@yopmail.com
search = driver.find_element_by_class_name('ycptinput').send_keys('trohixikixi-8575@yopmail.com')
search = driver.find_element_by_class_name('ycptinput').send_keys(Keys.RETURN)
time.sleep(3)

click = driver.find_element_by_id('newmail')
click.click()
time.sleep(3)

pyautogui.click(x=812, y=378)
pyautogui.write("migribessabrou-3094@yopmail.com")
pyautogui.click(x=671, y=410)
pyautogui.write("Assunto importante!")
pyautogui.click(x=871, y=665)
pyautogui.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet facilisis magna etiam tempor orci. Felis eget nunc lobortis mattis aliquam faucibus purus. Id diam vel quam elementum pulvinar etiam non. Id cursus metus aliquam eleifend mi in nulla posuere. Purus semper eget duis at tellus at urna. Mauris a diam maecenas sed enim ut sem viverra aliquet. Erat nam at lectus urna duis convallis convallis tellus id. Donec ac odio tempor orci dapibus ultrices. In cursus turpis massa tincidunt dui ut ornare lectus. Id aliquet lectus proin nibh. Cras tincidunt lobortis feugiat vivamus at augue eget arcu. Consectetur lorem donec massa sapien faucibus et molestie. Nec ultrices dui sapien eget mi proin. Eu facilisis sed odio morbi quis commodo odio. Cras semper auctor neque vitae tempus. Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula. Lorem sed risus ultricies tristique nulla aliquet. Tellus orci ac auctor augue mauris augue neque gravida. Dolor magna eget est lorem ipsum dolor sit amet consectetur.")
pyautogui.click(x=582, y=880)
time.sleep(3)

home = driver.find_element_by_tag_name('a')
home.click()
time.sleep(3)

search1 = driver.find_element_by_class_name('ycptinput').clear()
search1 = driver.find_element_by_class_name('ycptinput').send_keys('migribessabrou-3094@yopmail.com')
search1 = driver.find_element_by_class_name('ycptinput').send_keys(Keys.RETURN)
time.sleep(3)

click1 = driver.find_element_by_id('newmail')
click1.click()
time.sleep(3)

pyautogui.click(x=812, y=378)
pyautogui.write("trohixikixi-8575@yopmail.com")
pyautogui.click(x=671, y=410)
pyautogui.write("Email de aviso - noreply")
pyautogui.click(x=871, y=665)
pyautogui.write("Email recebido com sucesso!")
pyautogui.click(x=582, y=880)
time.sleep(3)

home1 = driver.find_element_by_tag_name('a')
home1.click()
time.sleep(3)

search2 = driver.find_element_by_class_name('ycptinput').clear()
search2 = driver.find_element_by_class_name('ycptinput').send_keys('trohixikixi-8575@yopmail.com')
search2 = driver.find_element_by_class_name('ycptinput').send_keys(Keys.RETURN)
time.sleep(3)