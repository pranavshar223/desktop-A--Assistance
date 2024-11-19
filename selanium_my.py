from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setup
driver = webdriver.Chrome(executable_path='path_to_chromedriver')
driver.get("https://chat.openai.com/")

# Wait for page to load
time.sleep(5)

# Find the input area by inspecting the element and using the appropriate selector
input_area = driver.find_element_by_tag_name("textarea")  # Example using tag name; adjust if needed

# Enter the query
query = "What's the weather like today?"
input_area.send_keys(query)
input_area.send_keys(Keys.RETURN)

# Wait for the response
time.sleep(10)  # Adjust based on how long it takes to get a response

# Get the response
response_div = driver.find_element_by_class_name("response_class_name")  # Replace with actual class name
response_text = response_div.text
print(response_text)

# Clean up
driver.quit()
