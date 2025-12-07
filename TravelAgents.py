from crewai import Agent, LLM
from TravelTools import search_web_tool
import os
from dotenv import load_dotenv
load_dotenv()

# Load Mistral API key from environment variables
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Initialize the language model
llm = LLM(model="mistral/mistral-small-latest", temperature=0.2)

# Location Expert Agent
location_expert = Agent(
    role="Location Expert",
    goal="Research and provide comprehensive information about travel destinations, including visa requirements, transportation options, weather, and safety information.",
    backstory="""You are an experienced travel consultant specializing in destination research.
    You have extensive knowledge about visa requirements, flight options, local transportation,
    weather patterns, and safety considerations for travelers worldwide. You always use web search
    to get the most current and accurate information.""",
    llm=llm,
    tools=[search_web_tool],
    verbose=True,
    allow_delegation=False,
)

# Local Guide Expert Agent
guide_expert = Agent(
    role="Local Guide Expert",
    goal="Provide insider knowledge about local attractions, restaurants, cultural experiences, and hidden gems based on traveler interests.",
    backstory="""You are a knowledgeable local guide who has lived in numerous cities worldwide.
    You specialize in creating authentic travel experiences by recommending the best local spots,
    cultural activities, restaurants, and attractions. You stay updated on current events and
    new openings by searching the web. You tailor recommendations to match traveler preferences.""",
    llm=llm,
    tools=[search_web_tool],
    verbose=True,
    allow_delegation=False,
)

# Travel Planner Expert Agent
planner_expert = Agent(
    role="Travel Planner Expert",
    goal="Create comprehensive day-by-day travel itineraries that include accommodations, activities, dining, and logistics, optimized for budget and preferences.",
    backstory="""You are a professional travel planner with years of experience creating
    detailed itineraries. You excel at organizing trips efficiently, considering travel time,
    budget constraints, and client preferences. You synthesize information from location and
    guide experts to create seamless travel plans. You use web search to verify current prices,
    opening hours, and booking information.""",
    llm=llm,
    tools=[search_web_tool],
    verbose=True,
    allow_delegation=False,
)