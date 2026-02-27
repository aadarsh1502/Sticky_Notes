📝 Sticky Notes Web Application

A simple and user-friendly Sticky Notes web application built using Django.
This application allows users to create, edit, and delete notes with a title and description. All notes are stored in a SQLite database using unique IDs.

🚀 Features

➕ Add new notes (Title + Description)

✏️ Edit existing notes

🗑️ Delete notes

📂 Notes stored in SQLite database

🆔 Each note managed using unique ID

🎨 Frontend built using Django Templates + CSS

💻 Runs locally

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS (Django Templates)

Database: SQLite

Server: Django Development Server

📁 Project Structure
sticky_notes_project/
│
├── project/        # Main project settings
├── app/            # Notes application
├── db.sqlite3
└── manage.py
⚙️ Installation & Setup

Follow these steps to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # For Windows
3️⃣ Install Dependencies
pip install django
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Start the Server
python manage.py runserver

Now open your browser and go to:

http://127.0.0.1:8000/

🎯 Future Improvements

Add user authentication (Login / Signup)

Add search functionality

Add note categories

Add timestamps

Deploy to cloud (Render / Railway)
