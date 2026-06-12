# 🎓 Student Engagement Monitor

An AI-powered real-time student engagement monitoring system built using **Python, OpenCV, MediaPipe, Streamlit, and Plotly**.

The system uses facial landmark detection, blink analysis, and head pose estimation to classify student engagement levels during online learning sessions and displays the results through an interactive dashboard.

---

## 🚀 Features

* Real-time webcam-based face tracking
* MediaPipe Face Mesh integration
* Eye Aspect Ratio (EAR) based blink detection
* Head pose (yaw) estimation
* Engagement classification:

  * ✅ Attentive
  * 🤔 Confused
  * ⚠️ Distracted
  * 🚫 No Face Detected
* Automatic CSV session logging
* Interactive Streamlit dashboard
* Real-time engagement analytics and visualizations

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy
* Pandas
* Streamlit
* Plotly

---

## 📂 Project Structure

```text
student_engagement_monitor/
│
├── logs/
│   └── session_*.csv
│
├── app.py
├── realtime_monitor.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/SaiPraneethGadala/student_engagement_monitor.git
cd student_engagement_monitor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Start Real-Time Monitoring

```bash
python realtime_monitor.py
```

The webcam will start capturing facial landmarks and tracking engagement.

### Step 2: Launch Dashboard

Open a new terminal and run:

```bash
streamlit run app.py
```

The dashboard will display:

* Engagement Summary
* Live Session Tracking
* Engagement Breakdown Charts
* Timeline Analysis
* Session Logs

---

## 📊 Engagement Classification Logic

### ✅ Attentive

* Looking at screen
* Normal blink rate
* Low head yaw angle

### 🤔 Confused

* Excessive blinking
* Increased eye activity

### ⚠️ Distracted

* Looking away from screen
* High head yaw angle

### 🚫 No Face

* Face not detected by camera

---

## 🎯 Applications

* Smart Classrooms
* Online Learning Platforms
* Educational Analytics
* Student Attention Monitoring
* AI-Based Learning Systems

---

## 🔮 Future Enhancements

* Multi-student tracking
* Emotion recognition
* Attendance management
* Cloud database integration
* Teacher alert system
* Advanced analytics dashboard

---

## 👨‍💻 Author

**Sai Praneeth**

B.Tech – Computer Science & Engineering (AI & ML)

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
