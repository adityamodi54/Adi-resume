import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)

def main():
    # Advanced CSS and HTML for enhanced appearance and icons
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;  /* Light grey background for a softer look */
            color: #333333;
        }
        h1 {
            color: #0068c9; /* Blue for main titles */
        }
        h2, h3 {
            color: #ff6347; /* Tomato red for subheadings */
            margin-top: 40px; /* Space above headers for clarity */
        }
        p, li {
            color: #4a4a4a; /* Dark grey for text for better readability */
            font-size: 18px; /* Larger font size */
        }
        .icon {
            font-size: 25px; /* Size of the icons */
            color: #ff6347; /* Matching the headers */
            padding-right: 10px; /* Space between icon and text */
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("🧳 Jane Doe's Resume")

    # Load local Lottie animation
    animation_welcome = load_lottiefile("Animation1713721671069.json")
    
    # Layout using columns for a dynamic feel
    col1, col2 = st.columns([2, 1])  # Optimized layout ratio
    with col1:
        st.markdown("""
            ## 📞 Contact Information
            - **Email:** `jane.doe@example.com`
            - **Phone:** `+1234567890`
            - **Location:** `San Francisco, CA`
        """)
        st.markdown("""
            ## 📝 Professional Summary
            *Experienced software developer with over 10 years of experience specializing in front-end development.
            Strong background in project management and customer relations. Committed to high standards of user experience,
            optimizing performance, and collaborating effectively with team members.*
        """)
        st.markdown("""
            ## 💼 Work Experience
            **Senior Software Developer**  
            *Tech Solutions Inc., San Francisco, CA*  
            **June 2015 - Present**
            - Lead a team of 10 developers in creating information systems for clients in the finance industry.
            - Focus on improving application responsiveness and streamline functionalities.
            - Conduct code reviews, mentor junior developers, and manage project timelines.
        """)
        st.markdown("""
            ## 🎓 Education
            **Bachelor of Science in Computer Science**  
            *University of California, Berkeley*  
            **2005 - 2009**
        """)
        st.markdown("""
            ## 🛠 Skills
            - **Programming Languages:** Python, JavaScript, C#
            - **Frameworks:** React, Angular
            - **Tools:** Git, Docker, Jenkins
            - **Other:** Agile Methodologies, UX Design
        """)
    with col2:
        if animation_welcome:
            st_lottie(animation_welcome, height=300, key="welcome")  # Adjust height as needed
        else:
            st.error("Failed to load local Lottie animation.")

if __name__ == "__main__":
    main()
