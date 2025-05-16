from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    crime_types = ['murder', 'theft', 'arson', 'fraud']
    locations = ['warehouse', 'market', 'office', 'old_factory']
    times = ['night', 'afternoon', 'morning']
    return render_template('index.html', crime_types=crime_types, locations=locations, times=times)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    crime_type = data.get('crime_type')
    location = data.get('location')
    time = data.get('time')

    suspects = ['john', 'susan', 'alice', 'bob']

    reports = []
    for person in suspects:
        result = run_prolog_evaluation(crime_type, location, time, person)
        reports.append(result)

    # Sort by suspicion score descending
    reports.sort(key=lambda r: r['score'], reverse=True)

    best_suspect = reports[0] if reports else None

    # Return list with correct keys for frontend
    if best_suspect:
        # Rename keys to what frontend expects
        best_suspect_renamed = {
            "name": best_suspect["person"],
            "score": best_suspect["score"],
            "verdict": best_suspect["verdict"],
            "justifications": best_suspect["factors"]
        }
        return jsonify([best_suspect_renamed])
    else:
        return jsonify([])

def run_prolog_evaluation(crime_type, location, time, person):
    crime_type = crime_type.lower()
    location = location.lower()
    time = time.lower()

    score = 0
    factors = []

    motives = {
        'john': ['murder', 'theft'],
        'susan': ['arson'],
        'alice': ['fraud'],
        'bob': ['fraud', 'theft']
    }

    presence = {
        'john': [('warehouse', 'night'), ('old_factory', 'morning')],
        'susan': [('market', 'afternoon')],
        'alice': [('office', 'afternoon')],
        'bob': [('warehouse', 'night')]
    }

    weapons = {
        'john': True,
        'susan': False,
        'alice': False,
        'bob': False
    }

    alibi = {
        'john': False,
        'susan': True,
        'alice': True,
        'bob': False
    }

    if crime_type in motives.get(person, []):
        score += 35
        factors.append(f"Had motive ({crime_type}): Yes (+35 points)")
    else:
        factors.append(f"Had motive ({crime_type}): No (+0 points)")

    if (location, time) in presence.get(person, []):
        score += 30
        factors.append(f"Was at crime scene ({location}, {time}): Yes (+30 points)")
    else:
        factors.append(f"Was at crime scene ({location}, {time}): No (+0 points)")

    if weapons.get(person, False):
        score += 20
        factors.append("Had relevant weapon/item: Yes (+20 points)")
    else:
        factors.append("Had relevant weapon/item: No (+0 points)")

    if not alibi.get(person, True):
        score += 15
        factors.append("No specific alibi: Yes (+15 points)")
    else:
        factors.append("No specific alibi: No (+0 points)")

    if score >= 70:
        verdict = "⚠️ Strong suspect."
    elif score >= 40:
        verdict = "⚠️ Possible suspect."
    else:
        verdict = "✅ Not likely a suspect."

    return {
        "person": person,
        "score": score,
        "verdict": verdict,
        "factors": factors
    }


if __name__ == '__main__':
    app.run(debug=True)
