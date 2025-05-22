# 🏨 Customer Management Module – Hotel Management System

This project is a GUI-based **Customer Management System** built using **Python Tkinter** and **MySQL**. It is a key module of a full-fledged Hotel Management System.

## 📌 Features

- 🔢 Auto-generated Customer Reference Number
- 🧾 Add / Update / Delete / Reset customer information
- 📥 Dropdowns for Gender, Nationality, ID Proof Type
- 🔍 Search customers by **Mobile** or **Reference ID**
- 📊 Display data in an interactive table with scrollbars
- 💾 Fully integrated with a MySQL database

## 🛠 Tech Stack

- **Frontend:** Python `Tkinter`
- **Backend:** MySQL
- **Image Handling:** Pillow (PIL)
- **Connector:** mysql-connector-python

## ⚙️ Requirements

- Python 3.x
- MySQL Server
- Python Libraries:
  ```bash
  pip install mysql-connector-python pillow
🗃️ MySQL Setup
Run the following SQL to create the database and table:

sql
Copy
Edit
CREATE DATABASE management;

USE management;

CREATE TABLE customer (
    Ref VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Mother VARCHAR(100),
    Gender VARCHAR(20),
    PostCode VARCHAR(20),
    Mobile VARCHAR(20),
    Email VARCHAR(100),
    Nationality VARCHAR(50),
    Idproof VARCHAR(50),
    Idnumber VARCHAR(50),
    Address VARCHAR(255)
);
Update your MySQL credentials in the script if needed:

python
Copy
Edit
conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="YourPassword",
    database="management"
)
▶️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Vikash8340/hotel-management.git
cd hotel-management
Run the script:

bash
Copy
Edit
python customer_module.py
📷 Screenshots
(Add screenshots of your application here to visually demonstrate its features)

🧑‍💻 Author
Vikash Kumar Ray
📧 vikash4evry123@gmail.com
🔗 GitHub Profile
