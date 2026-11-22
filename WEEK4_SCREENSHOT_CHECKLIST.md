# Week 4 Screenshot Checklist

These are screenshots to capture in a real browser or terminal before submission. No Week 4 screenshots or browser visual tests were captured during verification; route checks used Flask's test client and local HTTP requests.

- [ ] `week4-01-menu-live.png` — `/menu`, with the two clearly labeled Week 4 verification items and their prices visible.
- [ ] `week4-02-item-detail.png` — `/menu/1`, showing the database-backed item name, description, icon, and price.
- [ ] `week4-03-staff-form.png` — `/admin/menu/new`, showing the form fields and the navigation link.
- [ ] `week4-04-form-save.png` — submit a clearly labeled item and show the redirect to `/menu` with the saved name and price.
- [ ] `week4-05-empty-name-validation.png` — submit a blank or whitespace-only name and show the validation message.
- [ ] `week4-06-missing-item.png` — `/menu/999`, showing the not-found response.
- [ ] `week4-07-test-results.png` — terminal output from `python -m unittest discover -s tests -v` showing success.
- [ ] `week4-08-gitignore.png` — terminal output confirming `instance/`, SQLite files, and backup patterns are ignored.

Keep the browser address bar or terminal command visible where useful. Do not expose credentials, environment variables, or database/backup contents in screenshots. The staff form is currently unauthenticated; capture it only in the local educational environment.
