# 🌍 Country Analytics Dashboard

An interactive web dashboard built with **Python**, **Streamlit**, **Pandas**, **Plotly**, and the **REST Countries API**.

The dashboard allows users to explore country data, search countries, filter by region, sort by population or area, visualize statistics, view country flags, and download filtered data as CSV.

---

# 🚀 Features

## 🔍 Search Countries

* Search countries by name
* Case-insensitive search

## 🌎 Region Filtering

Filter countries by:

* Africa
* Americas
* Asia
* Europe
* Oceania

## 📊 Sorting

Sort countries by:

* Population (High → Low)
* Area (High → Low)

## 📈 Summary Statistics

Displays:

* Total Countries
* Average Population
* Largest Population
* Average Area

## 📉 Interactive Charts

* Top 10 Countries by Population
* Interactive Plotly Visualizations
* Hover Tooltips

## 🏳️ Country Information

View:

* Country Flag
* Capital City
* Population
* Area
* Currency
* Languages

## ⬇️ CSV Download

Download filtered data directly as a CSV file.

## ⚠️ Error Handling

* API request validation
* Network timeout handling
* User-friendly error messages

## ⏳ Loading Spinner

Displays loading progress while fetching data from the API.

---

# 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Requests
* Plotly
* REST Countries API
* Git
* GitHub

---

# 📂 Project Structure

```text
country-analytics-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── dashboard-home.png
    ├── search-country.png
    ├── population-chart.png
    └── country-details.png
```

---

# 📸 Screenshots

## Dashboard Home

![Dashboard Home](screenshots/dashboard-home.png)

## Search Country

![Search Country](screenshots/search-country.png)

## Population Chart

![Population Chart](screenshots/population-chart.png)

## Country Details

![Country Details](screenshots/country-details.png)

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/country-analytics-dashboard.git
cd country-analytics-dashboard
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a file named `requirements.txt`

```text
streamlit
pandas
requests
plotly
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```
Common Errors ModuleNotFoundError: No module named 'streamlit'

Install Streamlit:

pip install streamlit 

'streamlit' is not recognized

Run:

python -m streamlit run app.py

instead of:

streamlit run app.py

Open your browser:

http://localhost:8501
---

# 🌐 API Used

REST Countries API

Endpoint:

```text
https://restcountries.com/v3.1/all
```

Fields Used:

* name
* capital
* population
* region
* currencies
* languages
* area
* flags

---

# 📊 Dashboard Workflow

```text
REST Countries API
        ↓
API Request
        ↓
JSON Response
        ↓
Data Cleaning
        ↓
Pandas DataFrame
        ↓
Search & Filtering
        ↓
Sorting
        ↓
Summary Statistics
        ↓
Interactive Charts
        ↓
CSV Download
        ↓
Streamlit Dashboard
```

---

# 🔮 Future Enhancements

* Dark Mode
* Multiple Region Selection
* Country Comparison Tool
* Population Heatmap
* Cached API Calls
* Historical Population Trends
* Additional Data Sources
* Cloud Database Integration

---

# 🎯 Learning Outcomes

This project demonstrates:

* REST API Integration
* JSON Data Parsing
* Data Cleaning with Pandas
* Data Analysis
* Interactive Data Visualization
* Dashboard Development with Streamlit
* CSV Export Functionality
* Error Handling
* Git & GitHub Version Control
* Deployment Readiness

---

# 👨‍💻 Author

Developed as a portfolio project to showcase Python, Data Analytics, Visualization, and Dashboard Development skills.

## Connect

GitHub: [https://github.com/yourusername](https://github.com/nithyasrid)

LinkedIn: [https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/nithya-sri-d-b94b86281/)

Live Demo: [https://your-app.streamlit.app
](https://nithyasrid-country-analytics-dashboard-app-oihvjf.streamlit.app/)
