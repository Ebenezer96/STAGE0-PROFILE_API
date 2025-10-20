
# 🧩 STAGE 0 - PROFILE API

## 📘 Project Overview

This is my **Stage 0 Backend Task** submission — a simple RESTful API that returns my profile information along with a random cat fact fetched from an external API.
It demonstrates **API integration**, **JSON formatting**, and **backend development skills** using **Python (FastAPI)**.

---

## 📍 Endpoint

**GET** `/me`

**Live URL:**
👉 [https://stage0-profileapi.pxxl.click/me](https://stage0-profileapi.pxxl.click/me)

---

## ✅ Example Response

```json
{
  "status": "success",
  "user": {
    "email": "ebenezeramakato96@gmail.com",
    "name": "Ebenezer Amakato",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T12:00:00.000Z",
  "fact": "Cats sleep for 70% of their lives."
}
```

---

## ⚙️ How to Run Locally (Windows)

1. **Clone this repository**

   ```bash
   git clone https://github.com/Ebenezer96/STAGE0-PROFILE_API.git
   cd STAGE0-PROFILE_API
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```

5. **Test locally:**
   Visit 👉 [http://127.0.0.1:8000/me](http://127.0.0.1:8000/me)

---

## 🧾 Dependencies

* **fastapi** – Web framework
* **uvicorn** – ASGI server
* **httpx** – For fetching Cat Facts API

---

## 📁 Folder Structure

```
STAGE0-PROFILE_API/
│
├── main.py
├── requirements.txt
└── README.md
```




* 🌐 Server URL: [https://stage0-profileapi.pxxl.click/me](https://stage0-profileapi.pxxl.click/me)
* 🔗 GitHub Repo: [https://github.com/Ebenezer96/STAGE0-PROFILE_API](https://github.com/Ebenezer96/STAGE0-PROFILE_API)
* 👤 Full Name: *Ebenezer Amakato*
* 📧 Email: *[ebenezeramakato96@gmail.com](mailto:ebenezeramakato96@gmail.com)*
* 💻 Stack: *Backend*

-