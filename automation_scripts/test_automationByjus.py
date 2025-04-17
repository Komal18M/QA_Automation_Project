import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def create_screenshot_folder():
    """Creates a screenshots folder if it doesn't exist."""
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

def take_screenshot(driver, filename):
    """Takes a screenshot with timestamp and saves in the screenshots folder."""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    full_path = f"screenshots/{filename}_{timestamp}.png"
    driver.save_screenshot(full_path)
    print(f"📸 Screenshot saved: {full_path}")

def test_homepage_login():
    print("🚀 Testing Homepage and Login Button Visibility...\n")

    create_screenshot_folder()  # Ensure screenshots folder exists

    # Setup Chrome driver with options
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('--ignore-certificate-errors')  # ✅ Ignore SSL errors
    options.add_argument('--allow-running-insecure-content')  # ✅ Allow mixed content

    # Initialize Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Step 1: Navigate to Byju's website
        driver.get("https://byjus.com/")
        time.sleep(3)  # Wait for page to load

        # Step 2: Validate the page title
        expected_title = "BYJU'S Online learning Programs For K3, K10, K12, NEET, JEE, UPSC & Bank Exams"
        actual_title = driver.title
        print(f"ℹ️ Page title: {actual_title}")
        assert expected_title in actual_title, "Title does not match expected content"
        print("✅ Homepage title verified!")
        take_screenshot(driver, "homepage_loaded")

        # Step 3: Check login button visibility
        login_button = driver.find_element(By.XPATH, '//*[@id="top-navbar-collapse"]/ul/li[8]/a')
        assert login_button.is_displayed(), "Login button is not visible"
        print("✅ Login button is visible!")
        take_screenshot(driver, "login_button_visible")

    except AssertionError as ae:
        print("❌ Assertion failed:", ae)
        take_screenshot(driver, "assertion_failed")

    except Exception as e:
        print("❌ An unexpected error occurred:", e)
        take_screenshot(driver, "unexpected_error")

    finally:
        driver.quit()
        print("\n🧪 Test completed.")

# Run the test
if __name__ == "__main__":
    test_homepage_login()







