import pandas as pd
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sample JSON data
json_data = '''
{
    "employees": [
        {"id": 1, "name": "John", "age": 30, "department": "HR"},
        {"id": 2, "name": "Alice", "age": 25, "department": "IT"},
        {"id": 3, "name": "Bob", "age": 35, "department": "Finance"}
    ]
}
'''

# Load JSON data into a Python object
data = json.loads(json_data)

# Convert JSON to DataFrame
df = pd.DataFrame(data)
print(df)

# Convert DataFrame to HTML table
table_html = df.to_html(index=False)

# Email configuration
sender_email = "nandeshbabu@gmail.com"
receiver_email = "nivethashreeks@gmail.com"
password = "ojip rczk hbpt gwmp"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Email content
subject = "JSON to Table Email"
body = f"<p>Table from JSON data:</p>{table_html}"


# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach HTML content to the email
message.attach(MIMEText(body, "html"))

# Establish a connection with the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Start TLS for security
    server.starttls()
    
    # Login to the email account
    server.login(sender_email, password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully.")
