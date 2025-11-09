def format_name(first_name, last_name):
    """
    Format a full name as "Last, First".
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name and last_name must be strings")
    first = first_name.strip()
    last = last_name.strip()
    if not first or not last:
        raise ValueError("first_name and last_name cannot be empty")
    return f"{last}, {first}"

if __name__ == "__main__":
    # Examples
    print(format_name("SUSANNA", "JASMINE"))        # JASMINE, SUSANNA
    print(format_name("  TEENA  ", "LILLY")) # LILLY, TEENA