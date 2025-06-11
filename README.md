# MyBankingWorld_FlaskApp

A simple, full-featured online banking system built with Flask and MongoDB. The application supports user and admin operations for managing different types of bank accounts, performing transactions, and viewing account history.

## Features

- **Account Management**
  - Open Savings and Current accounts with personal details and privilege levels.
  - Close, delete, or reactivate accounts.
  - View all accounts associated with a user's email.
  - Admins can view all accounts and reactivate accounts.

- **Transactions**
  - Deposit and withdraw funds.
  - Transfer funds between accounts.
  - Enforce daily transaction limits based on user privileges (Premium/Gold/Silver).
  - Transaction history for all accounts.

- **Admin Dashboard**
  - View and update privilege levels and daily limits.
  - View all transactions in the system.

## Technologies Used

- **Backend:** Flask (Python)
- **Database:** MongoDB (with PyMongo)
- **Frontend:** HTML/Jinja templates (Flask rendering)
- **Security:** Passwords and PINs are securely hashed.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB (running locally or accessible remotely)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Application

1. **Set up MongoDB:**  
   Ensure your MongoDB service is running and accessible by the Flask app.
2. **Configure Environment:**  
   - (If needed) Set your MongoDB URI in the app configuration.
3. **Start the Flask server:**
   ```bash
   python main.py
   ```
   The app should be available at `http://127.0.0.1:5000/`

## Usage

- **User Operations:**  
  - Register and log in.
  - Open new Savings/Current accounts.
  - Deposit, withdraw, transfer funds.
  - View transaction history.

- **Admin Operations:**  
  - Log in as admin.
  - View all accounts and transactions.
  - Change privilege values for transaction limits.
  - Reactivate closed accounts.

## Project Structure

```
.
├── main.py
├── app.py
├── models/
│   ├── account.py
│   ├── savings.py
│   └── current.py
├── repositories/
│   └── account_repository.py
├── services/
│   ├── account_manager.py
│   └── transaction_manager.py
├── admin/
│   └── admin.py
├── routes/
├── templates/
└── requirements.txt
```

## Account Types

- **Savings Account:** Requires name, email, DOB, gender, privilege, balance, PIN.
- **Current Account:** Requires name, email, registration number, website URL, privilege, balance, PIN.

## Privileges & Limits

- Users are assigned privilege levels (Premium/Gold/Silver), which determine their daily transaction limits. These can be updated by the admin.

## Security

- All sensitive information such as PINs are hashed before storage.
- Session-based authentication for users and admins.

## License

This project is for educational/demo purposes. Please modify and secure further before deploying in production.

---

*Created by [171801rohith](https://github.com/171801rohith)*
