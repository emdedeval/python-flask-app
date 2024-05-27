from flask import Flask, render_template_string, request, redirect, url_for
from urllib.parse import quote

def create_app():
    app = Flask(__name__)

    # Home route
    @app.route('/')
    def home():
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Welcome</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; }
                    .container { text-align: center; padding: 50px; }
                    h1 { color: #4CAF50; }
                    a { color: #4CAF50; text-decoration: none; }
                    a:hover { text-decoration: underline; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Well done!</h1>
                    <p>You successfully deployed your Flask app. Now you can start building your app.</p>
                    <p><a href="{{ url_for('greet', name='World') }}">Greet the World</a></p>
                    <p><a href="{{ url_for('quote_example', text='Flask is great!') }}">See URL Encoding Example</a></p>
                </div>
            </body>
            </html>
        """)

    # Greeting route
    @app.route('/greet/<name>')
    def greet(name):
        return f'Hello, {quote(name)}! Welcome to your Flask app.'

    # URL Encoding example route
    @app.route('/quote/<text>')
    def quote_example(text):
        encoded_text = quote(text)
        return f'Original: {text} <br> Encoded: {encoded_text}'

    # Simple form example route
    @app.route('/form', methods=['GET', 'POST'])
    def form():
        if request.method == 'POST':
            name = request.form.get('name')
            return redirect(url_for('greet', name=name))
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Submit Your Name</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; }
                    .container { text-align: center; padding: 50px; }
                    input[type="text"] { padding: 10px; width: 200px; }
                    input[type="submit"] { padding: 10px 20px; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Submit Your Name</h1>
                    <form method="post">
                        <input type="text" name="name" placeholder="Enter your name">
                        <input type="submit" value="Submit">
                    </form>
                </div>
            </body>
            </html>
        """)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
