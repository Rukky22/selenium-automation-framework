# 🧪 Selenium Automation Framework (Pytest + WebDriver Manager)

A scalable, maintainable, and extensible **UI Test Automation Framework** built using **Selenium**, **Pytest**, and **Python**.  
This framework supports cross-browser testing, automatic driver management, detailed HTML reports, and reusable page object design.

---

## 🚀 Features

- ✅ **Pytest-based** for simplicity and scalability
- 🌐 **Cross-browser support** (Chrome, Firefox, Edge)
- ⚙️ **WebDriver Manager** – no need to manually download drivers
- 🧱 **Page Object Model (POM)** architecture
- 🧩 **Custom logging** and test reporting (HTML & log file outputs)
- 🔁 **Automatic test reruns** for flaky tests
- 🧪 Supports **markers**: `smoke`, `regression`, `login`, etc.
- 📦 Ready for **CI/CD integration** (GitHub Actions, Jenkins, GitLab CI)

---

## 🗂 Project Structure

selenium-automation-framework/
│
├── src/
│ ├── pages/ # Page Object files (e.g., LoginPage.py)
│ ├── tests/ # Test scripts (e.g., test_login.py)
│ ├── utils/ # Utility modules (e.g., driver_factory.py)
│ └── conftest.py # Pytest fixtures and hooks
│
├── reports/ # Test reports & logs
│
├── requirements.txt # Project dependencies
├── pytest.ini # Pytest configuration file
├── .gitignore # Files to ignore in Git
└── README.md # Project documentation

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rukky22/selenium-automation-framework.git
cd selenium-automation-framework

2️⃣ Create and Activate Virtual Environment

Windows:

python -m venv .venv
.venv\Scripts\activate


macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🧰 Running Tests
Run all tests:
pytest

Run with detailed report:
pytest --html=reports/test_report.html --self-contained-html

Run smoke or regression suite:
pytest -m smoke
pytest -m regression

Run with reruns for flaky tests:
pytest --reruns 2

🧾 Reporting

After execution, reports are generated in the reports/ folder:

test_report.html → Detailed HTML test report

logs/test.log → Execution logs

You can open the HTML report in any browser.

🌐 Browser Options

By default, tests run in Chrome.
To change browser, pass the --browser option:

pytest --browser firefox
pytest --browser edge


Headless mode:

pytest --browser chrome --headless

🔗 Integration with CI/CD

This framework can be integrated into:

GitHub Actions

Jenkins Pipelines

GitLab CI/CD

Azure DevOps

Example CI step:

- name: Run UI Tests
  run: pytest --html=reports/test_report.html --self-contained-html

🧑‍💻 Contributing

Fork the repository

Create your feature branch (git checkout -b feature/awesome-feature)

Commit changes (git commit -m 'Add awesome feature')

Push to the branch (git push origin feature/awesome-feature)

Open a Pull Request 🚀

🪪 License

This project is licensed under the MIT License
.

❤️ Author

Randolph Rukevwe Oghwe
💼 QA Automation Engineer | SDET
🔗 LinkedIn Profile

🧠 Passionate about quality engineering, automation, and test framework design.


---

Would you like me to include a **badge section** (e.g., Pytest, Selenium, Build passing, Python ve
```
