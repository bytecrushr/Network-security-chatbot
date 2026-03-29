# SecureBot — Network Security Chatbot

## Project Overview
A Flask-based network security chatbot built for an IBM Internship project (BCAIN661C) by Piyush Sahu (24-BCA-3209).

## Architecture
- **Backend**: Python 3.11 + Flask (runs on port 5000)
- **Frontend**: Single-page HTML/CSS/JS served via Flask's `render_template`
- **No database** — knowledge base and quiz pool are in-memory Python data structures

## Key Files
- `main.py` — Flask app with all chatbot logic, routes, and knowledge base
- `templates/index.html` — Chat UI (dark themed, responsive)

## Features
- 15 Q&A topics on Network Security
- Glossary of 12 security terms
- Interactive 5-question quiz (randomly sampled from 8 questions)
- Quick-action buttons for common topics
- Typing indicator animation
- Session-based quiz tracking (in-memory dict)

## Running
The app is configured as a workflow: `python main.py` on port 5000.
