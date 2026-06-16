import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Load Scaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# Load Model
with open("youtube_ad_revenue_model.pkl", "rb") as file:
    model = pickle.load(file)

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio(
    "Go To",
    ["Home", "Predict Revenue", "Visualizations"]
)

# ==========================
# HOME PAGE
# ==========================
if selection == "Home":

    st.title("📺 YouTube Ad Revenue Prediction")

    st.write("""
    This application predicts YouTube Ad Revenue using Machine Learning.

    Features used:
    - Views
    - Likes
    - Comments
    - Watch Time Minutes
    - Video Length Minutes
    - Subscribers
    - Category
    - Device
    - Country
    - Month

    Model Performance:
    - R² Score: 0.9519
    - MAE: 3.17
    - RMSE: 13.60

    Best Model: Linear Regression
    """)

# ==========================
# PREDICTION PAGE
# ==========================
elif selection == "Predict Revenue":

    st.title("💰 Predict YouTube Ad Revenue")

    col1, col2 = st.columns(2)

    with col1:
        views = st.number_input("Views", min_value=0, value=10000)
        likes = st.number_input("Likes", min_value=0, value=1000)
        comments = st.number_input("Comments", min_value=0, value=100)
        watch_time_minutes = st.number_input(
            "Watch Time Minutes",
            min_value=0.0,
            value=5000.0
        )
        video_length_minutes = st.number_input(
            "Video Length Minutes",
            min_value=0.0,
            value=10.0
        )

    with col2:
        subscribers = st.number_input(
            "Subscribers",
            min_value=0,
            value=100000
        )

        category = st.selectbox(
            "Category",
            [
                "Education",
                "Entertainment",
                "Gaming",
                "Lifestyle",
                "Music",
                "Tech"
            ]
        )

        device = st.selectbox(
            "Device",
            [
                "Desktop",
                "Mobile",
                "TV",
                "Tablet"
            ]
        )

        country = st.selectbox(
            "Country",
            [
                "AU",
                "CA",
                "DE",
                "IN",
                "UK",
                "US"
            ]
        )

        month = st.selectbox(
            "Month",
            [
                "April",
                "August",
                "December",
                "February",
                "January",
                "July",
                "June",
                "March",
                "May",
                "November",
                "October",
                "September"
            ]
        )

    year = st.number_input(
        "Year",
        min_value=2020,
        max_value=2035,
        value=2025
    )

    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=1
    )

    if st.button("Predict Revenue"):

        data = {
            'views': views,
            'likes': likes,
            'comments': comments,
            'watch_time_minutes': watch_time_minutes,
            'video_length_minutes': video_length_minutes,
            'subscribers': subscribers,
            'year': year,
            'day': day,

            'category_Entertainment': 0,
            'category_Gaming': 0,
            'category_Lifestyle': 0,
            'category_Music': 0,
            'category_Tech': 0,

            'device_Mobile': 0,
            'device_TV': 0,
            'device_Tablet': 0,

            'country_CA': 0,
            'country_DE': 0,
            'country_IN': 0,
            'country_UK': 0,
            'country_US': 0,

            'month_August': 0,
            'month_December': 0,
            'month_February': 0,
            'month_January': 0,
            'month_July': 0,
            'month_June': 0,
            'month_March': 0,
            'month_May': 0,
            'month_November': 0,
            'month_October': 0,
            'month_September': 0
        }

        # Category Encoding
        if category != "Education":
            data[f"category_{category}"] = 1

        # Device Encoding
        if device != "Desktop":
            data[f"device_{device}"] = 1

        # Country Encoding
        if country != "AU":
            data[f"country_{country}"] = 1

        # Month Encoding
        if month != "April":
            data[f"month_{month}"] = 1

        input_df = pd.DataFrame([data])

        # Scale Input
        scaled_input = scaler.transform(input_df)

        # Prediction
        prediction = model.predict(scaled_input)

        st.success(
            f"💰 Predicted Ad Revenue: ${prediction[0]:,.2f}"
        )

        st.subheader("Input Summary")
        st.dataframe(input_df)

# ==========================
# VISUALIZATIONS PAGE
# ==========================

elif selection == "Visualizations":

    st.title("📊 Model Insights & Visualizations")

    # =====================================
    # Feature Importance
    # =====================================

    st.subheader("Top Features Influencing Ad Revenue")

    features = [
        'Watch Time Minutes',
        'Likes',
        'Comments',
        'Views',
        'Year'
    ]

    importance = [
        59.63,
        8.65,
        2.11,
        0.64,
        0.21
    ]

    fig1, ax1 = plt.subplots(figsize=(8, 5))

    ax1.bar(features, importance)

    ax1.set_title("Feature Importance")

    ax1.set_ylabel("Coefficient Value")

    plt.xticks(rotation=20)

    st.pyplot(fig1)

    # =====================================
    # Model Comparison
    # =====================================

    st.subheader("Regression Model Performance")

    models = [
        "Linear Regression",
        "Gradient Boosting",
        "Random Forest",
        "Decision Tree",
        "KNN"
    ]

    r2_scores = [
        0.9519,
        0.9517,
        0.9510,
        0.8921,
        0.6622
    ]

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    ax2.bar(models, r2_scores)

    ax2.set_title("Model Comparison (R² Score)")

    ax2.set_ylabel("R² Score")

    plt.xticks(rotation=20)

    st.pyplot(fig2)

    # =====================================
    # Revenue Driver Analysis
    # =====================================

    st.subheader("Revenue Driver Analysis")

    driver_data = pd.DataFrame({
        "Feature": [
            "Watch Time",
            "Likes",
            "Comments",
            "Views"
        ],
        "Impact": [
            59.63,
            8.65,
            2.11,
            0.64
        ]
    })

    st.bar_chart(
        driver_data.set_index("Feature")
    )

    # =====================================
    # Sample Revenue Growth Trend
    # =====================================

    st.subheader("Revenue Growth Trend")

    trend_df = pd.DataFrame({
        "Views": [
            1000,
            5000,
            10000,
            50000,
            100000
        ],
        "Revenue": [
            15,
            60,
            120,
            600,
            1200
        ]
    })

    st.line_chart(
        trend_df.set_index("Views")
    )

    # =====================================
    # Metrics Dashboard
    # =====================================

    st.subheader("Best Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "R² Score",
            "0.9519"
        )

    with col2:
        st.metric(
            "MAE",
            "3.17"
        )

    with col3:
        st.metric(
            "RMSE",
            "13.60"
        )

    st.success(
        "Linear Regression was selected as the final model because it achieved the highest R² Score and lowest prediction errors."
    )

    # =====================================
    # Key Business Insights
    # =====================================

    st.subheader("📌 Key Insights")

    st.info("""
    • Watch Time Minutes is the strongest predictor of ad revenue.

    • Likes and Comments significantly improve monetization.

    • Videos with higher engagement tend to generate more revenue.

    • Linear Regression achieved the best overall performance with an R² Score of 95.19%.

    • Audience engagement is more influential than views alone.
    """)