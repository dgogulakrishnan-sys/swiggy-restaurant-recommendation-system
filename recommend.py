import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load encoded data
cleaned_df = pd.read_csv(r"D:\PROJECTS\SWIGGY_RESTAURANT_RECOMMENDATION_SYSTEM\DATA\cleaned_data.csv")
encoded_df = pd.read_csv(r"D:\PROJECTS\SWIGGY_RESTAURANT_RECOMMENDATION_SYSTEM\DATA\encoded_data.csv")
scaled_df = pd.read_csv(r"D:\PROJECTS\SWIGGY_RESTAURANT_RECOMMENDATION_SYSTEM\DATA\scaled_data.csv")

with open(r"D:\PROJECTS\SWIGGY_RESTAURANT_RECOMMENDATION_SYSTEM\DATA\encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

with open(r"D:\PROJECTS\SWIGGY_RESTAURANT_RECOMMENDATION_SYSTEM\DATA\scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


def recommend_restaurants(city, cuisine, rating, cost, top_n=5):

    # Create user input dataframe
    user_df = pd.DataFrame({
        "city":[city],
        "cuisine":[cuisine],
        "rating":[rating],
        "rating_count":[0],
        "cost":[cost]
    })

    # Encode categorical
    user_encoded = encoder.transform(user_df[["city","cuisine"]])

    user_encoded_df = pd.DataFrame(
        user_encoded,
        columns=encoder.get_feature_names_out(["city","cuisine"])
    )

    # Combine
    user_full = pd.concat(
        [user_df[["rating","rating_count","cost"]].reset_index(drop=True),
         user_encoded_df],
        axis=1
    )

    # Scale
    user_scaled = scaler.transform(user_full)

    # Compute similarity (1 x 141k only)
    similarity_scores = cosine_similarity(user_scaled, scaled_df)

    # Get top N indices
    top_indices = similarity_scores[0].argsort()[-top_n:][::-1]

    return cleaned_df.iloc[top_indices]