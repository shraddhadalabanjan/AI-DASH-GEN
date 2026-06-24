# AI-DASH-GEN

An AI-driven portfolio dashboard generator that dynamically syncs user engagement metrics (views, likes, comments) and manages articles using a Python (Flask) backend, SQLite database, and Firebase Authentication.


## 🚀 About the Project
**AIDashGen** is a full-stack portfolio dashboard application designed for content creators and professionals. It allows users to securely register and log in, view live engagement analytics, and dynamically manage their published articles through a centralized web interface. 

## 🔑 Key Features
* **Secure Authentication:** Integrated **Firebase Authentication** providing reliable, real-time user signup and sign-in functionality.
* **Dynamic Analytics Dashboard:** Displays key portfolio performance metrics including total views, likes, comments, and publication counts.
* **Dynamic Article Management:** Enables users to publish new articles and instantly view updated listings pulled directly from the database.
* **Robust Python Backend:** Built with a lightweight **Flask API** handling data routing, query parameters, and user state handling without cross-origin blocks (**CORS** enabled).
* **Persistent SQLite Storage:** Implements a relational database with auto-initialization schemas (`user_stats` and `articles` tables) to safely store user information.
* **Responsive UI:** Features a sleek, modern front-end layout utilizing custom CSS grids and flexible box properties optimized for both desktop and mobile viewports.

## 🛠️ Tech Stack Used
* **Frontend:** HTML5, CSS3, JavaScript (ES6, Fetch API)
* **Backend:** Python 3, Flask, Flask-CORS
* **Database:** SQLite3
* **Authentication:** Firebase (Compat Web SDK v10)
