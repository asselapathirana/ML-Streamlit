
def style(st):
    hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;} /* hide main (hamburger) menu */
footer {visibility: hidden;}  /*# hide 'made with' footer */
.css-12oz5g7 {padding-top: 1rem;} /*# remove space on top */
</style>
"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

 