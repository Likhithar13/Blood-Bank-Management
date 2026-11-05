# Module D – System and acceptance testing

## Test cases
| Test | Action | Expected result |
|---|---|---|
| T1 | Open dashboard | Dashboard loads |
| T2 | Register valid donor | Donor is saved and listed |
| T3 | Register donor under 18 | Validation error |
| T4 | Add stock | Inventory record appears |
| T5 | Request within recorded stock | Demo status says stock recorded as available – verification required |
| T6 | Request above recorded stock | Demo status says insufficient recorded stock |

Run unit tests:
```bash
python manage.py test
```

## Selenium browser test
Install a compatible browser and driver, start the Django server, then run:
```bash
python manage.py runserver
```
In a second terminal:
```bash
python selenium_test.py
```
