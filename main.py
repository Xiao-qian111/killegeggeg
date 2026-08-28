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

if "petals" not in st.session_state:
    st.session_state.petals = [
        ["None", 0, 0, 5],
        ["Basic", 10, 0, 5],
        ["gunmu", 0, 10, 0],
        ["sccutter", 15, 0, 0],
        ["egeggeg", 0, ".", 0],
        ["cutegay", 5, 5, 0]
    ]

if "using" not in st.session_state:
    st.session_state.using = []

# Start
if "stage" not in st.session_state:
    st.session_state.stage = 0
    
if st.session_state.stage == 0:
    with emp.container():
        ti("Is SCXG a sb?")
        yes = bu("Yes", "scsb")
        no = bu("No", "scgood")
    if yes:
        emp.empty()
        getout("SCXG isn't a sb")
    if no:
        st.session_state.stage = 1
        st.rerun()

elif st.session_state.stage == 1:
    with emp.container():
        ti("Is Egeggeg a sb?")
        yes = bu("Yes", "egsb")
        no = bu("No", "eggood")
    if no:
        emp.empty()
        getout("Egeggeg is a sb")
    if yes:
        st.session_state.stage = 2
        st.rerun()

elif st.session_state.stage == 2:
    with emp.container():
        ti("Killegeggeg Game")
        gogogo = bu("Start▶️", "gogogo")
        if gogogo:
            su("Please click it again after a while (this is a bug, idk why)")
            st.session_state.stage = 3

elif st.session_state.stage == 3:
    options = []
    for petal in st.session_state.petals:
        for i in range(petal[3]):
            options.append(petal[0])
    st.subheader("You can choose 5 petals")
    selected = []
    for i in range(len(options)):
        checked = st.checkbox(options[i], key = i)
        if checked:
            selected.append(options[i])
    if len(selected) > 5:
        st.warning("You choosed too much!")
    else:
        st.info(f"Selected {len(selected)}/5：{selected}")
    if len(selected) == 5 and st.button("Done"):
        st.session_state.using = selected
        st.success(f"Choosed: {selected}")
