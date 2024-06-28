import pywhatkit as kit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def send_whatsapp_message(message):
    # Replace with the recipient's phone number
    recipient = "+85255445781"

    # Schedule message using pywhatkit
    kit.sendwhatmsg_instantly(recipient, message)

    # Delay to allow time for WhatsApp Web to load and message to be typed
    time.sleep(5)  # Adjust as needed based on your system speed and internet connection

    # Initialize Firefox WebDriver with Selenium
    driver = webdriver.Firefox()

    try:
        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com/")

        # Wait for WhatsApp Web to fully load
        time.sleep(10)

        # Locate the message input field
        message_box = driver.find_element_by_css_selector("._ak1l > div:nth-child(1) > div:nth-child(1) > p:nth-child(1)")

        # Enter the message into the input field
        message_box.send_keys('testing')
        
        # Send the message by hitting Enter key
        message_box.send_keys(Keys.ENTER)

        message_box.send_keys('testing')
        
        # Send the message by hitting Enter key
        message_box.send_keys(Keys.ENTER)

        print(f"Message sent successfully to {recipient}")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        # Close the browser session
        driver.quit()






with open('cybersecuity.report.txt', 'r', encoding='utf-8') as file:
    file_content = file.read()

# Split the file content based on the separator
job_listings = file_content.split('----------------------------------------\n')

# Process each job listing
for job in job_listings:
    # Prepare the message for WhatsApp
    message = job.strip()  # Remove leading/trailing whitespace
    a = f'''


        {message}



    '''
    print(type(a))
    break
    # Send WhatsApp message for each job listing
