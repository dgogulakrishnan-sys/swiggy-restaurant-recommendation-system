import streamlit as st
import pandas as pd
from recommend import recommend_restaurants

# -------------------------------
# PAGE CONFIG (MUST BE FIRST)
# -------------------------------
st.set_page_config(
    page_title="Swiggy Recommendation System",
    layout="wide"
)

# -------------------------------
# LOAD DATA (CACHED FOR SPEED)
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv(
        r"D:\PROJECTS\SWIGGY_RESTAURANT_RECOMMENDATION_SYSTEM\DATA\cleaned_data.csv"
    )

df = load_data()

# -------------------------------
# CACHE RECOMMENDATION FUNCTION
# -------------------------------
@st.cache_data
def get_recommendations(city, cuisine, rating, cost):
    return recommend_restaurants(city, cuisine, rating, cost)

# -------------------------------
# BACKGROUND STYLE
# -------------------------------
page_bg = """
<style>
.stApp {
    background: 
        linear-gradient(rgba(255,255,255,0.7), rgba(255,255,255,0.7)),
        url("https://images.unsplash.com/photo-1498654896293-37aacf113fd9");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown("""
<h1 style='
    text-align: center;
    font-size: 60px;
    font-family: Arial Black;
    color: #FC8019;
'>
Swiggy Restaurant Recommendation System
</h1>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("Filter Restaurants")

with st.sidebar.form("filter_form"):

    city = st.selectbox(
        "Select City",
        sorted(df["city"].unique())
    )

    cuisine = st.selectbox(
        "Select Cuisine",
        sorted(df["cuisine"].unique())
    )

    rating = st.slider(
        "Preferred Rating",
        1.0, 5.0, 4.0
    )

    cost = st.number_input(
        "Preferred Cost (₹)",
        min_value=50,
        max_value=2000,
        value=300
    )

    recommend_btn = st.form_submit_button("Recommend Restaurants")

# -------------------------------
# SHOW RECOMMENDATIONS
# -------------------------------
if recommend_btn:

    with st.spinner("Finding best restaurants for you... 🍴"):
        results = get_recommendations(city, cuisine, rating, cost)

    st.markdown("Top Recommendations")

    if results.empty:
        st.warning("No restaurants found matching your criteria.")
    else:

        cols = st.columns(3)

        for i, (_, row) in enumerate(results.iterrows()):
            col = cols[i % 3]

            with col:
                st.markdown(f"""
                <div class="card">
                    <h3 style="color:#FC8019;">{row['name']}</h3>
                    <p><b>City:</b> {row['city']}</p>
                    <p><b>Cuisine:</b> {row['cuisine']}</p>
                    <p><b>Rating:</b> {row['rating']:.1f} / 5</p>
                    <p><b>Ratings Count:</b> {int(row['rating_count'])}</p>
                    <p><b>Average Cost:</b> ₹{int(row['cost'])}</p>
                </div>
                """, unsafe_allow_html=True)