#!/usr/bin/env python3
"""
Update the hardcoded Regular Meetup dates in signup2.html
Run this when the schedule changes or weekly to verify
"""

import re

SIGNUP_FILE = 'signup2.html'

# Regular Meetup dates from index.html schedule
# Update this list manually when the schedule changes
REGULAR_MEETUP_DATES = [
    '2026-04-16',
    '2026-05-07',
    '2026-05-14',
    '2026-05-21',
    '2026-06-04',
    '2026-06-11',
    '2026-06-18',
    '2026-07-09'
]

def update_signup_dates():
    """Update signup2.html with current Regular Meetup dates"""
    with open(SIGNUP_FILE, 'r') as f:
        content = f.read()
    
    # Generate the dates array
    dates_list = ',\n            '.join([f"'{date}'" for date in REGULAR_MEETUP_DATES])
    new_dates_section = f"""const DATES = [
            {dates_list}
        ];"""
    
    # Replace the DATES array (match the exact format)
    pattern = r"const DATES = \[[^\]]*\];"
    
    if not re.search(pattern, content, re.DOTALL):
        print("⚠️  Could not find DATES array in signup2.html")
        return False
    
    new_content = re.sub(pattern, new_dates_section, content, flags=re.DOTALL)
    
    if new_content == content:
        print("ℹ️  No changes needed - dates are already up to date")
        return False
    
    with open(SIGNUP_FILE, 'w') as f:
        f.write(new_content)
    
    print("✅ Updated signup2.html with Regular Meetup dates:")
    for date in REGULAR_MEETUP_DATES:
        print(f"   {date}")
    print("\nℹ️  Remember to also update this script when schedule changes!")
    return True

if __name__ == '__main__':
    success = update_signup_dates()
    exit(0 if success else 1)
