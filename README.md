# Hotel Room Reservation API – Group 9

## Group Members
- 166101 – Ochieng Glen Kipchumba  
- 164416 – Cheruiyot Terence Kiptoo  
- 166329 – Tugee Laura Chemos  
- 151112 – Ondari Kimberly  
- 145836 – Musyoka Brian Kioko  
- 150567 – Natasha Njoroge  

---

## Project Description
This is a Django REST API for managing hotel room reservations.  
It will allow us to create and manage hotels, rooms, customers, reservations, and payments.  
The API will also handle validations such as preventing overlapping bookings and calculating total stay costs.

---

## Planned Models
1. **Hotel** – Stores hotel details like name, location, description, and rating.  
2. **Room** – Linked to a hotel, contains room number, type, price, and availability status.  
3. **Customer** – Stores personal details like name, email, phone number, and ID number.  
4. **Reservation** – Links a customer and a room with check-in/check-out dates, total price, and booking status.  
5. **Payment** – Linked to a reservation, records amount, payment method, transaction ID, and date.  
6. **Amenity** – Features like WiFi, breakfast, air conditioning (linked to rooms).

---

## Relationships
- One hotel can have many rooms.  
- One customer can make many reservations.  
- One room can have many reservations (on different dates).  
- One reservation can have multiple payments.  
- Rooms and amenities have a many-to-many relationship.

---

## How to Set Up Locally
```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/HotelRoomReservation-Group9.git
cd HotelRoomReservation-Group9

# 2. Create a virtual environment
py -m venv venv

# 3. Activate the virtual environment (PowerShell)
venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply migrations
python manage.py migrate

# 6. Create an admin user
python manage.py createsuperuser

# 7. Start the server
python manage.py runserver
