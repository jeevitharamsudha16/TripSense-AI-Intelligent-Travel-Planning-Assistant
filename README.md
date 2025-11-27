# ✈️ AI Travel Planner
![App Screenshot](https://github.com/jeevitharamsudha16/TripSense-AI-Intelligent-Travel-Planning-Assistant/blob/main/Snip20251127_1.png)

**1. Introduction**

The AI Travel Planner is an intelligent multi-agent system designed to automate travel planning using CrewAI, Google Gemini 2.5 Flash, Serper Search API, and Streamlit.
It generates:
- A detailed travel research summary
- A personalized itinerary
- A clear budget breakdown
- A visual gallery of destination images
- The system eliminates manual travel research and helps users plan complete trips with AI.

**2. Project Objectives**
**The main objectives of this project are:**
- To automate destination research using web search tools
- To generate structured day-wise itineraries
- To compute budget distribution for travelers
- To provide destination images to enhance trip visualization
- To build an interactive and easy-to-use travel assistant

**3. Technologies Used**
| Component                  | Technology                    |
| -------------------------- | ----------------------------- |
| **Frontend/UI**            | Streamlit                     |
| **AI Model**               | Google Gemini 2.5 Flash       |
| **Multi-Agent Framework**  | CrewAI                        |
| **Search API**             | SerperDevTool (Serper API)    |
| **Image Retrieval**        | SerpAPI - Google Image Search |
| **Budget & Data Handling** | Pandas                        |
| **Environment Management** | python-dotenv                 |
| **HTTP Requests**          | Requests                      |

**4. System Architecture**

**User Inputs Trip Details →**
↳ CrewAI Agents Activated →
     1. **Travel Research Expert**
     2. **Itinerary Planner**

- Serper Tool fetches real-time travel information 
- Gemini LLM processes research & creates itinerary 
- Budget breakdown calculated with Pandas 
- SerpAPI fetches image results 
  
**Streamlit UI displays:**
- Research
- Day-wise itinerary
- Budget
- Destination images

**5. Multi-Agent Design**
**🤖 Agent 1 — Travel Researcher**

- Role: Collect destination-related insights
- Uses Serper search tool for live web research
- Outputs structured travel brief including:
- Flight ranges
- Weather
- Best areas to stay
- Local transport
- Cultural and safety tips
- Activities based on user style

**🤖Agent 2 — Itinerary Planner**

- Role: Create an optimized multi-day travel plan
- Uses Gemini + research data
**Generates:**
- Day-by-day itinerary
- Food suggestions
- Photo spots
- Budget categories
- Activity recommendations

**6. Key Features**
**✔ Automated Travel Research**

**AI retrieves destination info such as:**

- Weather
- Places of interest
- Local culture
- Safety guidelines
- Best neighborhoods to stay

**✔ Personalized Itinerary Builder**

**Produces a day-wise plan based on:**

- Trip duration
- Travel style
- Budget
- Visitor count

**✔ Smart Budget Breakdown**

**Calculates estimates for:**
- Flights
- Stay
- Food & drinks
- Transport
- Activities
- Miscellaneous

**✔ Destination Image Gallery**
- Using SerpAPI + Google Images:
- Fetches real images of the location
- Displays them in a responsive grid layout

**✔ Clean Streamlit UI**

**Three-tab interface:**

- 🔍 Research
- 📝 Itinerary
- 📸 Destination Images

**7. Workflow Description**
**Step 1 — User Input**

**User fills:**
- Origin
- Destination
- Month
- Budget
- Trip duration
- Travel style

**Step 2 — Multi-Agent Execution**

CrewAI executes both tasks sequentially.

**Step 3 — Data Aggregation**

**The app compiles:**

- Gemini research output
- Gemini itinerary
- Pandas budget breakdown
- SerpAPI images

**Step 4 — Display in UI**

Streamlit shows all sections neatly.

**8. Sample Output (Summarized)**
**🔍 Research Summary Example**
- Singapore offers modern attractions, cultural zones, and well-connected transport.
- Ideal to visit in January with pleasant temperatures.
- Best areas to stay include Marina Bay, Orchard Road, and Little India.

**📝 Itinerary Example**
- Day 1: Marina Bay Sands, Merlion Park, River Cruise  
- Day 2: Sentosa Island + SkyHelix + Adventure Cove  
- Day 3: Gardens By The Bay + Cloud Forest  

**💰 Budget Breakdown Example**
- Flights: 40%  
- Stay: 30%  
- Food: 15%  
- Transport: 5%  
- Activities: 7%  
- Misc: 3%  
**📸 Images Example**

- Skyline
- Gardens By The Bay
- Sentosa

**9. Limitations**

- SerpAPI requires a valid API key
- Serper research depends on search quality
- Itinerary accuracy varies based on online data
- Flights/hotel data not included (removed intentionally)
- App requires stable internet connection

**10. Future Enhancements**
- Add hotel, flight, and attraction comparison
- Enable multi-country itineraries
- Add PDF export for full trip plan
- Add cost-optimization AI agent
- Add map route planner
- Add offline caching of research outputs
- Add sentiment-based travel style recommendation

**11. Conclusion**

The AI Travel Planner successfully demonstrates the power of multi-agent systems, real-time search tools, and large language models working together to automate travel planning.

**It delivers:**
- Accurate travel research
- Personalized itineraries
- Intelligent budgeting
- Beautiful image galleries

This system can be expanded into a full-featured AI Travel Assistant App for travel agencies, tourism startups, and individual travelers.
