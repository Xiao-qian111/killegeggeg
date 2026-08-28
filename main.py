# Some codes are by AI
import streamlit as st

emp = st.empty()

def ti(text):
    st.title(text, text_alignment="center")

def he(text):
    st.header(text, text_alignment="center")

def su(text):
    st.subheader(text, text_alignment="center")

def bu(text, id):
    _, c_center, _ = st.columns([1, 1.2, 1])
    with c_center:
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
start_flag = [False, False]
if not start_flag[0]:
    start_flag[1] = True
    ti("Is SCXG a sb?")
    yes = bu("Yes", "scsb")
    no = bu("No", "scgood")
    if yes:
        st.empty()
        getout("SCXG isn't a sb")
    if no:
        start_flag[0] = True
        start_flag[1] = False

if not start_flag[1]:
    st.title(emp, "Is Egeggeg a sb?", text_alignment="center")
    yes = bu("Yes", "egsb")
    no = bu("No", "eggood")
    if no:
        st.empty()
        getout("Egeggeg is a sb")
    if yes:
        start_flag[1] = True
