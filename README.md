# bondandharvey – Bond and Harvey Food Menu & Cart

POS food menu site for **Bond and Harvey**. Browse items, add to cart, visible cart. Built with Flask and optimized so **searching "bondandharvey"** can rank your site on top in Google.

## Features

- **Food menu**: Mains, Salads, Sides, Drinks, Desserts
- **Cart**: Add to cart; cart visible in side panel with total
- **Search**: Filter by category and search box
- **SEO**: Title/keywords include "bondandharvey", JSON-LD (Restaurant + alternateName), sitemap, robots.txt

---

## Free hosting (so "bondandharvey" can be found on Google)

Your site must be **public on the internet** for Google to index it. These options are **free**:

### Option A: Render.com (recommended)

1. Push this project to a **GitHub** repo.
2. Go to [render.com](https://render.com) → Sign up (free) → **New → Web Service**.
3. Connect your GitHub repo and select this project.
4. Settings:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
   - **Plan:** Free
5. Deploy. Your site will be at:  
   `https://YOUR-SERVICE-NAME.onrender.com`  
   To get "bondandharvey" in the URL, name the service **bondandharvey** so the URL is:  
   **https://bondandharvey.onrender.com**

### Option B: PythonAnywhere (URL bondandharvey.pythonanywhere.com)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com) (free account).
2. Create a new **Web app** → Flask → Python 3.10.
3. In **Consoles** open a Bash console and:
   ```bash
   cd ~/bondandharvey   # or clone your repo here
   pip install -r requirements.txt --user
   ```
4. In the **Web** tab:
   - **Source code:** your project folder (e.g. `/home/YourUsername/bondandharvey`)
   - **WSGI file:** edit and set application to your Flask app, e.g.:
     ```python
     import sys
     path = '/home/YourUsername/bondandharvey'
     if path not in sys.path:
         sys.path.append(path)
     from app import app as application
     ```
   - **Static files:** URL `/static/`, directory `.../bondandharvey/static`
5. **Reload** the web app.  
   Your URL will be: **https://YourUsername.pythonanywhere.com**  
   To get "bondandharvey" in the URL, choose username **bondandharvey** when signing up so the site is:  
   **https://bondandharvey.pythonanywhere.com**

---

## Getting "bondandharvey" to show on top in Google

1. **Use "bondandharvey" in the URL**  
   - Render: name the service **bondandharvey** → `https://bondandharvey.onrender.com`  
   - PythonAnywhere: create account with username **bondandharvey** → `https://bondandharvey.pythonanywhere.com`

2. **Submit your site to Google**  
   - Go to [Google Search Console](https://search.google.com/search-console).  
   - Add property with your live URL (e.g. `https://bondandharvey.onrender.com`).  
   - Submit your sitemap: `https://bondandharvey.onrender.com/sitemap.xml`

3. **Wait for indexing**  
   - After a few days, search **bondandharvey** in Google.  
   - With no other site using that name, your official site usually appears at or near the top.

4. **Already done in this project**  
   - Page title: "bondandharvey – Bond and Harvey Food Menu & Order Online"  
   - Meta description and keywords include "bondandharvey"  
   - Footer and JSON-LD use "bondandharvey" / alternateName  
   - Sitemap and robots.txt are served for crawlers  

---

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

- Local: **http://127.0.0.1:5000**
- Same network: **http://YOUR_IP:5000**

---

## Project layout

```
sample/
├── app.py              # Flask app, routes, food data, sitemap/robots
├── requirements.txt    # Flask, gunicorn
├── Procfile            # For Render/Heroku-style hosts
├── render.yaml         # Optional Render blueprint
├── runtime.txt         # Optional Python version
├── README.md
├── static/
│   └── style.css
└── templates/
    ├── base.html       # SEO meta, JSON-LD (Restaurant + alternateName bondandharvey)
    └── index.html      # Menu grid + cart
```
