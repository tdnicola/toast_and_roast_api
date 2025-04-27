# 🥂 Toast and Roast API

Welcome to the **Toast and Roast API** — a simple, fun microservice that generates **random compliments** or **savage insults** on demand.

Built with ❤️ using Python, Flask, and Docker.

---

## ✨ Features

- 🎯 `/compliment` endpoint returns a positive, uplifting message.
- 🔥 `/insult` endpoint delivers a sarcastic or humorous roast.
- 🔀 Randomly generated using large, dynamic wordlists.
- 📎 Easily containerized and deployable anywhere using Docker.
- 🛡️ No external database needed — pure, fast, lightweight.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/toast_and_roast_api.git
cd toast_and_roast_api
```

### 2. Build the Docker Image

```bash
docker build -t toast_and_roast_api .
```

### 3. Run the Container

```bash
docker run -d -p 5000:5000 --name toast_and_roast_api toast_and_roast_api
```

✅ Now the API is live at [http://localhost:5000](http://localhost:5000)

---

## 📚 API Endpoints

### `GET /compliment`

- Returns a JSON compliment.

**Example Response:**

```json
{
  "type": "compliment",
  "message": "Behold, the radiant lighthouse."
}
```

---

### `GET /insult`

- Returns a JSON insult.

**Example Response:**

```json
{
  "type": "insult",
  "message": "You're as clueless as a soggy donut."
}
```

---

## 🧐 Architecture Overview

- `/compliment` → Randomly picks an opening + adjective + noun + template from the compliments word lists.
- `/insult` → Randomly generates a creative roast using insult word lists and templates.
- All word lists are stored in plain text files under `compliments/` and `insults/` folders.

---

## 🛠 Project Structure

```
toast_and_roast_api/
├── app.py               # Flask API application
├── compliments/         # Compliment data and logic
│   ├── adjectives.txt
│   ├── nouns.txt
│   ├── openings.txt
│   ├── templates.txt
│   └── __init__.py
├── insults/             # Insult data and logic
│   ├── adjectives.txt
│   ├── nouns.txt
│   ├── openings.txt
│   ├── templates.txt
│   └── __init__.py
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
└── README.md            # You are here!
```

---

## 🦙 Environment Notes

- Flask is configured to run on `0.0.0.0:5000` for easy container access.
- No database or persistent storage required.
- Designed for use alongside my Discord bot.

---

## 🙌 Acknowledgements

Inspired by good friends, bad jokes, and the eternal need for both **hype** and **humble pie**. 🥧 And the fact that all the APIs I use seem to go out.

