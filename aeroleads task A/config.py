"""
Configuration file for LinkedIn Scraper
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LinkedIn Credentials (TEST ACCOUNT ONLY)
LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL', '')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD', '')

# Scraping Configuration
MAX_PROFILES = int(os.getenv('MAX_PROFILES', 20))
DELAY_BETWEEN_PROFILES = int(os.getenv('DELAY_BETWEEN_PROFILES', 5))
PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', 10))

# Output Configuration
OUTPUT_CSV = 'linkedin_profiles.csv'
PROFILE_URLS_FILE = 'profile_urls.txt'

# Anti-blocking Configuration
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
]

# Selenium Configuration
HEADLESS_MODE = False  # Set to True to hide browser window
IMPLICIT_WAIT = 10  # seconds

# LinkedIn Selectors (may need updating if LinkedIn changes their HTML)
SELECTORS = {
    'name': 'h1.text-heading-xlarge',
    'headline': 'div.text-body-medium.break-words',
    'location': 'span.text-body-small.inline',
    'experience_section': 'section[data-section="experience"]',
    'education_section': 'section[data-section="educationsDetails"]',
    'skills_section': 'section[data-section="skillsDetails"]',
}
