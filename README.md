
# CrimeNet 🔍🕵️‍♂️

CrimeNet is an expert system for crime detection built using **Prolog** as the inference engine, with a **Python Flask** backend and a **HTML/CSS** frontend. The system allows users to input facts and evidence related to a crime and uses logical reasoning to identify the possible crime committed.

---

## 🧠 Project Overview

This system simulates an intelligent expert system that can help identify crimes based on facts and clues provided. It uses **Prolog rules** and facts to reason about criminal activities, such as theft, murder, kidnapping, etc.

---

## 🛠️ Technologies Used

- **Prolog** – Crime detection rules and logic (`crime.pl`)
- **Python (Flask)** – Backend server to interface with Prolog
- **HTML5/CSS3** – User Interface
- **SWI-Prolog** – Prolog runtime engine

---

## 📂 Project Structure

```
CrimeNet/
├── crime.pl                 # Prolog file with rules and knowledge base
├── app.py                   # Flask application
├── templates/
│   └── index.html           # Frontend UI (HTML)
├── static/
│   └── style.css            # Stylesheet
├── README.md                # This file
├── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- SWI-Prolog installed
- Flask installed

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Darshinibalu/CrimeNet.git
cd CrimeNet
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Make sure **SWI-Prolog** is installed and available in your system path.

### Running the Project

Start the Flask server:

```bash
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 👩‍💻 How It Works

1. User inputs information about a crime (e.g., location, time, weapon used).
2. Flask sends the data to the Prolog engine.
3. Prolog evaluates the rules in `crime.pl` to infer the most probable crime.
4. The result is returned and displayed on the web page.

---

## 📸 Screenshots

https://ik.imagekit.io/x7u7hyl86/Screenshot%202025-05-15%20203816.png
https://ik.imagekit.io/x7u7hyl86/Screenshot%202025-05-15%20203833.png
---

## 📌 Future Improvements

- Add user authentication
- Include a database to store past cases
- Add more complex Prolog logic and crime scenarios
- Create a REST API for third-party integration

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Acknowledgements

- SWI-Prolog
- Flask documentation
- Frontend design inspirations from various sources

---
