from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage:
    """Page Object Model for Login Page."""
    
    # Locators for SauceDemo
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    
    def __init__(self, driver):
        """
        Initialize LoginPage.
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate(self, url="https://yourapp.com/login"):
        """
        Navigate to the login page.
        
        Args:
            url: Login page URL
        """
        logger.info(f"Navigating to {url}")
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
    
    def enter_username(self, username):
        """
        Enter username into username field.
        
        Args:
            username: Username to enter
        """
        logger.info(f"Entering username: {username}")
        element = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)
    
    def enter_password(self, password):
        """
        Enter password into password field.
        
        Args:
            password: Password to enter
        """
        logger.info("Entering password")
        element = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)
    
    def click_login(self):
        """Click the login button."""
        logger.info("Clicking login button")
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()
    
    def login(self, username, password):
        """
        Perform complete login action.
        
        Args:
            username: Username
            password: Password
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def verify_successful_login(self, expected_url_part="inventory.html"):
        """
        Verify that login was successful by checking URL or page element.
        
        Args:
            expected_url_part: A unique part of the URL expected after successful login.
            
        Returns:
            bool: True if login successful
        """
        logger.info("Verifying successful login")
        try:
            # Wait until the inventory container is visible (unique to SauceDemo)
            self.wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
            
            # Optional: also validate the URL contains expected part
            current_url = self.driver.current_url
            if expected_url_part not in current_url:
                raise AssertionError(f"Unexpected URL after login: {current_url}")
            
            logger.info(f"✓ Login successful. Current URL: {current_url}")
            return True
        except Exception as e:
            logger.error(f"❌ Login verification failed: {str(e)}")
            raise

    
    def verify_login_failure(self, expected_error):
        """
        Verify that login failed with expected error message.
        
        Args:
            expected_error: Expected error message
            
        Returns:
            bool: True if error message matches
        """
        logger.info("Verifying login failure")
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located(self.ERROR_MESSAGE)
            )
            actual_error = error_element.text
            
            if expected_error in actual_error:
                logger.info(f"Error message verified: {actual_error}")
                return True
            else:
                raise AssertionError(
                    f"Expected error '{expected_error}' but got '{actual_error}'"
                )
        except Exception as e:
            logger.error(f"Error verification failed: {str(e)}")
            raise
    
    def is_password_field_masked(self):
        """
        Check if password field is properly masked.
        
        Returns:
            bool: True if password field type is 'password'
        """
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        field_type = password_field.get_attribute("type")
        return field_type == "password"
    
    def are_all_elements_present(self):
        """
        Verify all login form elements are present.
        
        Returns:
            bool: True if all elements are present
        """
        try:
            self.driver.find_element(*self.USERNAME_INPUT)
            self.driver.find_element(*self.PASSWORD_INPUT)
            self.driver.find_element(*self.LOGIN_BUTTON)
            logger.info("All form elements are present")
            return True
        except Exception as e:
            logger.error(f"Missing form elements: {str(e)}")
            return False