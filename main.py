from flask import Flask
from utils import load_json, get_all_candidates, format_candidates, get_candidate_by_id, get_candidate_by_skill
app = Flask(__name__)

@app.route("/")

def page_main():
    """Главная страница"""
    candidates = get_all_candidates()
    result = format_candidates(candidates)
    return result


@app.route('/candidate/<int:uid>')

def page_candidate(uid):
    """Поиск кандидата по ID"""
    candidate = get_candidate_by_id(uid)
    result = f'<img_src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result

@app.route('/skills/<skill>')

def page_skills(skill):
    """Поиск кандидата по навыку"""
    skill_lower = skill.lower()
    candidates = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result
app.run()