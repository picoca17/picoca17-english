from flask import Flask, render_template_string, request

app = Flask(__name__)

# Base de datos ligera con actividades por nivel para la EOI
COURSE_DATA = {
    "A1": {
        "title": "A1 - Starter / Beginners",
        "phrases": "Cheer up! Every step counts.",
        "spelling_words": ["ENGLISH", "TEACHER", "WELCOME"],
        "reading": "Read the short email from Sarah and identify her job.",
        "mediation": "Traduce/Adapta este mensaje corto a tu compañero en español."
    },
    "A2": {
        "title": "A2 - Elementary",
        "phrases": "You are doing great! Keep going.",
        "spelling_words": ["SCHOOL", "STUDENT", "LESSON"],
        "reading": "Read the notice board and answer the questions.",
        "mediation": "Resume la información del folleto para tu amigo."
    },
    "B1": {
        "title": "B1 - Intermediate",
        "phrases": "You are very welcome! Practice makes progress.",
        "spelling_words": ["TRAVEL", "EXPERIENCE", "KNOWLEDGE"],
        "reading": "Read the travel blog and complete the gap fill.",
        "mediation": "Explica la normativa de la biblioteca a tu compañero de intercambio."
    },
    "B2": {
        "title": "B2 - EOI Certification Level",
        "phrases": "Thank you very much indeed for your hard work!",
        "spelling_words": ["ACCOMMODATION", "ENVIRONMENT", "MEDIATION"],
        "reading": "Read the article about sustainable living and answer the multiple-choice questions.",
        "mediation": "Examine the chart below and summarize the key trends for your study partner."
    },
    "C1": {
        "title": "C1 - Advanced",
        "phrases": "Brilliant work! Expressing complex ideas with confidence.",
        "spelling_words": ["SUBSTANTIAL", "CONSIDERABLE", "FLUCTUATE"],
        "reading": "Analyze the academic paper excerpt and identify nuances.",
        "mediation": "Synthesize the main arguments of two articles for a panel debate."
    },
    "C2": {
        "title": "C2 - Mastery / Proficiency",
        "phrases": "Congratulations! You are operating at native-like mastery.",
        "spelling_words": ["UNPRECEDENTED", "CONSCIENTIOUS", "ONOMATOPOEIA"],
        "reading": "Analyze the opinion piece on artificial intelligence and identify implicit attitudes.",
        "mediation": "Synthesize two conflicting opinion pieces into a cohesive 150-word summary."
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>picoca17 - English Academy</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 0; }
        header { background-color: #6c5ce7; color: white; text-align: center; padding: 2rem; }
        header h1 { margin: 0; font-size: 2.5rem; }
        header p { font-size: 1.1rem; opacity: 0.9; }
        nav { display: flex; justify-content: center; background-color: #a29bfe; padding: 0.5rem; flex-wrap: wrap; }
        nav a { color: white; padding: 0.8rem 1.2rem; text-decoration: none; font-weight: bold; border-radius: 4px; }
        nav a:hover { background-color: #6c5ce7; }
        .container { max-width: 900px; margin: 2rem auto; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .exercise-box { background: #ffeaa7; border-left: 5px solid #fdcb6e; padding: 1rem; margin: 1rem 0; border-radius: 4px; }
        footer { text-align: center; padding: 1.5rem; background: #2d3436; color: white; margin-top: 2rem; }
    </style>
</head>
<body>

<header>
    <h1>picoca17 🇬🇧 ✨</h1>
    <p>Aprende inglés de forma dinámica, motivadora y aprueba tus exámenes de la EOI</p>
</header>

<nav>
    <a href="/?level=A1">Nivel A1</a>
    <a href="/?level=A2">Nivel A2</a>
    <a href="/?level=B1">Nivel B1</a>
    <a href="/?level=B2">Nivel B2</a>
    <a href="/?level=C1">Nivel C1</a>
    <a href="/?level=C2">Nivel C2</a>
</nav>

<div class="container">
    <h2>{{ data.title }}</h2>
    <p><strong>Message from picoca17:</strong> <em>"{{ data.phrases }}"</em></p>
    <p><strong>You are very welcome</strong> to practice as much as you need!</p>

    <hr>

    <h3>🔤 Spelling Bee Challenge (Deletreando)</h3>
    <p>Escucha o practica deletreando las siguientes palabras clave para la EOI:</p>
    <ul>
        {% for word in data.spelling_words %}
            <li><strong>{{ word }}</strong>: {{ word | list | join(' - ') }}</li>
        {% endfor %}
    </ul>

    <h3>📖 Reading & Comprehension</h3>
    <div class="exercise-box">
        <p>{{ data.reading }}</p>
    </div>

    <h3>🔄 Mediación (EOI Skill)</h3>
    <div class="exercise-box">
        <p>{{ data.mediation }}</p>
    </div>
</div>

<footer>
    <p>picoca17 English School &copy; 2026 | Thank you very much indeed for visiting!</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    selected_level = request.args.get("level", "B2")
    data = COURSE_DATA.get(selected_level, COURSE_DATA["B2"])
    return render_template_string(HTML_TEMPLATE, data=data)

if __name__ == "__main__":
    app.run(debug=True)
    