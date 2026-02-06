"""
Bond and Harvey - POS Food Menu & Cart
Flask backend for food items and cart; SEO-friendly.
"""
from flask import Flask, render_template, jsonify, request, send_from_directory
from pathlib import Path

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# Sample food items (POS-style catalog)
FOOD_ITEMS = [
    {"id": 1, "name": "Classic Burger", "price": 12.99, "category": "Mains", "description": "Beef patty, lettuce, tomato, house sauce."},
    {"id": 2, "name": "Fish & Chips", "price": 14.99, "category": "Mains", "description": "Beer-battered cod, crispy fries, tartar sauce."},
    {"id": 3, "name": "Caesar Salad", "price": 9.99, "category": "Salads", "description": "Romaine, parmesan, croutons, Caesar dressing."},
    {"id": 4, "name": "Margherita Pizza", "price": 11.99, "category": "Mains", "description": "Tomato, mozzarella, basil."},
    {"id": 5, "name": "Grilled Chicken Wrap", "price": 10.99, "category": "Mains", "description": "Grilled chicken, greens, ranch in a tortilla."},
    {"id": 6, "name": "French Fries", "price": 4.99, "category": "Sides", "description": "Crispy golden fries with salt."},
    {"id": 7, "name": "Onion Rings", "price": 5.99, "category": "Sides", "description": "Crispy battered onion rings."},
    {"id": 8, "name": "Iced Tea", "price": 2.99, "category": "Drinks", "description": "House-brewed iced tea."},
    {"id": 9, "name": "Fresh Lemonade", "price": 3.49, "category": "Drinks", "description": "Fresh-squeezed lemonade."},
    {"id": 10, "name": "Chocolate Brownie", "price": 6.99, "category": "Desserts", "description": "Warm brownie with chocolate sauce."},
    {"id": 11, "name": "Apple Pie", "price": 5.99, "category": "Desserts", "description": "Classic apple pie, slice."},
    {"id": 12, "name": "Greek Salad", "price": 10.99, "category": "Salads", "description": "Cucumber, tomato, feta, olives, oregano."},
]


@app.route("/")
def index():
    """Main menu page - SEO-optimized."""
    base_url = request.url_root.rstrip("/")
    return render_template("index.html", items=FOOD_ITEMS, base_url=base_url)


@app.route("/api/items")
def api_items():
    """API: list all food items (for search/filter)."""
    category = request.args.get("category")
    q = (request.args.get("q") or "").strip().lower()
    items = FOOD_ITEMS
    if category:
        items = [i for i in items if i["category"] == category]
    if q:
        items = [
            i for i in items
            if q in i["name"].lower() or q in (i.get("description") or "").lower()
        ]
    return jsonify(items)


@app.route("/sitemap.xml")
def sitemap():
    """Sitemap for search engines (absolute URLs for SEO)."""
    base = request.url_root.rstrip("/")
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{base}/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>'''
    return xml, 200, {"Content-Type": "application/xml"}


@app.route("/robots.txt")
def robots():
    """Robots.txt for crawlers (absolute Sitemap URL)."""
    base = request.url_root.rstrip("/")
    text = f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n"
    return text, 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    import os
    Path("static").mkdir(exist_ok=True)
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() in ("1", "true", "yes")
    app.run(host="0.0.0.0", port=port, debug=debug)
