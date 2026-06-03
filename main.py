import streamlit as st
from app.planner import generate_trip

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

    if not from_location or not destination:
        st.warning("Please enter both From Location and Destination.")
        st.stop()

    if not interests:
        st.warning("Please select at least one interest.")
        st.stop()

    with st.spinner("Planning your trip..."):

        result = generate_trip(
            from_location=from_location,
            destination=destination,
            duration=duration,
            travelers=travelers,
            travel_type=travel_type,
            budget=budget,
            transport=transport,
            accommodation=accommodation,
            interests=interests
        )

    st.success("Trip Plan Generated")

    st.markdown("## Your AI Generated Itinerary")

    st.markdown(result)