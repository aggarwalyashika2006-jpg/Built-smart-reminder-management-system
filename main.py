import pandas as pd
import logging

# Logging Setup
logging.basicConfig(
    filename='logs/automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print("Smart Reminder Management System Started...")

# Load CSV Files
contacts = pd.read_csv('data/contacts.csv')
reminders = pd.read_csv('data/reminders.csv')

sent_list = []
failed_list = []

# Process Reminders
for index, row in reminders.iterrows():

    try:

        name = row['name']
        email = row['email']
        reminder_type = row['reminder_type']
        reminder_date = row['reminder_date']

        message = f"""
Hello {name},

This is your reminder for:
{reminder_type}

Date: {reminder_date}

Regards,
Smart Reminder Team
"""

        print(f"\n[SIMULATION] Sending Email To: {email}")
        print(message)

        sent_list.append({
            'name': name,
            'email': email,
            'reminder_type': reminder_type,
            'status': 'Sent'
        })

        logging.info(f"Email sent to {email}")

    except Exception as e:

        failed_list.append({
            'error': str(e)
        })

        logging.error(str(e))

# Save Reports
sent_df = pd.DataFrame(sent_list)
failed_df = pd.DataFrame(failed_list)

sent_df.to_csv('outputs/sent_report.csv', index=False)
failed_df.to_csv('outputs/failed_report.csv', index=False)

print("\nReports Generated Successfully")