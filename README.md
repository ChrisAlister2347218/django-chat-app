# Real-time Chat Application

A modern real-time chat application built with Django and Channels.

## 🚀 Live Demo
[View Demo](https://django-chat-10rn.onrender.com/)

## ✨ Features

- 🔐 User authentication (signup/login)
- 💬 Real-time messaging using WebSockets
- 👥 User list with online/offline status
- 📱 Responsive modern UI
- 💾 Message history persistence
- ⚡ Instant message delivery

## 🛠️ Technologies

- Django 5.1.6
- Django Channels
- WebSockets
- SQLite3
- HTML/CSS
- JavaScript

## 📋 Prerequisites

- Python 3.9+
- pip
- Virtual environment

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/django-chat-app.git
cd django-chat-app
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start development server
```bash
DJANGO_SETTINGS_MODULE=chat_project.settings python -m daphne chat_project.asgi:application
```

## 💻 Development

To contribute to this project:

1. Fork the repository
2. Create your feature branch
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes
```bash
git commit -m 'Add some AmazingFeature'
```
4. Push to the branch
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request

## 📝 License

[MIT License](LICENSE)

## 👥 Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter)

Project Link: [https://github.com/YOUR_USERNAME/django-chat-app](https://github.com/YOUR_USERNAME/django-chat-app)

## Project Structure

```
chat_project/
├── chat/
│   ├── static/
│   │   └── chat/
│   │       └── chat.css
│   │   
│   ├── templates/
│   │   └── chat/
│   │       ├── base.html
│   │       ├── chat.html
│   │       ├── login.html
│   │       └── signup.html
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── urls.py
│   └── views.py
└── chat_project/
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE) 
