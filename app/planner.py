import google.generativeai as genai

from app.config import GEMINI_API_KEY
from app.prompts import TRAVEL_PROMPT

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_trip(
    from_location,
    destination,
    duration,
    travelers,
    travel_type,
    budget,
    transport,
    accommodation,
    interests
):

    prompt = TRAVEL_PROMPT.format(
        from_location=from_location,
        destination=destination,
        duration=duration,
        travelers=travelers,
        travel_type=travel_type,
        budget=budget,
        transport=transport,
        accommodation=accommodation,
        interests=", ".join(interests)
    )

    response = model.generate_content(prompt)

    return response.text