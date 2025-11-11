import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import process
import random

QA_MAP = {
    "what should we know about your life story in a few sentences?":
        "I am Manu Singh, a final-year IT student at BPPIMT, skilled in Python, Django, FastAPI, and AI projects. "
        "I have built AI assistants, web applications, and worked with APIs and databases.",

    "what’s your #1 superpower?":
        "My problem-solving skills and ability to quickly learn and apply new technologies.",

    "what are the top 3 areas you’d like to grow in?":
        "I’d like to grow in three main areas — first, Artificial Intelligence, especially in applying LLMs and retrieval systems for real-world use cases. "
        "Second, backend system design and API development, since I’ve built several FastAPI and Django projects and want to deepen my expertise in scalable architecture. "
        "And third, cloud technologies and MLOps, to learn how to deploy and maintain AI applications efficiently on cloud platforms.",

    "what misconception do your coworkers have about you?":
        "People sometimes assume that since I’ve worked on UI/UX design, I’m more of a front-end person but I’m actually deeply passionate about backend and AI development.",

    "how do you push your boundaries and limits?":
        "I challenge myself with complex projects, practice coding daily, participate in competitions, "
        "and continuously learn new frameworks and technologies.",

    "can you tell me about a project you built?":
        "I built CampusMate, an AI-powered assistant using LangChain and FastAPI, "
        "allowing users to query PDFs up to 200 MB in seconds, with sub-2s responses and a Streamlit frontend.",

    "what technical skills do you have?":
        "I am skilled in Python, C++, C, HTML, and SQL. "
        "I use tools like GitHub, Postman, Figma, VS Code, and Render for development and deployment. "
        "My experience covers frameworks like Django, Django REST Framework, FastAPI, Streamlit, LangChain, and Bootstrap. "
        "I also understand core concepts such as Retrieval-Augmented Generation and Vector Databases.",

    "what achievements are you proud of?":
        "I ranked in the top 300 in CodeQuezt #21, "
        "led my cricket team to first place at BPPIMT, "
        "and successfully built and deployed two live web applications "
        "an Eco Park Ticket Booking System and an AI-powered CampusMate Assistant.",

    "have you done any certifications?":
        "Yes, I am an Oracle Certified Generative AI Professional and completed Django Essentials from Infosys Springboard.",

    "how do you handle team leadership?":
        "I have experience leading teams, like being captain of my cricket team, "
        "and collaborating with developers and designers on projects to meet deadlines efficiently."
}


def listen_and_transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Error: Speech recognition service failed."


def generate_answer(transcript):
    
    greetings = [
        "Sure, here's what I’d say.",
        "Hi there! Let me tell you.",
        "Glad you asked! Here’s my response.",
        "Of course! Here's my answer."
    ]

    question, score = process.extractOne(transcript.lower(), QA_MAP.keys())
    if score > 60:
        greeting = random.choice(greetings)
        return f"{greeting} {QA_MAP[question]}"
    return "Sorry, I can only answer a limited set of questions."


def speak(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()
