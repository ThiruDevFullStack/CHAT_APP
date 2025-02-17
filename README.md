# 📌 Chat Application

A real-time chat application built using **Django (backend)** and **React (frontend)** with WebSockets, JWT authentication, and MySQL database.

## 📂 Project Structure

```
CHAT_APP/
│── backend/
│   │── backend/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │── chat/
│   │   ├── consumers.py
│   │   ├── models.py
│   │   ├── routing.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │── users/
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │── env/ (Virtual Environment)
│   │── db.sqlite3
│   │── manage.py
│
│── frontend/
│   │── src/
│   │   ├── Components/
│   │   │   ├── ChatPage.js
│   │   │   ├── ChatRoomCreate.js
│   │   │   ├── LoginPage.js
│   │   │   ├── SignUpPage.js
│   │   ├── Styles/
│   │   │   ├── App.css
│   │   ├── App.js
│   │   ├── index.js
│   │── package.json
│   │── README.md
```

---

## 🚀 Features
- User authentication (Signup/Login) using **JWT**.
- Real-time chat with **WebSockets (Django Channels)**.
- Create and join chat rooms dynamically.
- Display active users in a chat room.
- Store chat messages and history in the database.

---

## 🔧 Backend Setup (Django)

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo.git
   cd CHAT_APP/backend
   ```
2. **Create and activate virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Run the server:**
   ```sh
   python manage.py runserver
   ```

---

## 🎨 Frontend Setup (React)

1. **Navigate to frontend directory:**
   ```sh
   cd CHAT_APP/frontend
   ```
2. **Install dependencies:**
   ```sh
   npm install
   ```
3. **Start the React development server:**
   ```sh
   npm start
   ```

---

## 📡 WebSockets Setup
Ensure Django Channels is installed and configured properly in `asgi.py`, `routing.py`, and `consumers.py`.

---

## 📜 API Endpoints
### **Authentication (JWT)**
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/users/signup/` | Register a new user |
| POST | `/api/users/login/` | Login and get JWT token |
| GET  | `/api/users/profile/` | Get logged-in user details |

### **Chat Functionalities**
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET  | `/api/chat/rooms/` | Get all chat rooms |
| POST | `/api/chat/rooms/` | Create a new chat room |
| GET  | `/api/chat/messages/{room_id}/` | Get chat history |

---

## 🛠️ Technologies Used
- **Backend:** Django, Django REST Framework, Django Channels, WebSockets, JWT
- **Frontend:** React.js, WebSockets, CSS
- **Database:** MySQL / SQLite

---

## 📌 To-Do
- Improve UI design
- Implement notifications for new messages
- Add file sharing functionality

---

## 🤝 Contributing
Feel free to submit issues or pull requests for improvements.

---

## 📄 License
This project is licensed under the MIT License.