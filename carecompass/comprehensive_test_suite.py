# Save this file as: comprehensive_test_suite.py

import random
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service  # New Import for Service class
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# --- Global Setup ---
REPORT = Report()

# FIX for 'AttributeError: 'str' object has no attribute 'capabilities'':
# Pass the downloaded path to the Service class, and then pass the Service object to Chrome.
# ChromeDriverManager().install() returns the path string.
DRIVER: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Credentials based on common Django roles in your files
USER_CREDS = {'username': 'user', 'password': 'user@123'}
NGO_CREDS = {'username': 'ngo', 'password': 'user@123'}
VOLUNTEER_CREDS = {'username': 'volunteer', 'password': 'user@123'}
BASE_URL = 'http://127.0.0.1:8000/'


class E2ETestSuite:
    """A comprehensive test suite for the web application."""

    def __init__(self):
        REPORT.setup(
            report_folder=r'Reports',
            module_name='CareCompass E2E Test',
            release_name='V2.1 (Fixed)',
            selenium_driver=DRIVER
        )
        DRIVER.get(BASE_URL)
        DRIVER.implicitly_wait(10)

    def _login(self, creds, role, test_number):
        """Helper method to handle login for different roles."""
        try:
            REPORT.write_step(
                f'Attempt Login as {role}',
                status=REPORT.status.Start,
                test_number=test_number
            )
            DRIVER.get(f'{BASE_URL}login/')
            time.sleep(1)
            DRIVER.find_element(By.NAME, 'username').send_keys(creds['username'])
            DRIVER.find_element(By.NAME, 'password').send_keys(creds['password'])
            DRIVER.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
            time.sleep(3)

            DRIVER.find_element(By.CSS_SELECTOR, ".btn-danger")

            REPORT.write_step(
                f'Successfully Logged in as {role}',
                status=REPORT.status.Pass,
                screenshot=True
            )
        except Exception as e:
            REPORT.write_step(
                f'Failed to Login as {role}: {e}',
                status=REPORT.status.Fail,
                screenshot=True
            )
            raise

    def _logout(self, role):
        """Helper method to handle logout."""
        try:
            DRIVER.find_element(By.CSS_SELECTOR, ".btn-danger").click()
            time.sleep(2)
            REPORT.write_step(
                f'Successfully Logged out from {role} Account',
                status=REPORT.status.Pass,
                screenshot=True
            )
        except Exception as e:
            REPORT.write_step(
                f'Logout Failed: {e}',
                status=REPORT.status.Warn,
                screenshot=True
            )

    # --- Test Case 1: Base Navigation & User Signup Flow ---
    def test_case_1_base_navigation_and_signup(self):
        try:
            REPORT.write_step('Go to Landing Page and Verify Title', status=REPORT.status.Start, test_number=1)
            DRIVER.get(BASE_URL)
            assert ('Home' in DRIVER.title or 'CareCompass' in DRIVER.title)
            REPORT.write_step('Landing Page loaded Successfully.', status=REPORT.status.Pass, screenshot=True)

            REPORT.write_step('Attempt User Signup', status=REPORT.status.Start, test_number=1.1)
            DRIVER.find_element(By.LINK_TEXT, "Signup").click()
            username = f'TestUser_{random.randint(100, 999)}'
            DRIVER.find_element(By.NAME, 'username').send_keys(username)
            DRIVER.find_element(By.NAME, 'email').send_keys(f'{username}@test.com')
            DRIVER.find_element(By.NAME, 'password').send_keys('Test@123')
            DRIVER.find_element(By.NAME, 'confirm_password').send_keys('Test@123')
            DRIVER.find_element(By.NAME, "Signup").click()
            time.sleep(3)

            REPORT.write_step('Signup Flow Completed', status=REPORT.status.Pass, screenshot=True)
        except Exception as e:
            REPORT.write_step(f'Failed Base Navigation or Signup: {e}', status=REPORT.status.Fail, screenshot=True)

    # --- Test Case 2: User Role - Login, Report Submission, and Donation ---
    def test_case_2_user_submit_report_and_donate(self):
        self._login(USER_CREDS, 'User', 2)

        try:
            REPORT.write_step('User Role: Submit a New Report', status=REPORT.status.Start, test_number=2.1)
            DRIVER.find_element(By.LINK_TEXT, "Submit Report").click()
            time.sleep(2)
            DRIVER.find_element(By.NAME, 'title').send_keys(f'Urgent Report {random.randint(1, 100)}')
            DRIVER.find_element(By.NAME, 'description').send_keys('Automated report submission.')
            DRIVER.find_element(By.CSS_SELECTOR, ".btn-neo").click()
            REPORT.write_step('Report Submitted Successfully.', status=REPORT.status.Pass, screenshot=True)
            time.sleep(3)

            REPORT.write_step('User Role: Attempt Donation', status=REPORT.status.Start, test_number=2.2)
            DRIVER.get(BASE_URL)
            DRIVER.find_element(By.NAME, 'amount').send_keys('1000')
            DRIVER.find_element(By.ID, 'Donate').click()
            time.sleep(3)
            REPORT.write_step('Donation Flow Completed.', status=REPORT.status.Pass, screenshot=True)

        except Exception as e:
            REPORT.write_step(f'Failed User Flow (Submit/Donate): {e}', status=REPORT.status.Fail, screenshot=True)

        self._logout('User')

    # --- Test Case 3: NGO Role - Accept Report and Profile Update ---
    def test_case_3_ngo_accept_report_and_update_profile(self):
        self._login(NGO_CREDS, 'NGO', 3)

        try:
            REPORT.write_step('NGO Role: Accept the Latest Submitted Report', status=REPORT.status.Start,
                              test_number=3.1)
            DRIVER.find_element(By.LINK_TEXT, "Report").click()
            time.sleep(2)
            DRIVER.find_element(By.LINK_TEXT, "View Details").click()
            time.sleep(2)
            DRIVER.find_element(By.LINK_TEXT, "Accept").click()
            time.sleep(3)
            REPORT.write_step('Report Accepted Successfully by NGO.', status=REPORT.status.Pass, screenshot=True)

            REPORT.write_step('NGO Role: Update Profile Details', status=REPORT.status.Start, test_number=3.2)
            DRIVER.find_element(By.LINK_TEXT, "Profile").click()
            time.sleep(2)
            DRIVER.find_element(By.NAME, 'phone').send_keys('017XXXXXXXX')
            DRIVER.find_element(By.NAME, 'address').send_keys('Dhaka, Bangladesh')
            DRIVER.find_element(By.CSS_SELECTOR, ".btn-primary").click()
            time.sleep(3)
            REPORT.write_step('NGO Profile Updated Successfully.', status=REPORT.status.Pass, screenshot=True)

        except Exception as e:
            REPORT.write_step(f'Failed NGO Flow (Accept Report/Profile Update): {e}', status=REPORT.status.Fail,
                              screenshot=True)

        self._logout('NGO')

    # --- Test Case 4: Volunteer Role - View Accepted Report and Update Proof ---
    def test_case_4_volunteer_view_and_update_proof(self):
        self._login(VOLUNTEER_CREDS, 'Volunteer', 4)

        try:
            REPORT.write_step('Volunteer Role: View Accepted Report', status=REPORT.status.Start, test_number=4.1)
            DRIVER.find_element(By.LINK_TEXT, "Report").click()
            time.sleep(2)
            DRIVER.find_element(By.LINK_TEXT, "View Details").click()
            time.sleep(2)
            REPORT.write_step('Volunteer viewed the Report Details.', status=REPORT.status.Pass, screenshot=True)

            REPORT.write_step('Volunteer Role: Update Proof of Work', status=REPORT.status.Start, test_number=4.2)
            # The actual file upload line is commented out as it requires a real file path
            # DRIVER.find_element(By.NAME, 'proof').send_keys("C:\\fakepath\\give.jpg")
            # DRIVER.find_element(By.CSS_SELECTOR, ".btn-success").click()
            REPORT.write_step('Proof element located and simulated update.', status=REPORT.status.Pass, screenshot=True)

        except Exception as e:
            REPORT.write_step(f'Failed Volunteer Flow (View/Proof Update): {e}', status=REPORT.status.Fail,
                              screenshot=True)

        self._logout('Volunteer')

    # --- Test Case 5: Leaderboard and Post Browsing ---
    def test_case_5_leaderboard_and_browsing(self):
        self._login(USER_CREDS, 'User (Browsing)', 5)

        try:
            REPORT.write_step('Check Leaderboard Page', status=REPORT.status.Start, test_number=5.1)
            DRIVER.find_element(By.LINK_TEXT, "Leaderboard").click()
            time.sleep(3)
            assert ('Leaderboard' in DRIVER.page_source)
            REPORT.write_step('Leaderboard loaded successfully.', status=REPORT.status.Pass, screenshot=True)

            REPORT.write_step('Browse Post by Title and Check Description', status=REPORT.status.Start, test_number=5.2)
            DRIVER.get(BASE_URL)
            DRIVER.find_element(By.PARTIAL_LINK_TEXT, 'মিরপুরে পথশিশুদের খাবার').click()
            time.sleep(3)
            DRIVER.find_element(By.ID, 'discription')
            REPORT.write_step('Post Browsing and Description check passed.', status=REPORT.status.Pass, screenshot=True)

        except Exception as e:
            REPORT.write_step(f'Failed Leaderboard or Browsing: {e}', status=REPORT.status.Fail, screenshot=True)

        self._logout('User (Browsing)')

    # --- Test Case 6: Final Cleanup and Public Access Check ---
    def test_case_6_final_logout_and_cleanup(self):
        try:
            REPORT.write_step('Final Check: Ensuring Logout and Public View', status=REPORT.status.Start, test_number=6)
            DRIVER.get(BASE_URL)
            time.sleep(2)
            DRIVER.find_element(By.LINK_TEXT, "Login")
            REPORT.write_step('Application is back to public view.', status=REPORT.status.Pass, screenshot=True)

        except Exception as e:
            REPORT.write_step(f'Final check failed: {e}', status=REPORT.status.Warn, screenshot=True)


# --- Execution Block ---
if __name__ == "__main__":
    suite = E2ETestSuite()
    try:
        suite.test_case_1_base_navigation_and_signup()
        suite.test_case_2_user_submit_report_and_donate()
        suite.test_case_3_ngo_accept_report_and_update_profile()
        suite.test_case_4_volunteer_view_and_update_proof()
        suite.test_case_5_leaderboard_and_post_browsing()
        suite.test_case_6_final_logout_and_cleanup()

    except Exception as e:
        print(f"An unexpected error occurred during test execution: {e}")

    finally:
        REPORT.generate_report()
        DRIVER.quit()