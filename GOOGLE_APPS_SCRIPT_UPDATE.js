// UPDATED Google Apps Script - Step 1: Deploy Settings
// After pasting this code:
// 1. Click "Deploy" > "New deployment"
// 2. Click the gear icon next to "Select type"
// 3. Choose "Web app"
// 4. Set "Execute as": Me
// 5. Set "Who has access": Anyone
// 6. Click "Deploy"
// 7. Copy the new deployment URL and update signup.html SCRIPT_URL

function doPost(e) {
  try {
    // Enable CORS
    const output = ContentService.createTextOutput();
    output.setMimeType(ContentService.MimeType.JSON);
    
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Volunteers');
    
    // Parse incoming data
    const data = JSON.parse(e.postData.contents);
    const { name, date, role } = data;
    
    // Validate
    if (!name || !date || !role) {
      output.setContent(JSON.stringify({
        success: false,
        message: 'Missing required fields'
      }));
      return output;
    }
    
    // Get all existing data (assuming columns: Date, Role, Name, Timestamp)
    const lastRow = Math.max(sheet.getLastRow(), 1);
    if (lastRow > 1) {
      const dataRange = sheet.getRange(2, 1, lastRow - 1, 3);
      const values = dataRange.getValues();
      
      // Check for conflicts
      for (let i = 0; i < values.length; i++) {
        const rowDate = values[i][0];
        const rowRole = values[i][1];
        const rowName = values[i][2];
        
        // Handle date comparison
        let existingDate;
        if (rowDate instanceof Date) {
          existingDate = Utilities.formatDate(rowDate, Session.getScriptTimeZone(), 'yyyy-MM-dd');
        } else {
          existingDate = String(rowDate);
        }
        
        if (existingDate === date && rowRole === role) {
          // Conflict found!
          const readableDate = formatDateReadable(date);
          output.setContent(JSON.stringify({
            success: false,
            conflict: true,
            message: `Sorry, ${role} on ${readableDate} is already taken by ${rowName}. Please choose a different role or date.`
          }));
          return output;
        }
      }
    }
    
    // No conflict - add the signup
    sheet.appendRow([date, role, name, new Date()]);
    
    output.setContent(JSON.stringify({
      success: true,
      message: 'Sign-up successful! Thank you for volunteering.'
    }));
    return output;
    
  } catch (error) {
    Logger.log('Error: ' + error.toString());
    const output = ContentService.createTextOutput();
    output.setMimeType(ContentService.MimeType.JSON);
    output.setContent(JSON.stringify({
      success: false,
      message: 'Server error. Please try again or contact the administrator.'
    }));
    return output;
  }
}

// Handle GET requests (for CORS preflight)
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'Service is running' }))
    .setMimeType(ContentService.MimeType.JSON);
}

function formatDateReadable(dateStr) {
  const date = new Date(dateStr + 'T00:00:00');
  const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
  return date.toLocaleDateString('en-US', options);
}
