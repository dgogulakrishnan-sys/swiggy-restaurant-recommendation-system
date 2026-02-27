 Swiggy Restaurant Recommendation System

A Machine Learning-powered restaurant recommendation system built using Streamlit.

This project recommends restaurants based on:
- City
- Cuisine
- Preferred Rating
- Budget

The application provides fast and personalized recommendations using similarity-based filtering.

Features

-  Sidebar-based smart filtering
-  Fast recommendation engine
-  Clean card-style UI
-  Professional dashboard layout
-  Cached performance optimization
-  Cosine similarity-based recommendation logic

Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Cosine Similarity 

Project Structure

SWIGGY_RESTAURANT_RECOMMENDATION_SYSTEM/
│
├── app.py 
├── recommend.py 
├── DATA/
│ ├── cleaned_data.csv
│ └── encoded_data.csv
├── requirements.txt
├── README.md
└── .gitignore

Installation & Setup

1. Clone the Repository

```bash
git clone https://github.com/yourusername/swiggy-restaurant-recommendation-system.git
cd swiggy-restaurant-recommendation-system
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
streamlit run app.py

** How It Works

Data is cleaned and preprocessed.

Categorical features are encoded.

Similarity matrix is computed using cosine similarity.

Restaurants are filtered based on user preferences.

Top matching results are displayed in card format.
