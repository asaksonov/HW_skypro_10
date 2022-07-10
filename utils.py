import json

def load_json():
    with open("candidates.json", "r", encoding = 'utf8') as file:
        candidates = json.load(file)
        return candidates

def format_candidates(candidates: list[dict]):
    """Форматирование спискв кандидадтов"""
    result = '<pre>'

    for candidate in candidates:
        result += f"""
             {candidate['name']}\n
             {candidate['position']}\n
             {candidate['skills']}\n
         """
    result += '</pre>'
    return result

def get_all_candidates():
    return load_json()

def get_candidate_by_id(uid: int):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['pk'] == uid:
            return candidate
    return None

def get_candidate_by_skill(skill: str):
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result