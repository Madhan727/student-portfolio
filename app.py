import streamlit as st

st.set_page_config(page_title="Student Portfolio", page_icon=":mortar_board:", layout="wide")

profile_pic_url = r"C:\Users\Madhanraj.D\Downloads\madhanraj.jpeg" 
col1,col2,col3=st.columns([1,2,3])
with col1:
    st.image(profile_pic_url, width=200)
with col2:
    st.title("D.Madhanraj")
    st.write("**Student | Major in Artificial inteligence and machine learning**")
    st.write("📍 Erode")

    st.markdown(
        """
        📧 *Email:* [madhand727@gmail.com](mailto:madhand727@gmail.com)  
        🔗 *LinkedIn:* [Madhan D](https://www.linkedin.com/in/madhan-d-3340b2315/)  
        """
    )

st.header("About Me")
st.write(
    """
    I am currently a B.E CSE[AIML] student at kgisl intitute of tecnology, passionate about  software development, artificial intelligence.
    My studies have equipped me with knowledge in machine learning, web development.
    I am eager to apply my skills in real-world projects and am actively seeking internship opportunities.
    """
)

st.header("Education")
st.write("### B.E CSE(AIML)")
st.write("##### kgisl institute of technology | **BATCH NO:** 2024-28")

st.subheader("Relevant Coursework")
courses = ["###### Introduction to Programming","###### Data Structures and Algorithms","###### Machine Learning","###### Database Systems"]
for course in courses:
    st.write(f"- {course}")

st.header("Skills")
st.write("**Programming Languages**ㅤ: Python, Java, SQL")
st.write("**Tools & Technologies**ㅤ: Git, Streamlit, Excel")
st.write("**Soft Skills** ㅤ: Teamwork, Problem-solving, Time management")

st.header("Academic Projects")

st.write("### Project 1: Title (e.g., Personal Portfolio Website)")
st.write(
    """
    - Description: Created a personal portfolio website using Streamlit.
    - Tools: Streamlit, Python
    - Skills Developed: Web development, UI design
    """
)

st.header("Extracurricular Activities")
st.write(" participated in coding challenges and hackathons.")
st.write("Volunteered as a tutor for introductory programming courses.")

st.markdown("---")
st.write("Thanks for visiting my portfolio! Feel free to reach out via email or LinkedIn for any opportunities")