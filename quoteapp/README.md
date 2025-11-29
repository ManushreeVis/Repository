# QuoteApp (fix notes)

Fix implemented: the Flask `/quote` route previously returned a Python set like `{quote, author}` which is not JSON serializable.

What I changed:
- Replaced the return with a JSON-serializable dict: `{"quote": quote, "author": author}`.
- Added `fetch_random_quote()` helper with error handling.
- Added unit tests in `tests/test_app.py` that mock `requests.get` and verify success and failure flows.

How to run tests:

1. From the project root, install pytest (if needed):

```bash
pip install pytest
```

2. Run tests:

```bash
pytest quoteapp/tests -q
```
