# CareCompass — "See Someone, Help Someone"
Django-based humanitarian aid coordination platform for Bangladesh.

## Quick Start
```bash
pip install django pillow
python manage.py runserver
```
Open: http://127.0.0.1:8000/

## Test Accounts
| Role      | Username      | Password  |
|-----------|---------------|-----------|
| Admin     | admin         | admin123  |
| User      | testuser      | Test@1234 |
| Volunteer | testvolunteer | Test@1234 |
| NGO       | testngo       | Test@1234 |

## URLs
| Page          | URL                          |
|---------------|------------------------------|
| Home          | /                            |
| Login         | /login/                      |
| Register      | /register/                   |
| Dashboard     | /dashboard/                  |
| Profile       | /profile/                    |
| Submit Report | /report/submit/              |
| All Reports   | /report/list/                |
| Leaderboard   | /leaderboard/                |
| Admin Panel   | /admin/                      |
