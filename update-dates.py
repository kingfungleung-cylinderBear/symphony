#!/usr/bin/env python3
"""
Update the hardcoded Thursday dates in signup.html
Run this weekly to refresh the date dropdown with the next 10 Thursdays
"""

import re
from datetime import datetime, timedelta

SIGNUP_FILE = 'signup.html'

def generate_thursday_options(count=10):
    """Generate the next N Thursdays as HTML option elements"""
    today = datetime.now()
    thursdays = []
    current_date = today
    
    while len(thursdays) < count:
        current_date += timedelta(days=1)
        if current_date.weekday() == 3:  # Thursday
            date_str = current_date.strftime('%Y-%m-%d')
            readable = current_date.strftime('%B %d, %Y (Thursday)')
            thursdays.append(f'                        <option value="{date_str}">{readable}</option>')
    
    return thursdays

def update_signup_dates():
    """Update signup.html with fresh Thursday dates"""
    with open(SIGNUP_FILE, 'r') as f:
        content = f.read()
    
    # Generate new dates
    new_dates = generate_thursday_options(10)
    hardcoded_dates = '\n'.join(new_dates)
    
    # Replace the date options (everything between the placeholder option and </select>)
    pattern = r'(<option value="">Choose a date...</option>)\s*(<option value=".*?</option>\s*)*(\s*</select>)'
    replacement = f'\\1\n{hardcoded_dates}\n                    \\3'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(SIGNUP_FILE, 'w') as f:
        f.write(new_content)
    
    print("✅ Updated signup.html with fresh Thursday dates:")
    for date_option in new_dates:
        print(f"   {date_option.strip()}")
    print("\nNext steps:")
    print("1. Review the changes: git diff signup.html")
    print("2. Commit: git add signup.html && git commit -m 'Update Thursday dates'")
    print("3. Push: git push origin main")

if __name__ == '__main__':
    update_signup_dates()
