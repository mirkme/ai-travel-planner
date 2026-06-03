import streamlit as st

st.set_page_config(
    page_title="TripGenie",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ TripGenie")
st.subheader("AI Travel Planner")

st.divider()

st.markdown("### Trip Information")

col1, col2 = st.columns(2)

with col1:

    from_location = st.text_input(
        "From Location",
        placeholder="Goa, India"
    )

    destination = st.text_input(
        "Destination",
        placeholder="Japan"
    )

    duration = st.number_input(
        "Trip Duration (Days)",
        min_value=1,
        max_value=60,
        value=7
    )

with col2:

    travelers = st.number_input(
        "Number of Travelers",
        min_value=1,
        max_value=20,
        value=1
    )

    budget = st.number_input(
        "Budget (₹)",
        min_value=1000,
        value=50000
    )

    travel_type = st.selectbox(
        "Travel Type",
        [
            "Solo",
            "Couple",
            "Family",
            "Friends",
            "Business"
        ]
    )

transport = st.selectbox(
    "Transport Preference",
    [
        "Flights",
        "Train",
        "Bus",
        "Car Rental",
        "No Preference"
    ]
)

accommodation = st.selectbox(
    "Accommodation Preference",
    [
        "Budget",
        "Mid-Range",
        "Luxury"
    ]
)

interests = st.multiselect(
    "Interests",
    [
        "Food",
        "Culture",
        "Adventure",
        "Nature",
        "Shopping",
        "Nightlife",
        "Anime",
        "Photography"
    ]
)

if st.button("Generate Trip"):

    st.success("Trip Details Generated")

    st.markdown("## Trip Summary")

    st.write(f"From: {from_location}")
    st.write(f"To: {destination}")
    st.write(f"Duration: {duration} Days")
    st.write(f"Travelers: {travelers}")
    st.write(f"Travel Type: {travel_type}")
    st.write(f"Budget: ₹{budget:,}")
    st.write(f"Transport: {transport}")
    st.write(f"Accommodation: {accommodation}")
    st.write(f"Interests: {', '.join(interests)}")