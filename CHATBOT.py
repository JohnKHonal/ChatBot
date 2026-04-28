"""
bmp_chatbot_timetable.py
Chatbot using Boyer–Moore algorithm + timetable lookup + faculty details
"""

import re

# ---------------------------------------------------------
# 1. SUBJECT → FULL NAME + FACULTY
# ---------------------------------------------------------

SUBJECT_INFO = {
    "BC601": (
        "Professional Business Communication",
        "Dr. Sritama Maitra"
    ),
    "CSE604": (
        "Advanced Data Structures",
        "Dr. Madhulika Y"
    ),
    "CSE603": (
        "High Performance Computer Architecture",
        "Dr. Kaushik"
    ),
    "CSE605": (
        "Mathematical Foundation of Computer",
        "Dr. Ekta Maini Marwaha"
    ),
    "CSE602": (
        "Advanced Software Project Planning",
        "Dr. Kaushik"
    ),
    "CSE601": (
        "Data Warehousing and Data Mining",
        "Dr. Madhulika Y"
    ),
    "HV601": (
        "Universal Human Values",
        "Dr. Sritama Maitra"
    ),
}

# ---------------------------------------------------------
# SLOT TIMES (from image)
# ---------------------------------------------------------
SLOT_TIMES = [
    ("09:15", "10:05"),
    ("10:10", "11:00"),
    ("11:00", "11:20"),  # BREAK
    ("11:20", "12:10"),
    ("12:15", "13:05"),
    ("13:10", "14:00"),  # LUNCH
    ("14:05", "14:55"),
    ("15:00", "15:50"),
]

# ---------------------------------------------------------
# TIMETABLE (based on your uploaded image)
# ---------------------------------------------------------

TIMETABLE = {
    "monday": [
        "CSE605", "HV601", "BREAK",
        "CSE602", "CSE604", "LUNCH",
        "CSE601", "CSE601"
    ],
    "tuesday": [
        "CSE602", "CSE602", "BREAK",
        "CSE604", "CSE603", "LUNCH",
        "HV601", "CSE601"
    ],
    "wednesday": [
        "CSE604", "CSE604", "BREAK",
        "BC601", "CSE602", "LUNCH",
        "CSE603", "CSE601"
    ],
    "thursday": [
        "CSE602", "CSE604", "BREAK",
        "CSE605", "BC601", "LUNCH",
        "CSE601", "CSE603"
    ],
    "friday": [
        "CSE601", "CSE603", "BREAK",
        "BC601", "CSE604", "LUNCH",
        "CSE602", "CSE605"
    ],
}

# ---------------------------------------------------------
# NORMALIZATION + BOYER MOORE
# ---------------------------------------------------------

def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())


def build_bad_char_table(pattern: str) -> dict:
    table = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    return table


def boyer_moore_search(text: str, pattern: str) -> int:
    n = len(text)
    m = len(pattern)
    if m == 0 or m > n:
        return -1
    bad = build_bad_char_table(pattern)
    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and text[shift + j] == pattern[j]:
            j -= 1
        if j < 0:
            return shift
        last = bad.get(text[shift + j], -1)
        shift += max(1, j - last)
    return -1

# ---------------------------------------------------------
# TIME HELPERS
# ---------------------------------------------------------

import re
TIME_RE = re.compile(r"(\b[01]?\d|2[0-3]):([0-5]\d)\b")

def extract_time(text: str):
    text = normalize(text)
    m = TIME_RE.search(text)
    if m:
        return f"{int(m.group(1)):02d}:{int(m.group(2)):02d}"
    return None

def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def find_slot(time_str):
    t = time_to_minutes(time_str)
    for i, (s, e) in enumerate(SLOT_TIMES):
        if time_to_minutes(s) <= t <= time_to_minutes(e):
            return i
    return -1

# ---------------------------------------------------------
# FIND DAY
# ---------------------------------------------------------

DAY_WORDS = ["monday", "tuesday", "wednesday", "thursday", "friday"]

def extract_day(text):
    text = normalize(text)
    for d in DAY_WORDS:
        if boyer_moore_search(text, d) != -1:
            return d
    return None

# ---------------------------------------------------------
# TIMETABLE QUERY RESPONSE
# ---------------------------------------------------------

def subject_details(code: str):
    if code in ("BREAK", "LUNCH"):
        return code, "", ""
    name, prof = SUBJECT_INFO.get(code, ("Unknown Subject", "Unknown Faculty"))
    return code, name, prof


def get_class_at(day: str, time_str: str):
    slot = find_slot(time_str)
    if slot == -1:
        return "Time not found in timetable slots."

    entry = TIMETABLE[day][slot]

    code, name, prof = subject_details(entry)

    if code in ("BREAK", "LUNCH"):
        return f"At {time_str} on {day.title()}, it is **{code}**."

    return (
        f"At {time_str} on {day.title()}, your class is:\n"
        f"→ **{code} – {name}**\n"
        f"→ Faculty: **{prof}**"
    )


def get_day_schedule(day: str):
    out = [f"Schedule for {day.title()}:"]
    for i, entry in enumerate(TIMETABLE[day]):
        start, end = SLOT_TIMES[i]
        code, name, prof = subject_details(entry)
        if code in ("BREAK", "LUNCH"):
            out.append(f"{start}-{end} → {code}")
        else:
            out.append(f"{start}-{end} → {code} – {name} ({prof})")
    return "\n".join(out)

# ---------------------------------------------------------
# MAIN QUERY HANDLER
# ---------------------------------------------------------

def answer_query(text: str):
    text_n = normalize(text)

    day = extract_day(text_n)
    time_str = extract_time(text_n)

    # FULL query: day + time
    if day and time_str:
        return get_class_at(day, time_str)

    # Only day
    if day:
        return get_day_schedule(day)

    # Greeting fallback
    if "hello" in text_n or "hi" in text_n:
        return "Hello! Ask me your class timings."

    return "Please ask like: 'What class on Monday at 10:30?' or 'Friday schedule'."

# ---------------------------------------------------------
# RUN CHATBOT
# ---------------------------------------------------------

def chat_loop():
    print("Timetable Chatbot with Professors (BMP-based)")
    print("Ask things like:")
    print(" - What class is on Monday at 09:30?")
    print(" - Which class do I have Friday?")
    print(" - Wednesday schedule\n")

    while True:
        user = input("You: ")
        if normalize(user) in ("bye", "exit", "quit"):
            print("Bot: Goodbye!")
            break
        print("Bot:", answer_query(user))

if __name__ == "__main__":
    chat_loop()
