# Fix for Volunteer Signup Overwrite Issue

## Problem
The signup form was allowing people to overwrite existing volunteer signups for the same date+role combination.

## Solution
Updated both the Google Apps Script backend and the HTML frontend to:
1. Check for conflicts before accepting signups
2. Show clear error messages with the name of who already signed up
3. Properly handle responses (removed no-cors mode)

## Steps to Apply the Fix

### Step 1: Update Google Apps Script

1. Open your Google Sheet for volunteers
2. Go to **Extensions** > **Apps Script**
3. Replace the entire code with the contents of `GOOGLE_APPS_SCRIPT_UPDATE.js`
4. Click **Save** (💾 icon)
5. Click **Deploy** > **New deployment**
6. Settings:
   - Type: **Web app**
   - Execute as: **Me**
   - Who has access: **Anyone**
7. Click **Deploy**
8. **IMPORTANT:** Copy the new deployment URL

### Step 2: Update signup.html (if URL changed)

If you got a new deployment URL in Step 1:

1. Open `signup.html`
2. Find the line: `const SCRIPT_URL = 'https://script.google.com/macros/...'`
3. Replace it with your new deployment URL
4. Save the file

### Step 3: Test

1. Try to sign up for a role/date
2. Try to sign up for the SAME role/date with a different name
3. You should see: "Sorry, [Role] on [Date] is already taken by [Name]"

## Files Changed

- `signup.html` - Updated JavaScript to properly handle conflict responses
- `GOOGLE_APPS_SCRIPT_UPDATE.js` - New backend logic with conflict detection

## What Changed

**Google Apps Script:**
- Added conflict detection loop before inserting data
- Returns proper JSON responses with `success`, `conflict`, and `message` fields
- Shows the name of who already signed up

**HTML/JavaScript:**
- Removed `mode: 'no-cors'` to allow reading responses
- Added proper error handling for conflicts
- Better user feedback messages

---

**Date:** April 14, 2026
**Issue:** Signup overwrites
**Status:** Fixed ✅
