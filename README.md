# 🌍 AI-Powered Trip Planner

An intelligent multi-agent travel planning system powered by CrewAI that generates personalized travel itineraries using AI agents working collaboratively.

## 🔗 Quick Links

- **🌐 Live Demo**: [https://multi-agent-travel-planner-crew.streamlit.app/](https://multi-agent-travel-planner-crew.streamlit.app/)
- **📚 GitHub Repository**: [https://github.com/wsmaisys/multi-agent-travel-planner](https://github.com/wsmaisys/multi-agent-travel-planner)

## 📋 Features

- **🏢 Location Expert Agent** - Gathers comprehensive travel information including accommodations, cost of living, visa requirements, transportation, weather forecasts, and local events
- **🎭 Local Guide Expert Agent** - Provides personalized recommendations for attractions, food, entertainment, and activities tailored to user interests
- **✈️ Travel Planner Expert Agent** - Compiles all information into a well-structured, day-by-day travel itinerary
- **📥 Multiple Download Formats** - Download travel plans as Text, Markdown, or CSV
- **🎨 Beautiful UI** - Streamlit-based interface with hierarchical display of agent responses
- **⏳ Real-time Progress** - See step-by-step progress as AI agents work on your trip plan

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Mistral API Key (get it from [console.mistral.ai](https://console.mistral.ai))

### Installation

1. **Clone or navigate to the project directory**

```bash
cd "Trip_Planner_MultiAgent"
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_api_key_here
```

4. **Run the application**

```bash
streamlit run app.py
```

5. **Open in browser**
   Navigate to `http://localhost:8501` to access the application.

## 📁 Project Structure

```
Trip_Planner_MultiAgent/
├── app.py                 # Main Streamlit application
├── Travelagents.py       # CrewAI agents configuration
├── TravelTasks.py        # Task definitions for agents
├── TravelTools.py        # Custom tools for agents
├── .env                  # Environment variables (create this)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Configuration

### Agent Configuration (`Travelagents.py`)

- **guide_expert** - City Local Guide Expert
- **location_expert** - Travel Trip Expert
- **planner_expert** - Travel Planning Expert

### Task Configuration (`TravelTasks.py`)

- `location_task()` - Gather location information
- `guide_task()` - Create local guide recommendations
- `planner_task()` - Compile final itinerary

### Tools (`TravelTools.py`)

- `search_web_tool()` - DuckDuckGo web search integration

## 💻 How to Use

1. **Enter Trip Details**

   - From City: Your starting point
   - Destination City: Where you want to go
   - Departure & Return Dates: Trip duration
   - Interests: Activities you enjoy (e.g., "sightseeing and good food")

2. **Generate Plan**

   - Click "🚀 Generate Travel Plan" button
   - Watch as AI agents work through their tasks
   - See progress updates in real-time

3. **View Results**

   - Location Information - Travel logistics and essentials
   - Local Guide - Attractions and recommendations
   - Full Itinerary - Complete day-by-day plan

4. **Download**
   - Choose preferred format: Text, Markdown, or CSV
   - Share or print your personalized travel plan

## 🛠️ Technologies Used

- **CrewAI** - Multi-agent orchestration framework
- **Streamlit** - Web UI framework
- **Mistral AI** - Language model for agent intelligence
- **LangChain** - LLM integration and tools
- **DuckDuckGo Search** - Web search functionality
- **python-dotenv** - Environment variable management

## 📦 Dependencies

See `requirements.txt` for complete list of dependencies.

Key packages:

- crewai
- streamlit
- mistralai
- langchain
- langchain_community
- python-dotenv
- duckduckgo-search

## 🔐 API Keys

This project requires a **Mistral API Key**:

1. Go to [console.mistral.ai](https://console.mistral.ai)
2. Create an account or sign in
3. Generate a new API key
4. Add it to your `.env` file

## 📝 Example Usage

```
From City: New Delhi
Destination City: Rome
Departure Date: 2025-03-01
Return Date: 2025-03-07
Interests: Sightseeing and good food
```

The system will generate:

- Accommodation recommendations and cost breakdown
- Visa requirements and travel logistics
- Top attractions and local recommendations
- Complete 7-day itinerary with time allocations
- Budget estimates and local tips

## 🐛 Troubleshooting

### "Mistral API Key is invalid"

- Verify your API key is correct in `.env`
- Ensure the key has proper permissions

### "ImportError: Fallback to LiteLLM is not available"

- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Ensure `litellm` is installed: `pip install litellm`

### Port already in use

```bash
streamlit run app.py --server.port 8501
```

### Module not found errors

- Ensure all files are in the same directory
- Reinstall dependencies: `pip install -r requirements.txt`

## 🤝 Contributing

Feel free to modify and improve the agents, tasks, and tools to suit your needs!

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Copyright © 2025 Wasim Ansari. All rights reserved.

## 🙋 Support

For issues or questions:

1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure your Mistral API key is valid
4. Review the CrewAI documentation: [docs.crewai.com](https://docs.crewai.com)

---

**Happy Planning! 🌍✈️🗺️**
