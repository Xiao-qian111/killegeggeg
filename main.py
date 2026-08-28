# Some codes are by AI
import streamlit as st

def ti(text):
    st.title(text, text_alignment="center")

def he(text):
    st.header(text, text_alignment="center")

def su(text):
    st.subheader(text, text_alignment="center")

def bu(text, id, em = True):
    _, c_center, _ = st.columns([1, 1.2, 1])
    with c_center:
        if em:
            emp = st.empty()
            tmp = emp.button(text, key = id)
        else:
            tmp = st.button(text, key = id)
    return tmp

def getout(why):
    ti("Get Out")
    he("Please reload if " + why)

petals = [
    ["Basic", 10, 0, 5],
    ["gunmu", 0, 10, 0],
    ["sccutter", 15, 0, 0],
    ["egeggeg", 0, ".", 0],
    ["cutegay", 5, 5, 0]
]

# Start
if "stage" not in st.session_state:
    st.session_state.stage = 0
emp = st.empty()
if st.session_state.stage == 0:
    emp.title("Is SCXG a sb?", text_alignment="center")
    yes = bu("Yes", "scsb")
    no = bu("No", "scgood")
    if yes:
        emp.empty()
        getout("SCXG isn't a sb")
    if no:
        st.session_state.stage = 1
        st.rerun()

elif st.session_state.stage == 1:
    emp.title("Is Egeggeg a sb?", text_alignment="center")
    yes = bu("Yes", "egsb")
    no = bu("No", "eggood")
    if no:
        emp.empty()
        getout("Egeggeg is a sb")
    if yes:
        pass
