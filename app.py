from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "recovery_data.json"

# Inicialize as variáveis globais
participant_data = {}
celebration_dates = {}
messages = []

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data_to_file(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/meetings")
def meetings():
    return render_template("meetings.html")

@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    global messages, celebration_dates, participant_data

    data = load_data()
    message = messages.pop(0) if messages else ""

    if request.method == "POST":
        if "name" in request.form and "days_clean" in request.form:
            name = request.form.get("name").strip()
            days_clean = request.form.get("days_clean").strip()
            if name and days_clean.isdigit():
                data[name] = int(days_clean)
                save_data_to_file(data)
                messages.append(f"Updated recovery time for {name}!")
                participant_data = data # Atualiza a variável global
                return redirect(url_for('calendar'))
            else:
                messages.append("Please, enter a valid name and number of days.")
                return redirect(url_for('calendar'))
        elif "celebration_date" in request.form and "celebration_description" in request.form:
            celebration_date = request.form.get("celebration_date")
            celebration_description = request.form.get("celebration_description")
            if celebration_date and celebration_description:
                celebration_dates[celebration_date] = celebration_description
                messages.append(f"Celebration '{celebration_description}' saved to {celebration_date}!")
                return redirect(url_for('calendar'))
            else:
                messages.append("Please, fill in the date and description of the celebration.")
                return redirect(url_for('calendar'))

    participant_data = data # Carrega os dados para a variável global ao carregar a página
    return render_template("calendar.html", data=participant_data, message=message, celebrations=celebration_dates)

@app.route('/delete_celebration', methods=['POST'])
def delete_celebration():
    global celebration_dates, messages
    date_to_delete = request.form.get('date')
    if date_to_delete in celebration_dates:
        del celebration_dates[date_to_delete]
        messages.append(f"Celebration of {date_to_delete} deleted!")
    return redirect(url_for('calendar'))

@app.route('/delete_participant', methods=['POST'])
def delete_participant():
    global participant_data, messages
    name_to_delete = request.form.get('name')
    data = load_data()
    if name_to_delete in data:
        del data[name_to_delete]
        save_data_to_file(data)
        participant_data = data # Atualiza a variável global
        messages.append(f"Participant {name_to_delete} deleted!")
    return redirect(url_for('calendar'))

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    participant_data = load_data() # Carrega os dados ao iniciar o app
    app.run(debug=True)