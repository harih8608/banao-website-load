import unittest
from selenium import webdriver

class WebsiteLoadingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    def test_website_loading(self):
        print("Starting website loading test.")
        self.driver.get("https://atg.world")
        print("Connected to atg.world website.")

        page_title = self.driver.title
        print(f"Page title: {page_title}")

        # Perform additional checks/assertions if needed
        # For example, you can check if certain elements exist on the page

        expected_title = "Across The Globe (ATG) - Professional and Personal Social Networking"
        self.assertEqual(page_title, expected_title)

        print("Website loaded successfully.")

    def tearDown(self):
        self.driver.quit()
        print("Website loading test completed.")

if __name__ == '__main__':
    unittest.main()
