<p align="center"> <img src="./img.png" alt="StudyFlow Banner" width="100%"> </p>
StudyFlow – Smart Study Planner 🎯
Basic Details
Team Name: 010101
Team Members

Member 1: Fathima Nazar - ICET

Member 2: Binsha Khalid - ICET

Hosted Project Link

[Add your deployed project link here]

Project Description

StudyFlow is a smart web-based study planner that generates personalized timetables based on exam date, subject difficulty, number of modules, and available daily study hours. It intelligently distributes sessions, tracks required vs remaining hours, and includes an integrated Pomodoro timer to enhance productivity.

The Problem Statement

Students often struggle with poor time management, uneven syllabus distribution, and last-minute exam stress. Traditional planning methods do not consider difficulty level, available time, or realistic workload distribution.

The Solution

StudyFlow dynamically generates a structured study timetable based on difficulty weighting and available hours. It calculates total required study time, distributes sessions evenly, tracks remaining hours, shows progress via a progress bar, and integrates a Pomodoro timer for focused study sessions.

Technical Details
Technologies/Components Used
For Software:

Languages used: Python, HTML

Frameworks used: Flask, Bootstrap

Libraries used: Jinja2 (Flask templating)

Tools used: VS Code, Git, GitHub

For Hardware:

(Not Applicable – Software Project)

Features

Smart timetable generation based on difficulty

Dynamic hours calculation (required vs available)

Remaining hours counter

Progress tracking with visual progress bar

Exam countdown display

Integrated Pomodoro timer (Focus + Break cycles)

Clean and responsive UI

Implementation
For Software:
Installation
git clone https://github.com/yourusername/studyflow.git
cd studyflow
pip install -r requirements.txt

Run
python app.py


Visit:

http://127.0.0.1:5000/

Project Documentation
Screenshots (Add at least 3)


User inputs subject details, difficulty, exam date, and daily available hours


Auto-generated structured timetable with session distribution


Progress bar and hours remaining counter

System Architecture

Architecture Explanation:

User inputs data via HTML form

Flask backend processes input

Smart allocation algorithm calculates:

Days remaining

Required study hours

Available hours

Schedule is generated dynamically

Data rendered using Jinja templates

Frontend displays progress and Pomodoro timer

Application Workflow

Workflow:

User enters subject details

System calculates days left

Difficulty weight applied

Total required hours computed

Compare with available hours

Generate structured timetable

Display progress + Pomodoro integration

Additional Documentation
API Documentation (Internal Routes)

Base URL: http://localhost:5000

GET /

Loads input form page

POST /generate

Processes user input

Generates timetable

Returns schedule with:

total_required

remaining

progress_percent

warning (if insufficient time)

Project Demo
Video

[Add your demo video link here]

The demo showcases:

Input form submission

Smart schedule generation

Difficulty-based distribution

Progress tracking

Pomodoro timer functionality

AI Tools Used (Transparency Section)

Tool Used: ChatGPT

Purpose:

Backend logic structuring

UI improvement suggestions

Deployment guidance

Debugging assistance

Human Contributions:

Project architecture design

Custom scheduling logic adjustments

UI styling decisions

Feature implementation and testing

Team Contributions

[Your Name]: Backend logic, smart scheduling algorithm, Flask integration

[Member Name]: UI/UX design, frontend structure, styling

[Member Name]: Testing, documentation, deployment setup

License

This project is licensed under the MIT License.

Made with ❤️ for smarter exam preparation 🚀
