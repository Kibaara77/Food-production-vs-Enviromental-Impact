import streamlit as st
import pandas as pd
import numpy as np
import joblib


model=joblib.load('EnvImpact.joblib')

st.title('Enviromental Impact Predictor for Food Production')


FOOD_DATA_STRING = """
Food_Product,Cluster,Environmental_Profile
Beef (beef herd),2,"Extreme High Impact/ Ho Land Use and Emission"
Beef (dairy herd),3,"Water & Eutrophication Intensive"
Lamb & Mutton,7,"Intensive Animal Feed & Processing"
Pig Meat,4,"Average but slight ho transport and retail"
Poultry Meat,4,"Average but slight ho transport and retail"
Milk,4,"Average but slight ho transport and retail"
Cheese,3,"Water & Eutrophication Intensive"
Eggs,1,"Overall Low Impact/Green"
Fish (farmed),3,"Water & Eutrophication Intensive"
Shrimps (farmed),4,"Average but slight ho transport and retail"
"""


# --- 2. LOAD DATA AND MODEL ---
try:
    # 2a. Load the trained K-Means or Clustering Model (if needed for prediction)
    # Since your table already has the cluster, we'll focus on loading the food data.
    # If your model is used to predict the cluster from input features, uncomment and rename below.
    # model = joblib.load(MODEL_FILE_NAME)
    
    # 2b. Load the reference food data into a Pandas DataFrame
    data = pd.read_csv(pd.io.common.StringIO(FOOD_DATA_STRING))
    food_list = data['Food_Product'].unique().tolist()
    
except FileNotFoundError:
    st.error(f"Error: Model file '{EnvImpact.joblib}' not found. Please check the file path.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred during setup: {e}")
    st.stop()

# --- 3. STREAMLIT APP LAYOUT ---
st.set_page_config(page_title="Food Impact Profiler", layout="centered")

#st.title("🌱 Food Environmental Impact Profiler")
st.markdown("Select a food product to view its pre-computed clustering and environmental profile.")

# --- 4. USER INPUT ---
# Create a dropdown menu for the user to select a food product
selected_food = st.selectbox(
    "Choose a Food Product:",
    options=food_list
)

# --- 5. DISPLAY RESULTS ---
if selected_food:
    # Look up the profile for the selected food
    profile_data = data[data['Food_Product'] == selected_food].iloc[0]
    
    cluster = profile_data['Cluster']
    environmental_profile = profile_data['Environmental_Profile']
    
    st.subheader(f"Results for: **{selected_food}**")
    
    # Display the cluster information with visual cues
    if cluster in [1, 4]:
        st.success(f"**Cluster ID:** {cluster}")
    elif cluster in [3, 7]:
        st.warning(f"**Cluster ID:** {cluster}")
    elif cluster == 2:
        st.error(f"**Cluster ID:** {cluster}")
    else:
        st.info(f"**Cluster ID:** {cluster}")
        
    st.markdown(f"**Environmental Profile:** {environmental_profile}")

    # Display an explanatory box
    if cluster == 2:
        st.markdown(
            "> **Interpretation:** This cluster (Extreme High Impact) typically represents food items with the highest overall footprint, dominated by land use and GHG emissions."
        )
    elif cluster == 1:
        st.markdown(
            "> **Interpretation:** This cluster (Overall Low Impact) represents food items with minimal environmental burdens across all metrics."
        )

st.sidebar.header("About")
st.sidebar.info("This application demonstrates the classification of food products into environmental impact clusters using pre-calculated data.")
  


