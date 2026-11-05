# Blood Bank Management System – Case Study 38

Educational Django implementation for Modules A–E.

## Requirements
- Python 3.10 or newer
- VS Code (recommended)
- Internet connection for installing packages

## Windows setup
Open a terminal in this folder and run:

```powershell
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py makemigrations management
py manage.py migrate
py manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Suggested demonstration
1. Dashboard opens.
2. Register a fictional donor.
3. Add/update a fictional stock count.
4. Create a demo emergency request.
5. Review the request status and take screenshots.
6. Run tests with `py manage.py test`.

## Selenium
With the server running in one terminal, open another terminal:
```powershell
venv\Scripts\activate
py selenium_test.py
```
A compatible Chrome browser is required.

## Modules
- Module A: `docs/MODULE_A_WATERFALL.md`
- Module B: `docs/MODULE_B_SCRUM.md`
- Module C: `docs/MODULE_C_DEVOPS.md`, `Jenkinsfile`, `Dockerfile`
- Module D: `docs/MODULE_D_TESTING.md`, `management/tests.py`, `selenium_test.py`
- Module E: `docs/MODULE_E_QUALITY_ETHICS.md`, `sonar-project.properties`

## Important safety note
This is a classroom prototype using fictional records. It is not suitable for real donor management, clinical compatibility checking, blood screening, cross-matching, stock release or medical decisions. A qualified blood-bank professional must verify all real-world decisions.
