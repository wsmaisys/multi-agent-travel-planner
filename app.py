from TravelAgents import guide_expert, location_expert, planner_expert
from TravelTasks import location_task, guide_task, planner_task
from crewai import Crew, Process
import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="🌍 Trip Planner", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
/* Center title and description */
h1 {
    text-align: center;
}
.center-text {
    text-align: center;
    font-size: 1.1em;
    line-height: 1.6;
    margin: 20px 0;
}
.button-container {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin: 30px 0;
}
.agent-section {
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
    border-left: 4px solid #1f77b4;
}
.location-section {
    background-color: #e3f2fd;
    border-left-color: #1976d2;
}
.guide-section {
    background-color: #f3e5f5;
    border-left-color: #7b1fa2;
}
.planner-section {
    background-color: #e8f5e9;
    border-left-color: #388e3c;
}
</style>
""", unsafe_allow_html=True)

# Streamlit App Title
st.title("🌍 AI-Powered Trip Planner")

# Centered description
st.markdown("""
<div class="center-text">
💡 <b>Plan your next trip with AI!</b><br>
Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
<br><br>
🎡 Best places to visit &nbsp; | &nbsp; 💰 Accommodation & budget planning<br>
🍕 Local food recommendations &nbsp; | &nbsp; 🚆 Transportation & visa details
</div>
""", unsafe_allow_html=True)

st.divider()

# User Inputs - Not in Sidebar (now in main area)
col1, col2 = st.columns(2)
with col1:
    from_city = st.text_input("🏡 From City", "New Delhi")
    date_from = st.date_input("📅 Departure Date")
    
with col2:
    destination_city = st.text_input("✈️ Destination City", "Rome")
    date_to = st.date_input("📅 Return Date")

interests = st.text_area("🎯 Your Interests", "sightseeing and good food", height=80)

# Initialize session state for storing responses
if "location_response" not in st.session_state:
    st.session_state.location_response = None
if "guide_response" not in st.session_state:
    st.session_state.guide_response = None
if "planner_response" not in st.session_state:
    st.session_state.planner_response = None
if "execution_log" not in st.session_state:
    st.session_state.execution_log = []

# Button to run CrewAI - Centered below inputs
st.divider()
col_button = st.columns([1, 2, 1])
with col_button[1]:
    generate_btn = st.button("🚀 Generate Travel Plan", use_container_width=True, key="generate_btn")
st.divider()

# Run CrewAI
if generate_btn:
    if not from_city or not destination_city or not date_from or not date_to or not interests:
        st.error("⚠️ Please fill in all fields before generating your travel plan.")
    else:
        # Reset session state
        st.session_state.execution_log = []
        
        # Create placeholder containers for streaming
        status_placeholder = st.empty()
        results_container = st.container()
        
        try:
            with status_placeholder.status("🔄 Generating your travel plan...", expanded=True):
                # Create all tasks first (don't execute yet)
                st.write("📋 Setting up travel planning workflow...")
                
                loc_task = location_task(location_expert, from_city, destination_city, date_from, date_to)
                guid_task = guide_task(guide_expert, destination_city, interests, date_from, date_to)
                plan_task = planner_task([loc_task, guid_task], planner_expert, destination_city, interests, date_from, date_to)
                
                # Option 1: Run all agents in a single crew (RECOMMENDED)
                st.write("🤖 Starting AI agents workflow...")
                
                crew = Crew(
                    agents=[location_expert, guide_expert, planner_expert],
                    tasks=[loc_task, guid_task, plan_task],
                    process=Process.sequential,
                    verbose=True,
                )
                
                st.write("⚙️ Executing travel planning...")
                result = crew.kickoff()
                
                # Extract individual task outputs
                if hasattr(result, 'tasks_output') and result.tasks_output:
                    st.write("✅ All agents completed successfully!")
                    
                    # Get individual task results
                    if len(result.tasks_output) >= 3:
                        st.session_state.location_response = str(result.tasks_output[0].raw if hasattr(result.tasks_output[0], 'raw') else result.tasks_output[0])
                        st.session_state.guide_response = str(result.tasks_output[1].raw if hasattr(result.tasks_output[1], 'raw') else result.tasks_output[1])
                        st.session_state.planner_response = str(result.tasks_output[2].raw if hasattr(result.tasks_output[2], 'raw') else result.tasks_output[2])
                    else:
                        # Fallback: use final result for all
                        final_output = result.raw if hasattr(result, 'raw') else str(result)
                        st.session_state.location_response = final_output
                        st.session_state.guide_response = final_output
                        st.session_state.planner_response = final_output
                else:
                    # Fallback for older CrewAI versions
                    final_output = result.raw if hasattr(result, 'raw') else str(result)
                    st.session_state.planner_response = final_output
                    st.session_state.location_response = "Included in final plan"
                    st.session_state.guide_response = "Included in final plan"
                
                st.write("🎉 Travel plan generation complete!")
                
        except Exception as e:
            st.error(f"❌ Error during execution: {str(e)}")
            st.session_state.execution_log.append(f"ERROR: {str(e)}")
            
            # Show debug information
            with st.expander("🔍 Debug Information"):
                st.code(str(e))
                st.write("**Execution Log:**")
                for log in st.session_state.execution_log:
                    st.text(log)
        
        # Display Results Hierarchically
        if st.session_state.planner_response:
            st.markdown("---")
            st.subheader("📊 Travel Plan Results")
            
            # Create tabs for better organization
            tab1, tab2, tab3, tab4 = st.tabs(["📝 Full Itinerary", "📍 Location Info", "🎯 Local Guide", "📥 Downloads"])
            
            with tab1:
                st.markdown('<div class="agent-section planner-section">', unsafe_allow_html=True)
                st.markdown("### ✈️ Travel Planner Expert Report")
                st.markdown(st.session_state.planner_response)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with tab2:
                st.markdown('<div class="agent-section location-section">', unsafe_allow_html=True)
                st.markdown("### 🏢 Location Expert Report")
                if st.session_state.location_response:
                    st.markdown(st.session_state.location_response)
                else:
                    st.info("Location information is included in the final itinerary below.")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with tab3:
                st.markdown('<div class="agent-section guide-section">', unsafe_allow_html=True)
                st.markdown("### 🎭 Local Guide Expert Report")
                if st.session_state.guide_response:
                    st.markdown(st.session_state.guide_response)
                else:
                    st.info("Guide information is included in the final itinerary below.")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with tab4:
                st.markdown("### 📥 Download Your Travel Plan")
                
                # Prepare combined report
                combined_report = f"""
# 🌍 AI-POWERED TRIP PLAN TO {destination_city.upper()}

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Trip Duration:** {date_from} to {date_to}

---

## 📍 LOCATION INFORMATION
{st.session_state.location_response or 'See full itinerary below'}

---

## 🎯 LOCAL GUIDE RECOMMENDATIONS
{st.session_state.guide_response or 'See full itinerary below'}

---

## ✈️ COMPLETE TRAVEL ITINERARY
{st.session_state.planner_response}

---

**Interests:** {interests}
**Traveling from:** {from_city}
**Destination:** {destination_city}
"""
                
                # Download buttons
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.download_button(
                        label="📄 Download as Text",
                        data=combined_report,
                        file_name=f"Travel_Plan_{destination_city}_{datetime.now().strftime('%Y%m%d')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col2:
                    st.download_button(
                        label="📋 Download as Markdown",
                        data=combined_report,
                        file_name=f"Travel_Plan_{destination_city}_{datetime.now().strftime('%Y%m%d')}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                
                with col3:
                    # Prepare CSV summary
                    csv_data = f"""Attribute,Value
From City,{from_city}
Destination,{destination_city}
Departure Date,{date_from}
Return Date,{date_to}
Interests,{interests}
Generated,{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
                    st.download_button(
                        label="📊 Download Summary CSV",
                        data=csv_data,
                        file_name=f"Travel_Summary_{destination_city}_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                
                # Success message
                st.success("✅ All downloads are ready! Choose your preferred format above.")
        
        # Clear status after completion
        status_placeholder.empty()