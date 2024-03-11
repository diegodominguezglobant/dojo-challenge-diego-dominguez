import re


def find_dates_within_text(text):
    pat = [
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b',  # Month DD, YYYY
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}(?:st|nd|rd|th)?,\s+\d{4}\b',  # Mon DDth, YYYY
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # MM/DD/YYYY
        r'\b\d{1,2}-\d{1,2}-\d{4}\b'  # DD-MM-YYYY
    ]

    dates = []
    for patron in pat:
        dates.extend(re.findall(patron, text))

    dates = list(dict.fromkeys(dates))

    return dates
