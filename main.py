import streamlit as st

def ti(text):
    st.title(text, text_alignment="center")

def he(text):
    st.header(text, text_alignment="center")

def su(text):
    st.subheader(text, text_alignment="center")

def getout(why):
    ti("Get Out")
    he("Please reload if " + why)
    st.stop()

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
    ti("Is SCXG a sb?")
    yes = st.button("Yes")
    no = st.button("No")
    if yes:
        getout("SCXG isn't a sb")
    if no:
        start_flag[0] = True

if not start_flag[1]:
    ti("Is Egeggeg a sb?")
    yes = st.button("Yes")
    no = st.button("No")
    if no:
        getout("Egeggeg is a sb")
    if yes:
        start_flag[1] = True
