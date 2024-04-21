import streamlit as st

def main():
    # Custom CSS to improve the appearance of the resume
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Open Sans', sans-serif;
            background-color: #f3f2ef;
            color: #333;
        }
        .block-container {
            padding: 2rem;
            max-width: 800px;
            margin: auto;
        }
        h2 {
            border-bottom: 2px solid #0c6efc;
            padding-bottom: 0.5rem;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Jane Doe's Resume")

    st.markdown("""
        ## Contact Information
        - **Email:** jane.doe@example.com
        - **Phone:** +1234567890
        - **Location:** San Francisco, CA
    """)

    st.markdown("""
        ## Professional Summary
        Experienced software developer with over 10 years of experience specializing in front-end development.
        Strong background in project management and customer relations. Committed to high standards of user experience,
        optimizing performance, and collaborating effectively with team members.
    """)

    st.markdown("""
        ## Work Experience
        **Senior Software Developer**  
        *Tech Solutions Inc., San Francisco, CA*  
        **June 2015 - Present**
        - Lead a team of 10 developers in creating information systems for clients in the finance industry.
        - Focus on improving application responsiveness and streamline functionalities.
        - Conduct code reviews, mentor junior developers, and manage project timelines.
    """)

    st.markdown("""
        ## Education
        **Bachelor of Science in Computer Science**  
        *University of California, Berkeley*  
        **2005 - 2009**
    """)

    st.markdown("""
        ## Skills
        - **Programming Languages:** Python, JavaScript, C#
        - **Frameworks:** React, Angular
        - **Tools:** Git, Docker, Jenkins
        - **Other:** Agile Methodologies, UX Design
    """)

if __name__ == "__main__":
    main()
