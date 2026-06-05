# ✈️ TripGenie — AI Travel Planner

TripGenie is an AI-powered travel planning web app built with [Streamlit](https://streamlit.io/) and [Google Gemini](https://ai.google.dev/). Enter your trip details and get a fully personalized itinerary — complete with a day-by-day schedule, budget breakdown, food recommendations, and travel tips — in seconds.

---

## 🚀 Features

- 📍 Origin-to-destination trip planning
- 🗓️ Day-by-day itinerary generation
- 💰 Budget allocation breakdown
- 🍜 Food & restaurant recommendations
- 🧳 Tailored to travel type, transport, accommodation & interests
- ⚡ Powered by Gemini 2.5 Flash

---

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.9+
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tripgenie.git
cd tripgenie
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the app

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`.

---

## 📁 Project Structure

```
tripgenie/
├── main.py              # Streamlit UI entry point
├── requirements.txt     # Python dependencies
├── .env                 # API key (not committed)
├── .gitignore
└── app/
    ├── config.py        # Loads environment variables
    ├── planner.py       # Gemini API integration
    └── prompts.py       # Prompt template for the AI
```

---

## 💡 Solution Approach

1. **User Input** — The Streamlit UI collects trip parameters: origin, destination, duration, number of travelers, travel type, budget (₹), transport preference, accommodation preference, and interests.

2. **Prompt Engineering** — Inputs are injected into a structured prompt template (`prompts.py`) that instructs Gemini to generate five specific sections: trip summary, budget allocation, day-by-day itinerary, food recommendations, and travel tips.

3. **AI Generation** — The filled prompt is sent to `gemini-2.5-flash` via the `google-generativeai` SDK. The raw markdown response is returned directly to the UI.

4. **Display** — Streamlit renders the markdown response inline, giving users a clean, readable itinerary.

---

## 🔑 Dependencies

Key packages (see `requirements.txt` for full list):

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `google-generativeai` | Gemini API client |
| `python-dotenv` | Load `.env` variables |
| `pandas` / `numpy` | Data utilities |
| `pillow` | Image handling |

---

## 📝 Usage Example

1. Enter **From Location**: `Pune, India`
2. Enter **Destination**: `Tokyo, Japan`
3. Set **Duration**: `7 days`, **Travelers**: `2`, **Budget**: `₹2,00,000`
4. Choose **Travel Type**: `Couple`, **Transport**: `Flights`, **Accommodation**: `Mid-Range`
5. Select **Interests**: `Food`, `Culture`, `Anime`
6. Click **Generate Trip** — your itinerary appears instantly!

---

## ⚠️ Notes

- Keep your `.env` file private — it is excluded from version control via `.gitignore`.
- Gemini API usage may be subject to rate limits on free-tier keys.
- The budget input is denominated in Indian Rupees (₹).
