# 🧩 STAGE 0 - PROFILE API

## 📘 Project Overview
This is my **Stage 0 Backend Task** submission — a simple RESTful API that returns my profile information along with a **random cat fact** fetched from an external API.  
It demonstrates API integration, JSON formatting, and backend development skills using **Python (FastAPI)**.

---

## 📍 Endpoint
**GET** `/me`

### ✅ Example Response
```json
{
  "status": "success",
  "user": {
    "email": "amakatoebenezer@gmail.com",
    "name": "Ebenezer Amakato",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T12:00:00.000Z",
  "fact": "Cats sleep for 70% of their lives."
}
