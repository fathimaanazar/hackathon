from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database Setup
def init_db():
    conn = sqlite3.connect('studyflow.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            difficulty INTEGER,
            syllabus INTEGER,
            priority REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()


@app.route('/')
def index():
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', today=today)


@app.route('/generate', methods=['POST'])
def generate():
    exam_date = request.form['exam_date']
    daily_hours = int(request.form['daily_hours'])

    subjects = request.form.getlist('subject')
    difficulties = request.form.getlist('difficulty')
    syllabus_sizes = request.form.getlist('syllabus')

    today = datetime.today()
    exam = datetime.strptime(exam_date, "%Y-%m-%d")

    # ✅ Restrict past dates
    if exam.date() <= today.date():
        return "Error: Please select a future exam date."

    total_days = (exam - today).days

    plans = []

    for i in range(len(subjects)):
        # Skip empty rows
        if subjects[i] and difficulties[i] and syllabus_sizes[i]:
            difficulty = int(difficulties[i])
            syllabus = int(syllabus_sizes[i])

            priority = difficulty * syllabus

            plans.append({
                "subject": subjects[i],
                "difficulty": difficulty,
                "syllabus": syllabus,
                "priority": priority
            })

    # Sort subjects by priority
    plans.sort(key=lambda x: x['priority'], reverse=True)

    # Prevent division by zero
    total_priority = sum(p['priority'] for p in plans)

    if total_priority == 0:
        return "Error: Please enter valid subject details."

    # Distribute hours
    for p in plans:
        p['allocated_hours'] = round(
            (p['priority'] / total_priority) * daily_hours, 2
        )

    return render_template(
        'result.html',
        plans=plans,
        total_days=total_days
    )
if __name__ == '__main__':
    app.run(debug=True)