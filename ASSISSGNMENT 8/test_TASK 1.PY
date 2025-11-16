from pathlib import Path
import pytest

import importlib.util

# Load the implementation file by path (handles filename with space)
HERE = Path(__file__).parent
impl_path = HERE / "TASK 1.PY"

spec = importlib.util.spec_from_file_location("task1_module", str(impl_path))
task1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task1)

is_valid_email = task1.is_valid_email

@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "USER@EXAMPLE.COM",
        "user.name+tag+sorting@example.com",
        "user_name@example.co.uk",
        "user-name@sub.example.org",
        "u@a.io",
        "local.part.with.dots@sub-domain.example.com",
        "firstname.lastname@example.com",
        "1234567890@example.com",
        "!#$%&'*+-/=?^_`{}|~@example.org",
    ],
)
def test_valid_emails(email):
    assert is_valid_email(email) is True

@pytest.mark.parametrize(
    "email",
    [
        "",
        None,
        12345,
        "plainaddress",
        "missingatsign.com",
        "two@@example.com",
        ".local@domain.com",
        "local.@domain.com",
        "local..dots@domain.com",
        "local@-example.com",
        "local@example-.com",
        "local@example.c",
        "local@example.123",
        "local@.example.com",
        "local@exam_ple.com",
        "a" * 300 + "@example.com",
    ],
)
def test_invalid_emails(email):
    assert is_valid_email(email) is False

def test_whitespace_stripping():
    assert is_valid_email(" user@example.com ") is True