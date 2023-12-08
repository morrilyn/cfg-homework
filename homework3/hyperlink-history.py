from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Base and other URLs
base_url = 'https://codefirstgirls.com/'
urls = {'1': base_url + 'courses',
        '2': base_url + 'opportunities',
        '3': base_url + 'courses/cfgdegree',
        '4': base_url + 'opportunities/ambassadors'}

def navigate_and_display_options(current_url):
    # Print current URL
    print(f"Current URL: {current_url}")

    # Display navigation options
    print("Options:")
    for key, url in urls.items():
        print(f"{key}: Go to {url}")
    if current_url != base_url:
        print("Back: Go back to the previous page")

    # Get user choice
    choice = input("Enter your choice: ")
    return choice

def navigate_to(choice):
    if choice in urls:
        driver.get(urls[choice])
    elif choice.lower() == 'back':
        driver.back()

try:
    driver.get(base_url)
    while True:
        user_choice = navigate_and_display_options(driver.current_url)
        navigate_to(user_choice)

except KeyboardInterrupt:
    print("\nExiting the program.")
finally:
    driver.quit()


"""The script starts at the base URL
It displays options for navigation
The user inputs their choice to navigate to a different URL or go back
The script performs the navigation based on the user's input
This loop continues until the user forces an exit (e.g., by pressing Ctrl+Z)"""


# What is the time and space complexity of your solution?If you are making any assumptions, list them.

"""Time Complexity: Each iteration (user action) of the script is \( O(1) \), meaning it takes a constant amount of time regardless of the number of URLs. However, the total time is dependent on user interactions since the script runs in an indefinite loop.

Space Complexity: The space complexity is \( O(1) \) as the script uses a constant amount of memory, only storing a fixed number of URLs and user inputs, regardless of how long it runs."""