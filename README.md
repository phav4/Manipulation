# JSON User Data Manipulation (Python) #
### 📌 Project Overview ###
This project demonstrates how to load, process, and analyze user data stored in JSON format using Python.
The script reads user data from a JSON file, displays it in a readable table, converts date formats, and performs basic data analysis such as counting logins, checking verified emails, and identifying the first and last registered users.

### 📂 Project Structure ###
json_manipulation/
│
├── main.py
├── sample_users_with_id.json
├── requirements.txt
└── README.md

### 📄 Data Source ###
The user data is provided in JSON format and contains information such as:
 - User ID
 - Name and email
 - Login count
 - Account creation date
 - Email verification status

### ⚙️ Requirements ###
Ensure you have Python 3.x installed.
Install the required libraries using:
```
pip install json tabulate python-dateutil
```
Required Python Libraries
`json` (built-in)
`tabulate` – for table display
`python-dateutil` – for date parsing

### ▶️ How to Run the Program ###
Open a terminal in the project directory
Run the script:
```
python main.py
```
### 🧠 What the Program Does ###
✅ 1. Load JSON Data
Reads user data from a local JSON file
Converts it into Python objects (lists and dictionaries)

✅ 2. Display User Data
Extracts relevant fields
Displays all users in a tabular format

✅ 3. Convert Dates
Converts ISO 8601 date strings into a readable format

✅ 4. Calculate Total Logins
Sums all logins_count values across users

✅ 5. Count Verified Emails
Counts how many users have email_verified = true

✅ 6. Identify Account Timeline
Finds:
The first user to create an account
The most recent user to create an account

### 🛡️ Error Handling & Defensive Coding ###
`.get()` is used to safely access dictionary keys
Default values prevent crashes when fields are missing
This reflects real-world API and JSON data handling

### 📊 Sample Output ###
A table displaying all users
```
USER DATA TABLE

+--------------------------+----------------+-------------------+------------------+---------------+---------------------+
| User ID                  | Name           | Email             | Email Verified   |   Login Count | Created At          |
+==========================+================+===================+==================+===============+=====================+
| 583c3ac3f38e84297c002546 | test@test.com  | test@test.com     | True             |            15 | 2016-11-28 14:10:11 |
+--------------------------+----------------+-------------------+------------------+---------------+---------------------+
| 583c5484cb79a5fe593425a9 | test1@test.com | test1@test.com    | True             |             1 | 2016-11-28 16:00:04 |
+--------------------------+----------------+-------------------+------------------+---------------+---------------------+
| 583c57672c7686377d2f66c9 | aaa@aaa.com    | aaa@aaa.com       | True             |             2 | 2016-11-28 16:12:23 |
+--------------------------+----------------+-------------------+------------------+---------------+---------------------+
| 5840b954da0529cd293d76fe | a@a.com        | a@a.com           | True             |             3 | 2016-12-01 23:59:16 |
+--------------------------+----------------+-------------------+------------------+---------------+---------------------+
| 584a9d13e808bcf75f05f580 | N/A            | test9999@test.com | False            |             0 | 2016-12-09 12:01:23 |
+--------------------------+----------------+-------------------+------------------+---------------+---------------------+
```
Total login count
```
Total Login Count: 21
```
Number of verified email users
```
Number of Email Verified Users: 4
```
First and last account creation details
```
First Account Created:
test@test.com - 2016-11-28 14:10:11
```
```
Last Account Created:
test9999@test.com - 2016-12-09 12:01:23
```

### ✍️ Author ###
Favour Oyeleye
