# Copilot AI Interaction Log

**Date:** 2026-11-22
**Tool:** Copilot SDK assistant in VS Code
**Repository:** <https://github.com/youneskouisaz-dot/egn475-cafe-kouis>

## Actual assistance performed

1. Reviewed the repository state, relevant source files, Git differences, ignore rules, live SQLite database, and Week 4 draft documents.
2. Verified the live SQLite totals at the start of verification as 3 users, 11 menu items, 3 orders, and 6 order items. The live menu then contained the clearly labeled records `W4 Submission Verification A - Nov 22` (ID 10, 137 cents) and `W4 Submission Verification B - Nov 22` (ID 11, 249 cents).
3. Used local HTTP requests to verify `GET /menu`, `GET /menu/1`, and `GET /admin/menu/new` return the live database content and form. No existing record was modified during these checks.
4. Verified `GET /menu/999` returned HTTP 404 and a whitespace-only name submitted to `POST /admin/menu/new` returned HTTP 400.
5. Restarted the Flask development server and confirmed that menu item IDs 10 and 11 remained accessible from `/menu/10` and `/menu/11`. Final live counts observed during the restart check were 3 users, 12 menu items, 3 orders, and 6 order items; the extra live menu record was not created or removed by this current verification.
6. Ran `python -m unittest discover -s tests -v`: 22 tests ran and passed.
7. Confirmed `git check-ignore -v` identifies `instance/`, `*.sqlite`, and `*.backup` patterns. No database or backup file was staged.
8. Prepared and reviewed this assignment-answer and screenshot-checklist documentation.

## Actual work not performed

- No browser or screenshot test was performed.
- No live database record was deleted.
- No `init-db`, table reset, or database migration was run during this verification session.
- No live database direct-SQL insertion was used for the verification-item form records. Their presence was observed, but their original form submission is not newly claimed as a Copilot tool action in this session.

## Student responsibility

The student should review and personalize the assignment answers, disclose AI assistance according to course policy, and capture only their own authentic screenshot evidence.
