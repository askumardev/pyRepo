🛠 Step 1: Set up your Flask project
Install Flask (if you haven't already):


pip install flask
Create a new project folder, say myflaskapp, and inside it, create a file named app.py.

🛠 Step 2: Create a basic Flask app
In app.py, write:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
🛠 Step 3: Run the Flask app
In the terminal, inside your project folder:


python app.py
Visit http://127.0.0.1:5000/

You should see "Hello, Flask!"

🛠 Step 4: Add a new functionality (example: show a list of posts)
Modify app.py:


from flask import Flask

app = Flask(__name__)

# Dummy data
posts = [
    {'title': 'First Post', 'content': 'This is my first post!'},
    {'title': 'Second Post', 'content': 'This is my second post!'}
]

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/posts')
def show_posts():
    output = ''
    for post in posts:
        output += f"<h2>{post['title']}</h2><p>{post['content']}</p>"
    return output

if __name__ == '__main__':
    app.run(debug=True)
🛠 Step 5: Test the functionality
Go to http://127.0.0.1:5000/ — home page

Go to http://127.0.0.1:5000/posts — list of posts displayed

🛠 Step 6 (Optional): Use templates (separate HTML files)
Create a folder called templates next to app.py.

Inside templates, create a file called posts.html:

html
Copy
Edit
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Posts</title>
</head>
<body>
  <h1>Posts</h1>
  {% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
  {% endfor %}
</body>
</html>
Update app.py to use render_template:


from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {'title': 'First Post', 'content': 'This is my first post!'},
    {'title': 'Second Post', 'content': 'This is my second post!'}
]

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/posts')
def show_posts():
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
Refresh http://127.0.0.1:5000/posts — now it uses the HTML template!