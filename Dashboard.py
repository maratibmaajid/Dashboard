# Dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CivicDesk Live Dashboard",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DATA (from your prompt) ---
DATA = {
    "traffic": {
        "loss_crore": 60000,
        "avg_speed_bengaluru": 18,
        "unmarked_roads_percent": 40,
    },
    "waste": {
        "total_generated_tonnes": 160000,
        "processed_percent": 30,
        "delhi_waste_tonnes": 11000,
        "plastic_increase_factor": 3,
    },
    "water": {
        "cities_at_risk": 21,
        "contaminated_percent": 70,
        "leaking_tap_waste_liters": 1000,
    },
    "pollution": {
        "annual_deaths": 1670000,
        "delhi_aqi_severe": 400,
        "oxygen_loss_per_tree_kg": 118,
    },
    "grievances": {
        "pothole_deaths_comparison": "more than terror attacks",
        "avg_resolution_days_min": 7,
        "avg_resolution_days_max": 30,
    }
}


# --- STYLING ---
# Inject custom CSS for a more polished look
st.markdown("""
<style>
    /* Main blocks */
    .stMetric {
        background-color: #2a2a39;
        border-radius: 10px;
        padding: 15px;
        color: white;
    }
    /* Metric labels */
    .stMetric > div > div:nth-child(1) {
        font-size: 1.2rem;
        color: #a0a0b0;
    }
    /* Metric values */
    .stMetric > div > div:nth-child(2) {
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
    }
    /* Fact card styling */
    .fact-card {
        background-color: #1c1c2e;
        border-left: 5px solid #6c63ff;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 10px;
        color: #f0f2f6;
        height: 100%;
    }
    .fact-card-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .fact-card-text {
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# --- HEADER ---
st.title("🏙️ CivicDesk: Real-Time Urban Insights")
st.markdown("An overview of key civic challenges across major Indian cities, based on recent studies and data.")


# --- LIVE STATS SECTION ---
st.markdown("### 🔴 Live Counters (Simulated)")
live_stats_placeholder = st.empty()

# Simulate live updates for key metrics
for i in range(1000): # Loop to keep updating
    with live_stats_placeholder.container():
        col1, col2, col3 = st.columns(3)
        # Calculate simulated live values
        live_waste = DATA['waste']['total_generated_tonnes'] + i * 15
        live_complaints = 52345 + i * 3
        live_water_loss = 234567890 + i * 1234

        col1.metric(
            label="Daily Solid Waste Generated (Tonnes)",
            value=f"{live_waste:,}"
        )
        col2.metric(
            label="Active Civic Grievances",
            value=f"{live_complaints:,}"
        )
        col3.metric(
            label="Water Wasted from Leaks (Litres)",
            value=f"{live_water_loss:,}"
        )
    time.sleep(2)


# --- SECTIONS ---
st.markdown("---") # Visual separator

# --- WASTE MANAGEMENT SECTION ---
st.header("🗑️ Waste Management Crisis")
col1, col2 = st.columns([1.5, 1])

with col1:
    # Create a comparison chart for waste generation vs. processing
    waste_df = pd.DataFrame({
        "Status": ["Waste Generated", "Waste Processed"],
        "Amount (Tonnes per day)": [
            DATA['waste']['total_generated_tonnes'],
            DATA['waste']['total_generated_tonnes'] * (DATA['waste']['processed_percent'] / 100)
        ]
    })
    fig = px.bar(
        waste_df,
        x="Status",
        y="Amount (Tonnes per day)",
        color="Status",
        color_discrete_map={"Waste Generated": "#6c63ff", "Waste Processed": "#ff6347"},
        title="India's Daily Solid Waste: Generated vs. Processed",
        text_auto=True
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown(
        f"""
        <div class="fact-card">
            <div class="fact-card-title">Only {DATA['waste']['processed_percent']}% Processed</div>
            <div class="fact-card-text">
                Out of <b>{DATA['waste']['total_generated_tonnes']:,} tonnes</b> of solid waste generated daily,
                a staggering 70% remains unprocessed, contributing to landfill overflow and pollution.
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="fact-card">
            <div class="fact-card-title">Plastic Waste Tripled</div>
            <div class="fact-card-text">
                The consumption and improper disposal of plastic have led to a <b>3x increase</b> in plastic waste
                over the last 5 years, choking water bodies and harming ecosystems.
            </div>
        </div>
        """, unsafe_allow_html=True
    )


# --- OTHER SECTIONS USING FACT CARDS ---
st.markdown("---")

# Traffic & Roads
st.header("🚦 Traffic & Roads")
col1, col2, col3 = st.columns(3)
with col1:
    st.warning(f"**₹{DATA['traffic']['loss_crore']:,} Crore** lost annually due to traffic congestion.")
with col2:
    st.info(f"Average traffic speed in Bengaluru is just **{DATA['traffic']['avg_speed_bengaluru']} km/h** during peak hours.")
with col3:
    st.error(f"**{DATA['traffic']['unmarked_roads_percent']}%** of Indian roads lack proper markings or signs.")

st.markdown("---")

# Water Supply
st.header("💧 Water Supply")
col1, col2, col3 = st.columns(3)
with col1:
    st.error(f"**{DATA['water']['cities_at_risk']} major cities** like Delhi & Bengaluru may soon run out of groundwater.")
with col2:
    st.warning(f"**{DATA['water']['contaminated_percent']}%** of India's water is contaminated and unsafe for direct consumption.")
with col3:
    st.info(f"A single leaking tap can waste nearly **{DATA['water']['leaking_tap_waste_liters']:,} liters** of water per month.")

st.markdown("---")

# Pollution & Environment
st.header("🌳 Pollution & Environment")
col1, col2, col3 = st.columns(3)
with col1:
    st.error(f"Air pollution causes **{DATA['pollution']['annual_deaths']:,} deaths** in India annually.")
with col2:
    st.warning(f"Delhi’s Air Quality Index (AQI) often crosses **{DATA['pollution']['delhi_aqi_severe']}+**, falling in the 'Severe' category.")
with col3:
    st.info(f"Cutting down one tree removes **{DATA['pollution']['oxygen_loss_per_tree_kg']} kg** of oxygen per year from the atmosphere.")


st.markdown("---")
st.sidebar.info("Dashboard by CivicDesk Analytics. Data sourced from NITI Aayog, Lancet, and NCRB reports.")