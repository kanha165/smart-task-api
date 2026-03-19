def get_priority(text: str):
    text = text.lower()

    if "urgent" in text:
        return "High"
    elif "important" in text:
        return "Medium"
    else:
        return "Low"