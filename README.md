# AI + Data Consultancy Marketing Site

A minimal Flask + Jinja + Tailwind (CDN) marketing website focused on inbound client conversion.

## Stack

- Python (Flask)
- Jinja templates
- Tailwind CSS via CDN (no build step)
- Minimal vanilla JavaScript
- No database

## Project Structure

```text
.
|- app.py
|- requirements.txt
|- Dockerfile
|- templates/
|  |- base.html
|  |- index.html
|  |- case_studies.html
|- static/
|  |- site.css
|  |- site.js
```

## Local Run

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate it:

```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the app:

```bash
python app.py
```

5. Open:

```text
http://127.0.0.1:5000
```

## Routes

- `/` -> Landing page
- `/case-studies` -> Case studies page

## Docker

Build image:

```bash
docker build -t ai-data-site .
```

Run container:

```bash
docker run -p 5000:5000 ai-data-site
```

Open:

```text
http://127.0.0.1:5000
```

## Deployment Notes

This app is designed for single-container deployment on platforms like:

- Google Cloud Run
- Render
- Fly.io
- Railway
- Any Docker-compatible host

Use the included `Dockerfile` as-is for a straightforward deployment path.

## Content Editing Guide

- Main data blocks (services/process/proof/tools/case cards): `app.py`
- Shared layout (nav/footer/meta): `templates/base.html`
- Landing page sections: `templates/index.html`
- Case study content: `templates/case_studies.html`
- Theme and component styles: `static/site.css`
- Mobile nav + contact form behavior: `static/site.js`

## Placeholders to Replace

- Brand label in nav/footer: `&lt;YOUR COMPANY NAME&gt;`
- Contact email: `hello@yourcompany.com`
