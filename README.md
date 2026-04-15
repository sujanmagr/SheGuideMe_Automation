# SheGuidesMe - Playwright Test Suite

Automated end-to-end tests for [sheguidesme.com](https://sheguidesme.com) using Playwright + pytest with Page Object Model (POM).

## Project Structure

```
sheguideme/
├── pages/
│   ├── login_page.py      # Login actions
│   ├── home_page.py       # Home feed actions
│   └── post_page.py       # Post creation actions
├── tests/
│   ├── test_login.py      # Login test
│   └── test_post.py       # Post creation test
├── conftest.py            # Loads .env before tests
├── .env                   # ⚠️ NOT pushed to GitHub (your real credentials)
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/sheguideme.git
cd sheguideme
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 3. Configure credentials
in .env file
```
Open `.env` and fill in your real credentials:
```
TEST_EMAIL=your_real_email@example.com
TEST_PASSWORD=your_real_password
BASE_URL=https://sheguidesme.com/
```

### 4. Run the tests
```bash
# Run all tests
pytest tests/

# Run a specific test
pytest tests/test_login.py
pytest tests/test_post.py

# Run headed (see the browser)
pytest tests/ --headed
```
