import pytest
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from src.utils.driver_factory import DriverFactory
from src.utils.logger import get_logger

# Load environment variables
load_dotenv()

logger = get_logger(__name__)


def pytest_configure(config):
    """Pytest configuration hook."""
    # Create reports directories
    Path("reports/screenshots").mkdir(parents=True, exist_ok=True)
    Path("reports/logs").mkdir(parents=True, exist_ok=True)
    
    logger.info("=" * 60)
    logger.info("Starting Test Suite")
    logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'dev')}")
    logger.info(f"Browser: {os.getenv('BROWSER', 'chrome')}")
    logger.info(f"Headless: {os.getenv('HEADLESS', 'false')}")
    logger.info("=" * 60)


@pytest.fixture(scope="session")
def test_data():
    """
    Load test data from JSON file with absolute path resolution.
    
    Returns:
        dict: Test data
    """
    env_path = os.getenv("TEST_DATA_PATH")
    if env_path and os.path.exists(env_path):
        test_data_path = env_path
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_data_path = os.path.join(base_dir, "data", "test_data.json")
    with open(test_data_path, "r") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def base_url(test_data):
    """
    Get base URL from test data based on environment.
    
    Returns:
        str: Base URL
    """
    environment = os.getenv('ENVIRONMENT', 'dev')
    return test_data['environments'][environment]['url']


@pytest.fixture(scope="function")
def driver():
    """
    Create and provide a WebDriver instance for each test.
    Automatically quits the driver after test completion.
    
    Yields:
        WebDriver: Browser driver instance
    """
    driver_instance = None
    try:
        driver_instance = DriverFactory.create_driver()
        yield driver_instance
    finally:
        if driver_instance:
            DriverFactory.quit_driver(driver_instance)


@pytest.fixture(scope="function")
def login_page(driver, base_url):
    """
    Create and provide a LoginPage instance.
    
    Args:
        driver: WebDriver fixture
        base_url: Base URL fixture
        
    Yields:
        LoginPage: Login page object
    """
    from src.pages.login_page import LoginPage
    
    page = LoginPage(driver)
    page.navigate(base_url)
    
    # Clear cookies before each test
    driver.delete_all_cookies()
    
    yield page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and take screenshots on failure.
    """
    outcome = yield
    report = outcome.get_result()
    
    # Only capture screenshots for test failures
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Generate screenshot filename
            test_name = item.name.replace(" ", "_").replace("[", "_").replace("]", "")
            screenshot_name = f"failed_{test_name}"
            
            # Take screenshot
            screenshot_path = DriverFactory.take_screenshot(driver, screenshot_name)
            
            if screenshot_path:
                logger.error(f"Test failed. Screenshot saved: {screenshot_path}")


def pytest_sessionfinish(session, exitstatus):
    """Hook called after test session finishes."""
    logger.info("=" * 60)
    logger.info("Test Suite Completed")
    logger.info(f"Exit Status: {exitstatus}")
    logger.info("=" * 60)