Backend 
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('aidashgen.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_stats
                 (email TEXT PRIMARY KEY, views INTEGER, likes INTEGER, comments INTEGER, published INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, title TEXT, views TEXT, comments TEXT, status TEXT)''')
    conn.commit()
    conn.close()

@app.route('/api/stats', methods=['GET', 'POST'])
def handle_stats():
    conn = sqlite3.connect('aidashgen.db')
    c = conn.cursor()
    if request.method == 'POST':
        data = request.json
        c.execute('INSERT OR REPLACE INTO user_stats VALUES (?, ?, ?, ?, ?)',
                  (data['email'], data['views'], data['likes'], data['comments'], data['published']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Saved"}), 200
    else:
        email = request.args.get('email')
        c.execute('SELECT views, likes, comments, published FROM user_stats WHERE email=?', (email,))
        row = c.fetchone()
        conn.close()
        if row:
            return jsonify({"views": row[0], "likes": row[1], "comments": row[2], "published": row[3]})
        return jsonify({"views": 0, "likes": 0, "comments": 0, "published": 0})

@app.route('/api/articles', methods=['GET', 'POST', 'DELETE'])
def handle_articles():
    conn = sqlite3.connect('aidashgen.db')
    c = conn.cursor()

    if request.method == 'POST':
        data = request.json
        c.execute('INSERT INTO articles (email, title, views, comments, status) VALUES (?, ?, ?, ?, ?)',
                  (data['email'], data['title'], '0', '0', 'Published'))
        conn.commit()
        conn.close()
        return jsonify({"message": "Article Added"}), 200

    elif request.method == 'DELETE':
        data = request.json
        email = data.get('email')
        title = data.get('title')
        # Delete by email + title (deletes the most recently added match)
        c.execute('''DELETE FROM articles WHERE id = (
                        SELECT id FROM articles WHERE email=? AND title=? ORDER BY id DESC LIMIT 1
                     )''', (email, title))
        conn.commit()
        conn.close()
        return jsonify({"message": "Article Deleted"}), 200

    else:  # GET
        email = request.args.get('email')
        c.execute('SELECT title, views, comments, status FROM articles WHERE email=? ORDER BY id DESC', (email,))
        rows = c.fetchall()
        conn.close()
        articles = [{"title": r[0], "views": r[1], "comments": r[2], "status": r[3]} for r in rows]
        return jsonify(articles)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)