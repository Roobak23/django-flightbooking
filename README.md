# ✈️ Django Flight Booking System

A simple and user-friendly Flight Booking Web Application built using **Django**.  
Users can search flights, book tickets, view booking confirmation, and manage authentication.

---

## 🚀 Features

### 👤 User Features
- User Signup, Login, Logout  
- Search flights by:
  - Source  
  - Destination  
  - Date  
- View available flights  
- Book flights (name, email, seats)  
- Booking success page  
- Redirect to bookings page after login (optional)

---

### 🛠 Admin Features
- Add, update, delete flights
- View all bookings
- Manage users
- Search flights in admin panel

---

## 🧱 Technologies Used
- Python 3  
- Django 5  
- SQLite  
- Bootstrap 5  
- HTML / CSS / JS  

---





## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Roobak23/django-flightbooking.git
cd django-flightbooking
```
### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate venv

```bash
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the server
```bash
python manage.py runserver
```

Now visit the app at:
👉 http://127.0.0.1:8000/

## 📌 Future Enhancements

- Payment integration
- Email ticket confirmation
- Seat availability
- User booking history
- Booking cancellation

## 🤝 Contributing

Pull requests are welcome!
Feel free to open issues for suggestions or improvements.

## 📜 License

Open-source under the MIT License.











