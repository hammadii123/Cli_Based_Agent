# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Chrome browser open karo
# driver = webdriver.Chrome()

# # URL open karo jahan form hai
# driver.get("https://demoqa.com/radio-button")

# # Browser window ko maximize karo
# driver.maximize_window()

# # Thori dair ruk jao taake elements load ho jaen
# time.sleep(2)

# # ---------- Positive Test Cases ----------

# # YES radio button click karo
# yes_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
# yes_button.click()
# print("✅ YES button test pass hogaya")

# time.sleep(1)

# # IMPRESSIVE radio button click karo
# impressive_button = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
# impressive_button.click()
# print("✅ IMPRESSIVE button test pass hogaya")

# # ---------- Negative Test Case (NO button is disabled) ----------

# no_button = driver.find_element(By.ID, "noRadio")

# # Check karo ke NO button enabled hai ya nahi
# if no_button.is_enabled():
#     no_button.click()
#     print("❌ NO button click hogaya (ye galat hai)")
# else:
#     print("✅ NO button disabled hai, test pass hogaya")

# # Test complete, ab browser close karo
# time.sleep(2)
# driver.quit()
