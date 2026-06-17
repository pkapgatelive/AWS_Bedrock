# Flask Task Tracker

A simple web-based task manager built with Flask. Tasks are persisted locally in a JSON file and displayed sorted by priority.

---

## Project Structure

```
Q-Developer/
├── app.py               # Flask backend (routes + file persistence)
├── requirements.txt     # Python dependencies
├── tasks.json           # Auto-generated task storage (created on first add)
└── templates/
    └── index.html       # Frontend UI
```

---

## Setup

**Prerequisites**: Python 3.x

```bash
# 1. (Optional) Activate a virtual environment
source ../excercise1/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open http://127.0.0.1:5000 in your browser.

---

## API Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | List all tasks sorted by priority (ascending) |
| `POST` | `/add` | Add a new task |
| `POST` | `/remove/<index>` | Remove task at given 0-based index |

### POST /add — Form Parameters

| Field | Type | Validation |
|-------|------|------------|
| `name` | string | Required, non-empty |
| `priority` | integer | Required, 1–5 |

Invalid input silently redirects back to `/` without saving.

---

## Data Storage

Tasks are stored in `tasks.json` as a JSON array:

```json
[
  {"name": "Write tests", "priority": 1},
  {"name": "Deploy app",  "priority": 3}
]
```

The file is created automatically on the first task add. Tasks are always loaded and re-sorted by priority on every request.

---

## Frontend

`templates/index.html` renders:
- An **add form** with a text input (task name) and a priority dropdown (1–5)
- A **task list** showing each task's priority badge and name, with a Remove button per task
- An empty state message when no tasks exist

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.1.1 | Web framework, routing, templating |

---

## Known Limitations

- No authentication — single-user local use only
- `tasks.json` is not thread-safe under concurrent writes
- Task indices are positional; concurrent sessions may cause index drift
