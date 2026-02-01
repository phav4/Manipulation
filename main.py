import json
from tabulate import tabulate
from dateutil import parser

# Load JSON data
with open("sample_users_with_id.json", "r", encoding="utf-8") as file:
    users = json.load(file)

# Convert ISO date to readable format
def format_date(date_str):
    return parser.parse(date_str).strftime("%Y-%m-%d %H:%M:%S")

# Prepare table data
table = []
for user in users:
    table.append([
        user.get("user_id", "N/A"),
        user.get("name", "N/A"),
        user.get("email", "N/A"),
        user.get("email_verified", False),
        user.get("logins_count", 0),
        format_date(user["created_at"])
    ])

headers = [
    "User ID",
    "Name",
    "Email",
    "Email Verified",
    "Login Count",
    "Created At"
]

print("\nUSER DATA TABLE\n")
print(tabulate(table, headers=headers, tablefmt="grid"))

# Sum all login counts
total_logins = sum(user.get("logins_count", 0) for user in users)
print("\nTotal Login Count:", total_logins)

# Count verified emails
verified_count = sum(1 for user in users if user.get("email_verified") is True)
print("Number of Email Verified Users:", verified_count)

# Find first and last account creation
sorted_users = sorted(users, key=lambda x: x["created_at"])

first_user = sorted_users[0]
last_user = sorted_users[-1]

print("\nFirst Account Created:")
print(f"{first_user.get('email', 'N/A')} - {format_date(first_user['created_at'])}")

print("\nLast Account Created:")
print(f"{last_user.get('email', 'N/A')} - {format_date(last_user['created_at'])}")
