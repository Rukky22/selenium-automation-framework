import pytest
from src.utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.login
class TestLoginFunctionality:
    """Test suite for login functionality."""
    
    def test_successful_login_standard_user(self, login_page, test_data):
        """Test successful login with standard user."""
        user_data = test_data['validUsers'][0]  # standard_user
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        logger.info(f"Username: {user_data['username']}, Role: {user_data['role']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_successful_login()
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")
    
    def test_successful_login_problem_user(self, login_page, test_data):
        """Test successful login with problem user."""
        user_data = test_data['validUsers'][1]  # problem_user
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        logger.info(f"Username: {user_data['username']}, Role: {user_data['role']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_successful_login()
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")
    
    def test_successful_login_performance_user(self, login_page, test_data):
        """Test successful login with performance glitch user."""
        user_data = test_data['validUsers'][2]  # performance_glitch_user
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        logger.info(f"Username: {user_data['username']}, Role: {user_data['role']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_successful_login()
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")
    
    def test_failed_login_locked_user(self, login_page, test_data):
        """Test failed login with locked out user."""
        user_data = test_data['invalidUsers'][0]  # locked_out_user
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        logger.info(f"Testing with: {user_data['username']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_login_failure(user_data['expectedError'])
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")
    
    def test_failed_login_invalid_username(self, login_page, test_data):
        """Test failed login with invalid username."""
        user_data = test_data['invalidUsers'][1]  # invalid_user
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        logger.info(f"Testing with: {user_data['username']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_login_failure(user_data['expectedError'])
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")
    
    def test_failed_login_invalid_password(self, login_page, test_data):
        """Test failed login with invalid password."""
        user_data = test_data['invalidUsers'][2]  # wrong password
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        logger.info(f"Testing with: {user_data['username']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_login_failure(user_data['expectedError'])
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")
    
    def test_failed_login_empty_username(self, login_page, test_data):
        """Test failed login with empty username."""
        user_data = test_data['invalidUsers'][3]  # empty username
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_login_failure(user_data['expectedError'])
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")
    
    def test_failed_login_empty_password(self, login_page, test_data):
        """Test failed login with empty password."""
        user_data = test_data['invalidUsers'][4]  # empty password
        
        logger.info(f"Starting test: {user_data['testCaseId']}")
        
        login_page.login(user_data['username'], user_data['password'])
        login_page.verify_login_failure(user_data['expectedError'])
        
        logger.info(f"✓ Test passed: {user_data['testCaseId']}")


@pytest.mark.login
class TestLoginPageValidations:
    """Test suite for login page element validations."""
    
    def test_password_field_is_masked(self, login_page):
        """Verify password field is properly masked."""
        assert login_page.is_password_field_masked(), "Password field should be masked"
        logger.info("✓ Password field is properly masked")
    
    def test_all_form_elements_present(self, login_page):
        """Verify all login form elements are present."""
        assert login_page.are_all_elements_present(), "Not all form elements are present"
        logger.info("✓ All form elements are present")