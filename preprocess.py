import re


def clean_text(text):
    """Clean and normalize text for semantic matching."""
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s.,+#-]", "", text)
    return text.strip()
