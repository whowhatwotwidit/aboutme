from pathlib import Path
import streamlit as st 
from PIL import Image


# LOADING ALL DATA
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "style.css"
cv_file = current_dir / "asset" / "CV_PAREL.pdf"
profile_picture = current_dir / "asset" / "profile_picture.png"

Title = "Digital CV | Earl Parel"
Icon = ":scroll:"
Name = "Earl Parel"
Description = """
ECE Graduate of Mapua University
"""
Email = "earllevip@gmail.com"
Socials = {
    "LinkedIn" : "www.linkedin.com/in/earlparel",
    "GitHub" : "https://github.com/whowhatwotwidit",
}

# END OF LOADING

#START OF STREAMLIT CODE
st.set_page_config(page_title=Title, page_icon=Icon)
# INITIATING IMPORT FILES
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    PDF = pdf_file.read()
profile_pic = Image.open(profile_picture)   
#OUTPUT
col1, col2 = st.columns([.45,.55],gap="small")
#col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label="Download",
        data = PDF,
        file_name = cv_file.name,
        mime="application/octect-stream"

    )
    st.write(":inbox_tray:",Email)

#GAP
st.write("#")
cols = st.columns(len(Socials))
for index, (platform,link) in enumerate(Socials.items()):
    cols[index].write(f"[{platform}]({link})")

#GAP
st.write("---")
st.write("#")
st.subheader("Education")
st.write("""
    - :ballot_box_with_check: Statefields School: Preschool
    - :ballot_box_with_check: Elizabeth Seton School-South: GS and JHS
    - :ballot_box_with_check: Mapua University: SHS(STEM) and ECE
    """)

st.write("#")
st.subheader("Skills")
st.write("""
    - :computer: Programming Languages: Java, Python, Kotlin
    - :electric_plug: Interests: Arduino, Raspberry Pi, NXT Bricks, App Development, Web Application Development, and Automation
    - :office: Skills: MS Office, Illustrator, Premiere Pro, and Photoshop
    - :male-factory-worker: Projects Done: Object Detection and Visualization
    - :globe_with_meridians: ECE Specializing in AIPN and currently studying for CCNA

    """)

st.write("#")

with st.container():
    st.write("---")
    st.subheader("send a message!")
    contact_form = """
    <form action="https://formsubmit.co/earl.parel@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="name" required>
     <input type="email" name="email" placeholder="email" required>
     <textarea name="message" placeholder="message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    lcol,rcol = st.columns(2)
    with lcol:
        st.markdown(contact_form,unsafe_allow_html=True)
    with rcol:
        st.empty()
