from flask import Flask, render_template, request, jsonify
from pyswip import Prolog

app = Flask(__name__)
prolog = Prolog()
prolog.consult('crime.pl')  

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
        query = f"score({person}, {crime_type}, {location}, {time}, Score, Justifications)"
        results = list(prolog.query(query))
        if results:
            res = results[0]
            score = res['Score']
            justifications = res['Justifications']
            if score >= 70:
                verdict = " Strong suspect."
            elif score >= 40:
                verdict = " Possible suspect."
            else:
                verdict = " Not likely a suspect."

            reports.append({
                "person": person,
                "score": score,
                "verdict": verdict,
                "factors": justifications
            })

    reports.sort(key=lambda r: r['score'], reverse=True)
    best_suspect = reports[0] if reports else None
    return jsonify([best_suspect] if best_suspect else [])

if __name__ == '__main__':
    app.run(debug=True)
