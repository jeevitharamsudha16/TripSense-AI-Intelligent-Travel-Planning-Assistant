
import os
import streamlit as st
from dotenv import load_dotenv
import pandas as pd
import requests

# ==========================
# Load Environment
# ==========================
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")

if SERPER_API_KEY is None:
    raise ValueError("❌ SERPER_API_KEY missing in .env")
if GOOGLE_API_KEY is None:
    raise ValueError("❌ GOOGLE_API_KEY missing in .env")
if SERP_API_KEY is None:
    raise ValueError("❌ SERP_API_KEY missing in .env")

# ==========================
# CrewAI + Tools
# ==========================
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

# Gemini (CrewAI native)
llm = LLM(
    model="google/gemini-2.5-flash",
    api_key=GOOGLE_API_KEY,
    temperature=0.5,
)

# ==========================
# Agents
# ==========================
travel_researcher = Agent(
    role="Travel Research Expert",
    goal="Research detailed travel info for {destination}",
    verbose=True,
    memory=True,
    backstory="Expert global travel researcher.",
    tools=[search_tool],
    llm=llm,
)

itinerary_planner = Agent(
    role="Itinerary Planner",
    goal="Prepare a full {days}-day itinerary for {destination}",
    verbose=True,
    memory=True,
    backstory="Creates balanced itineraries for all budgets.",
    tools=[search_tool],
    llm=llm,
)

# ==========================
# Tasks
# ==========================
travel_research_task = Task(
    description=(
        "Research {destination}. Include:\n"
        "- Flight ranges from {origin}\n"
        "- Best areas to stay\n"
        "- Local transport options\n"
        "- Attractions matching style {style}\n"
        "- Weather in {month}\n"
        "- Safety/cultural tips"
    ),
    expected_output="Structured markdown research brief.",
    tools=[search_tool],
    agent=travel_researcher,
)

itinerary_task = Task(
    description=(
        "Create {days}-day itinerary for {destination}.\n"
        "- Day-wise plan\n"
        "- Food suggestions\n"
        "- Budget breakdown\n"
        "- Photo spot recommendations"
    ),
    expected_output="Full markdown itinerary.",
    tools=[search_tool],
    agent=itinerary_planner,
)

# ==========================
# Crew
# ==========================
crew = Crew(
    agents=[travel_researcher, itinerary_planner],
    tasks=[travel_research_task, itinerary_task],
    process=Process.sequential,
)

# ==========================
# Budget Calculator
# ==========================
def compute_budget_breakdown(total_budget, days, travellers):
    split = {
        "Flights": 0.40,
        "Stay": 0.30,
        "Food & Drinks": 0.15,
        "Local Transport": 0.05,
        "Activities": 0.07,
        "Misc": 0.03,
    }
    rows = []
    for cat, pct in split.items():
        amount = total_budget * pct
        rows.append({
            "Category": cat,
            "Total (₹)": round(amount),
            "Per Person (₹)": round(amount / travellers),
        })
    return pd.DataFrame(rows)

# ==========================
# Google Images via SerpAPI
# ==========================
def get_google_images(query: str):
    url = f"https://serpapi.com/search?engine=google_images&q={query}&api_key={SERP_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if "images_results" in data:
            return [img['original'] for img in data['images_results']]
    except Exception as e:
        return [f"Error fetching images: {str(e)}"]
    return []

# ==========================
# Streamlit UI
# ==========================
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

st.title("✈️ AI Travel Planner (CrewAI + Gemini + Serper)")
st.write("Plan perfect trips with AI-powered research, itinerary and destination images!")

# -------- Form --------
with st.form("plan_form"):
    col1, col2 = st.columns(2)

    with col1:
        origin = st.text_input("Departure City", "Bengaluru")
        destination = st.text_input("Destination", "Singapore")
        month = st.selectbox("Travel Month",
                             ["January","February","March","April","May","June",
                              "July","August","September","October","November","December"])
    with col2:
        days = st.slider("Trip Duration (days)", 2, 14, 5)
        travellers = st.number_input("Travellers", 1, 10, 2)
        budget = st.number_input("Total Budget (₹)", 10000, 500000, 80000)

    style = st.selectbox(
        "Travel Style",
        ["Balanced", "Relaxed", "Adventure", "Food", "Nightlife", "Culture"],
    )

    submit = st.form_submit_button("✨ Generate Plan")

# -------- Process Request --------
if submit:
    with st.spinner("💡 Researching & Planning your trip..."):
        result = crew.kickoff({
            "origin": origin,
            "destination": destination,
            "days": days,
            "travellers": travellers,
            "budget": budget,
            "month": month,
            "style": style,
        })

    st.success("🎉 Trip Planned Successfully!")

    # Extract
    research = result.tasks_output[0].raw
    itinerary = result.tasks_output[1].raw

    # Tabs
    tab1, tab2, tab3 = st.tabs(["🔍 Research", "📝 Itinerary", "📸 Destination Images"])

    # ====== TAB 1 Research ======
    with tab1:
        st.markdown(research)

    # ====== TAB 2 Itinerary ======
    with tab2:
        st.markdown(itinerary)
        df = compute_budget_breakdown(budget, days, travellers)
        st.subheader("💰 Approx Budget Breakdown")
        st.dataframe(df, hide_index=True)

    # ====== TAB 3 Destination IMAGES ======
    with tab3:
        st.subheader(f"📸 Images for {destination}")

        image_urls = get_google_images(destination)
        cols = st.columns(3)

        for i, url in enumerate(image_urls):
            cols[i % 3].image(url, caption=f"Image {i + 1} from Google")
