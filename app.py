from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import subprocess

# Create a Chrome WebDriver instance
options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress','localhost:9220')
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/upload")

file_path = "./day.txt"
day_file = open(file_path, "r+")
day = day_file.read()
print(day)
day_file.close()

new_value = int(day) + 1
if os.path.exists(file_path):
    os.remove(file_path)
    
with open(file_path, "w") as file:
    file.write(str(new_value))



title = "Daily Andrew Tate workout Day: " + day
video_description = title + "#andrew #workout #trending"


publish = driver.find_element("xpath", "//ytcp-button[@id='select-files-button']/div[@class='label style-scope ytcp-button']")
publish.click()
time.sleep(3)
# Compile and run the AutoIt script
autoit_script_path = "./autoit/yt_upload.au3"  # Path to your AutoIt script
subprocess.run(["./autoit/yt_upload.exe", autoit_script_path])

time.sleep(5)
video_title = driver.find_element('xpath', "/html//div[@id='textbox']")
video_title.clear()
video_title.send_keys(title)

description_input = driver.find_element("xpath", "//ytcp-social-suggestions-textbox[@id='description-textarea']/ytcp-form-input-container[@id='container']//ytcp-social-suggestion-input[@id='input']/div[@id='textbox']")
description_input.send_keys(video_description)

age_button = driver.find_element('xpath', "//div[@id='audience']//div[@class='made-for-kids-rating-container style-scope ytkc-made-for-kids-select']/tp-yt-paper-radio-group[@role='radiogroup']/tp-yt-paper-radio-button[2]/div[@id='radioContainer']/div[@id='offRadio']")
age_button.click()

next_details = driver.find_element("xpath", "/html//ytcp-button[@id='next-button']")
next_details.click()
time.sleep(3)
next_details.click()
time.sleep(3)

next_checks = driver.find_element("xpath", "//ytcp-button[@id='next-button']/div[@class='label style-scope ytcp-button']")
next_checks.click()

visibility = driver.find_element("xpath", "//tp-yt-paper-radio-group[@id='privacy-radios']/tp-yt-paper-radio-button[3]//div[@id='offRadio']")
visibility.click()

done_button = driver.find_element("xpath", "/html//ytcp-button[@id='done-button']")
done_button.click()


driver.quit()

