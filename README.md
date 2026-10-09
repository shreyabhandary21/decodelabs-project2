# DecodeLabs Project 2 – Backend API Development

## Objective
A simple backend API built with Python Flask for the DecodeLabs Industrial Training Project 2.

The project demonstrates:
- GET API endpoints
- POST API endpoint
- User input and JSON responses
- Basic input validation
- HTTP status codes

## Project Structure

```text
DecodeLabs_Project_2_Backend_API/
│
├── backend/
│   └── app.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or later
- VS Code
- Postman or a browser for testing

## How to Run

### 1. Open the project in VS Code

Open the `DecodeLabs_Project_2_Backend_API` folder.

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate it

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:

```powershell
venv\Scripts\activate.bat
```

### 4. Install Flask

```powershell
pip install -r requirements.txt
```

### 5. Run the API

```powershell
python backend\app.py
```

The API will normally run at:

`http://127.0.0.1:5000`

## API Endpoints

### GET /
Checks whether the API is running.

### GET /api/users
Returns all users.

### GET /api/users/1
Returns a specific user.

### POST /api/users
Creates a new user.

Example JSON body:

```json
{
  "name": "Ananya",
  "email": "ananya@example.com"
}
```

## Validation

The POST endpoint checks:
- JSON request body
- Name is provided
- Email is provided
- Email contains `@`

Invalid input returns HTTP 400.

A missing user returns HTTP 404.

A successful user creation returns HTTP 201.

## Testing

You can test GET requests in a browser.

For POST, use Postman:
1. Select POST.
2. Enter `http://127.0.0.1:5000/api/users`.
3. Select Body → raw → JSON.
4. Enter the sample JSON.
5. Click Send.

## Learning Outcome

This project demonstrates the basic flow:

Client → HTTP Request → Flask API → Validation → Response

It can be extended later with a database, authentication, update/delete operations, and a frontend.
