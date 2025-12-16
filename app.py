from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key-123'

# Contact Form
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=100)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Send Message')

# Resume Data
resume_data = {
    "personal_info": {
        "name": "Rajeshkumar K",
        "title": "Python Developer",
        "email": "rajeshraj8558@gmail.com",
        "phone": "+91 8248190818",
        "location": "Vellore",
        "github": "https://github.com/Rajeshraj8558",
        "linkedin": "#"
    },
    
    "summary": "Aspiring Python Full Stack Developer with a strong foundation in Python, Django, SQL, and front-end technologies such as HTML, CSS, JavaScript, and Bootstrap. Passionate about developing scalable web applications and contributing to impactful projects. Experienced with development workflows using GitHub and Visual Studio Code. A quick learner with a passion for back-end development, problem solving, and building scalable web applications.",
    
    "projects": [
        {
            "title": "Voice Based Email for Visually Impaired People",
            "description": "Developed an innovative Voice-Based Email system to enhance communication for visually impaired individuals.",
            "details": [
                "Collaborated on the design and development of an Android application",
                "Allows seamless email communication through voice commands",
                "Built with Java, SQL Database, XML, HTML, CSS, JavaScript"
            ],
            "technologies": ["HTML", "CSS", "JavaScript", "XML", "Java", "SQL Database"],
            "github_link": "#"
        },
        {
            "title": "Personal Portfolio Website",
            "description": "Dynamic portfolio website with authentication system and content management.",
            "details": [
                "Implemented user authentication (sign-up, login, logout)",
                "Secure access to website features",
                "Built with Django and SQLite"
            ],
            "technologies": ["Bootstrap", "Python", "Django", "SQLite"],
            "github_link": "#"
        },
        {
            "title": "Study Learning Web Platform",
            "description": "Web-based learning platform for course management and interactive learning.",
            "details": [
                "User authentication and authorization",
                "Create and manage courses",
                "Explore different topics interactively"
            ],
            "technologies": ["HTML", "CSS", "JavaScript", "Python", "Django", "SQLite"],
            "github_link": "#"
        },
        {
            "title": "Employee Management System (CRUD)",
            "description": "Employee management system for managing personal records and details.",
            "details": [
                "Implemented CRUD operations (Create, Read, Update, Delete)",
                "Efficient management of employee reports",
                "User-friendly interface for data management"
            ],
            "technologies": ["Python", "Django", "SQLite"],
            "github_link": "#"
        },
        {
            "title": "Social Media Integration Web Page",
            "description": "Responsive webpage with social media integration for improved engagement.",
            "details": [
                "Responsive design using Bootstrap",
                "Social media icons integration",
                "Seamless user interaction across devices"
            ],
            "technologies": ["Bootstrap", "Python", "Django", "SQLite"],
            "github_link": "#"
        }
    ],
    
    "skills": {
        "programming": ["Python", "JavaScript (basic)", "HTML", "CSS"],
        "frameworks": ["Django", "Bootstrap", "RESTful APIs", "NumPy", "Pandas"],
        "databases": ["SQL", "SQLite"],
        "tools": ["Git", "GitHub", "Visual Studio Code"],
        "soft_skills": ["Quick Learner", "Data Structures & Algorithms", "Problem-Solving", "Team Collaboration", "Debugging using ChatGPT"]
    },
    
    "education": [
        {
            "degree": "M.Sc. Computer Science",
            "institution": "Govt. Thirumagal Mill's College, Thiruvalluvar University",
            "duration": "2022‑2024",
            "location": "Vellore",
            "score": "CGPA: 7.9/10"
        },
        {
            "degree": "B.Sc. Computer Science",
            "institution": "Muthurangam Govt. Arts College, Thiruvalluvar University",
            "duration": "2019‑2022",
            "location": "Vellore",
            "score": "CGPA: 6.2/10"
        }
    ],
    
    "certifications": [
        {
            "name": "Programming in Python",
            "issuer": "META"
        },
        {
            "name": "Crash Course on Python",
            "issuer": "Google"
        }
    ]
}

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/')
def home():
    return render_template('index.html', data=resume_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=resume_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Here you would typically save to database or send email
        flash('Your message has been sent successfully! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', form=form, data=resume_data)

@app.route('/api/resume')
def api_resume():
    return jsonify(resume_data)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)