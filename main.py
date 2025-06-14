# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    

    if button_python:
        return redirect("https://www.python.org/")
    elif button_discord:
        return redirect("https://github.com/ibrahimkes/discordBot")
    elif button_html:
        return redirect("https://www.w3schools.com/html/")
    elif button_db:
        return redirect("https://www.sqlalchemy.org/")
    
    return render_template('index.html')

@app.route('/feedback.form', methods=['POST'])
def feedback_form():

    email = request.form.get("email")
    text = request.form.get("text")

    with open("feedback.txt", "a") as file:
        file.write(f"Email: {email}\n")
        file.write(f"Text: {text}\n")
        file.write("--------------")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
