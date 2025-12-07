from crewai import Task
from datetime import datetime

def location_task(agent, from_city, destination_city, date_from, date_to):
    """
    Task for Location Expert to research destination information
    """
    return Task(
        description=f"""Research comprehensive travel information for a trip from {from_city} to {destination_city}
        between {date_from} and {date_to}.
        
        Use the search_web_tool to find current information about:
        
        1. **Visa Requirements**: Check if travelers from {from_city} need a visa for {destination_city}
        2. **Flight Options**: Research available flights, approximate costs, and travel time
        3. **Local Transportation**: Research metro, buses, taxis, and ride-sharing options in {destination_city}
        4. **Weather**: Check typical weather conditions for {destination_city} during the travel dates
        5. **Safety Information**: Research current safety advisories and travel warnings
        6. **Currency & Budget**: Research local currency, exchange rates, and general cost of living
        
        IMPORTANT: You MUST use the search_web_tool for each of these topics to get current, accurate information.
        Do not rely on general knowledge alone - search for specific, up-to-date information.""",
        expected_output="""A comprehensive report including:
        - Visa requirements and application process (if needed)
        - Flight options with estimated costs
        - Local transportation guide with prices
        - Weather forecast and packing recommendations
        - Safety tips and emergency contacts
        - Budget estimates for accommodation, food, and activities
        - Currency information and exchange tips""",
        agent=agent,
    )

def guide_task(agent, destination_city, interests, date_from, date_to):
    """
    Task for Local Guide Expert to provide recommendations
    """
    return Task(
        description=f"""Act as a local guide for {destination_city} and create personalized recommendations
        for a traveler interested in: {interests}.
        
        Trip dates: {date_from} to {date_to}
        
        Use the search_web_tool to research and provide:
        
        1. **Top Attractions**: Must-see landmarks and attractions matching the interests
        2. **Local Restaurants**: Highly-rated local eateries (not tourist traps) serving authentic cuisine
        3. **Cultural Experiences**: Museums, theaters, festivals, or events happening during the travel dates
        4. **Hidden Gems**: Lesser-known spots that locals love
        5. **Food Recommendations**: Specific dishes to try and where to find them
        6. **Nightlife/Entertainment**: Evening activities, bars, clubs, or live music venues
        7. **Shopping Areas**: Local markets, boutiques, or shopping districts
        
        IMPORTANT: Search for current information including recent reviews, opening hours, and any special events
        or closures during the travel period.""",
        expected_output="""A detailed local guide including:
        - Top 10-15 attractions with descriptions and why they match the interests
        - 8-10 restaurant recommendations with specific dishes to try
        - Cultural events or festivals happening during the visit
        - 5-7 hidden gems off the beaten path
        - Neighborhood guide with character descriptions
        - Practical tips (best times to visit attractions, how to avoid crowds)
        - Local customs and etiquette tips""",
        agent=agent,
    )

def planner_task(context_tasks, agent, destination_city, interests, date_from, date_to):
    """
    Task for Travel Planner Expert to create the final itinerary
    """
    # Calculate trip duration
    trip_duration = (date_to - date_from).days + 1
    
    return Task(
        description=f"""Create a comprehensive, day-by-day travel itinerary for {destination_city}
        from {date_from} to {date_to} ({trip_duration} days).
        
        Traveler interests: {interests}
        
        Use information from the Location Expert and Local Guide Expert (provided in context),
        and use the search_web_tool to verify current information about:
        
        1. **Accommodation**: Research 3-4 hotel/accommodation options with prices
        2. **Daily Itinerary**: Create hour-by-hour plans for each day
        3. **Activity Booking**: Note which activities need advance booking
        4. **Meal Planning**: Suggest specific restaurants for breakfast, lunch, and dinner
        5. **Transportation**: Include travel time between activities and transportation methods
        6. **Budget Breakdown**: Provide daily and total budget estimates
        7. **Practical Tips**: Booking links, contact numbers, and reservation recommendations
        
        The itinerary should:
        - Balance activities with rest time
        - Group nearby attractions together to minimize travel
        - Include backup options in case of bad weather
        - Consider opening hours and peak times
        - Stay within a reasonable budget
        
        IMPORTANT: Search for current prices, opening hours, and booking requirements.""",
        expected_output=f"""A complete travel plan document including:
        
        **EXECUTIVE SUMMARY**
        - Trip overview and highlights
        - Total estimated budget breakdown
        - Key booking priorities
        
        **ACCOMMODATION OPTIONS**
        - 3-4 recommended hotels/accommodations with prices, locations, and pros/cons
        
        **DAY-BY-DAY ITINERARY** (for all {trip_duration} days)
        For each day:
        - Morning activities (with times and locations)
        - Lunch recommendation
        - Afternoon activities (with times and locations)
        - Dinner recommendation
        - Evening activities (optional)
        - Daily budget estimate
        - Transportation notes
        
        **BOOKING CHECKLIST**
        - Activities requiring advance booking with links/contacts
        - Restaurant reservations needed
        - Transportation tickets to purchase
        
        **PACKING LIST**
        - Based on weather and planned activities
        
        **EMERGENCY INFORMATION**
        - Important phone numbers
        - Hospital/clinic locations
        - Embassy contact information
        
        The plan should be detailed, practical, and ready to execute.""",
        agent=agent,
        context=context_tasks,
    )