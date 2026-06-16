# 📺 Content Monetization Modeler

## 📌 Project Overview

The Content Monetization Modeler is a Machine Learning project designed to predict YouTube ad revenue based on video performance metrics, audience engagement, and channel statistics.

The project utilizes data preprocessing, feature engineering, regression modeling, and Streamlit deployment to provide accurate revenue predictions for content creators and digital marketers.

---

## 📸 Application Screenshots

### 🏠 Home Page

![Home Page](Screenshots/Home%20Page.png)

### 💰 Predict Revenue Page

![Prediction Page](Screenshots/Prediction%20Page.png)

### ✅ Prediction Result

![Prediction Result](Screenshots/Prediction%20Result.png)

### 📊 Visualizations Dashboard

![Visualizations](Screenshots/Visualizations%20Page.png)

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Feature Engineering
- Multiple Regression Models
- Model Evaluation using:
  - R² Score
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
- Feature Importance Analysis
- Interactive Streamlit Web Application
- Revenue Prediction in Real Time
- Business Insights & Visualizations

---

## 📂 Dataset Features

### Numerical Features

- Views
- Likes
- Comments
- Watch Time Minutes
- Video Length Minutes
- Subscribers
- Year
- Day

### Categorical Features

- Category
- Device
- Country
- Month

### Target Variable

- Ad Revenue (USD)

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Manipulation |
| NumPy | Numerical Operations |
| Scikit-Learn | Machine Learning |
| Streamlit | Web Application |
| Matplotlib | Data Visualization |
| Pickle | Model Serialization |
| GitHub | Version Control |

---

## 🤖 Machine Learning Models

The following regression algorithms were implemented and compared:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. K-Nearest Neighbors (KNN) Regressor

---

## 📊 Model Performance

| Model | R² Score | MAE | RMSE |
|--------|---------|------|------|
| Linear Regression | 0.9519 | 3.17 | 13.60 |
| Gradient Boosting Regressor | 0.9517 | 3.69 | 13.64 |
| Random Forest Regressor | 0.9510 | 3.99 | 13.74 |
| Decision Tree Regressor | 0.8921 | 5.79 | 20.38 |
| KNN Regressor | 0.6622 | 29.06 | 36.06 |

### 🏆 Best Model

**Linear Regression**

- R² Score: 0.9519
- MAE: 3.17
- RMSE: 13.60

---

## 📈 Key Insights

- Watch Time Minutes is the strongest predictor of ad revenue.
- Likes and comments significantly improve monetization.
- Higher audience engagement leads to higher earnings.
- Views positively impact revenue but are less influential than watch time.
- Seasonal effects were observed during certain months.
- Audience engagement is more important than views alone.

---

## 📊 Visualizations Included

- Feature Importance Analysis
- Regression Model Comparison
- Revenue Driver Analysis
- Revenue Growth Trend
- Model Performance Dashboard

---

## 📁 Project Structure

```text
CONTENT MONETIZATION MODELER PROJECT/
│
├── Report/
│   └── Content Monetization Modeler Report.pdf
│
├── Screenshots/
│   ├── Home Page.png
│   ├── Prediction Page.png
│   ├── Prediction Result.png
│   └── Visualizations Page.png
│
├── model.py
├── monetization analysis.ipynb
├── README.md
├── requirements.txt
├── scaler.pkl
├── youtube_ad_revenue_dataset.csv
└── youtube_ad_revenue_model.pkl
```

---

## ▶️ How to Run the Application

### Clone Repository

```bash
git clone https://github.com/yourusername/content-monetization-modeler.git
cd content-monetization-modeler
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run model.py
```

or

```bash
python -m streamlit run model.py
```

---

## 📦 Requirements

```text
streamlit
pandas
numpy
matplotlib
scikit-learn
```

---

## 🌐 Streamlit Application

The application allows users to:

- Enter YouTube video metrics
- Select category, device, country, and month
- Predict expected ad revenue
- View business insights
- Explore model performance visualizations

---

## 🎯 Project Outcomes

✔ Cleaned and processed YouTube analytics data

✔ Built and evaluated five regression models

✔ Achieved 95.19% prediction accuracy (R² Score)

✔ Identified key drivers of YouTube ad revenue

✔ Developed an interactive Streamlit application

✔ Generated actionable business insights

---

## 🔮 Future Enhancements

- Integration with YouTube Analytics API
- Real-time revenue forecasting
- Advanced models such as XGBoost and LightGBM
- Cloud deployment
- Personalized creator recommendations

---

