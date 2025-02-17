# ChatRoomApp

## Overview
ChatRoomApp is a real-time chat application built using Django and React. It provides JWT-based authentication, WebSockets (Django Channels) for real-time messaging, and stores chat history in a MySQL database. Users can create chat rooms, send and receive messages in real-time, and view active participants.

## Features
- **Authentication:** Users can sign up and log in using JWT authentication.
- **Chat Rooms:** Users can create new chat rooms or join existing ones.
- **Real-Time Messaging:** Messages are sent and received instantly using WebSockets.
- **Chat History:** Messages are stored in the database and can be retrieved anytime.
- **Active User Tracking:** Displays logged-in users in a chat room.
- **Frontend:** React-based UI for creating and joining chat rooms.
- **Backend:** Django handles authentication, message storage, and WebSockets for real-time communication.
- **Error Handling:** Basic input validation and error messages.

## Technologies Used
### Backend:
- Django
- Django REST Framework (DRF)
- Django Channels (WebSockets)
- MySQL
- JWT Authentication

### Frontend:
- React.js
- HTML5, CSS3, JavaScript
- WebSockets API

## Project Structure
```
ChatRoomApp/
├── backend/
│   ├── chat/
│   ├── accounts/
│   ├── config/
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3 (if using SQLite for testing)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   ├── index.js
│   ├── public/
│   ├── package.json
│
├── README.md
```

## Setup Instructions
### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ChatRoomApp.git
   cd ChatRoomApp/backend
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Start the Django server:
   ```sh
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend folder:
   ```sh
   cd ../frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React development server:
   ```sh
   npm start
   ```

## Usage
1. Register and log in to the app.
2. Create a new chat room or join an existing one.
3. Start sending and receiving real-time messages.
4. View active users in the chat room.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|------------|
| POST | `/api/auth/register/` | User registration |
| POST | `/api/auth/login/` | User login (JWT token) |
| GET | `/api/chat/rooms/` | Get available chat rooms |
| POST | `/api/chat/rooms/create/` | Create a new chat room |
| GET | `/api/chat/rooms/{room_id}/messages/` | Get chat history |

## WebSockets
The chat feature uses WebSockets for real-time messaging. WebSocket connections are established at:
```
ws://localhost:8000/ws/chat/{room_name}/
```
Messages sent through WebSockets are automatically broadcasted to all participants in the room.

## Future Enhancements
- Add typing indicators
- Implement message reactions (likes, emojis)
- Support for private messaging
- UI improvements with better design

## License
This project is licensed under the MIT License.

## Contributors
- **Thirumurugan** (Developer)

