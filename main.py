# Some codes are by AI
import streamlit as st
import random as r

LOCKED = [-1, 6, 7]

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
        ["Gunmu", 0, 10, 0],
        ["SC's Cutter", 15, 0, 0],
        ["Egeggeg", -5, 25, 0],
        ["Cutegay", 5, 5, 0],
        ["Bbl15-Antagonisms", 100, -50, 0],
        ["Unknow", -10, 50, 0]
    ]

if "id" not in st.session_state:
    st.session_state.id = {}
    i = 0
    for p in st.session_state.petals:
        st.session_state.id[p[0]] = i
        i += 1

if "using" not in st.session_state:
    st.session_state.using = []

if "damage" not in st.session_state:
    st.session_state.damage = 0
if "sheild" not in st.session_state:
    st.session_state.sheild = 0
if "edamage" not in st.session_state:
    st.session_state.edamage = 0
if "esheild" not in st.session_state:
    st.session_state.esheild = 0

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
    with emp.container():
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
            for item in selected:
                st.session_state.damage += st.session_state.petals[st.session_state.id[item]][1]
                st.session_state.sheild += st.session_state.petals[st.session_state.id[item]][2]
            st.session_state.stage = 4

elif st.session_state.stage == 4:
    with emp.container():
        ti("What to do?")
        inv = bu("Check inventory", "inv")
        kill = bu("Fight", "kill")
        if inv:
            st.session_state.stage = 3
        if kill:
            st.session_state.stage = 5

elif st.session_state.stage == 5:
    st.session_state.edamage = r.randint(10, 75)
    st.session_state.esheild = r.randint(0, 25)
    with emp.container():
        ti("You meet an Egeggeg")
        he("Damage: " + str(st.session_state.edamage))
        he("Sheild: " + str(st.session_state.esheild))
        killit = bu("Kill", "killit")
        if killit:
            player = st.session_state.damage - st.session_state.esheild
            enemy = st.session_state.edamage - st.session_state.sheild
            if player > enemy:
                st.session_state.stage = 6
            elif player == enemy:
                st.session_state.stage = 7
            else:
                st.session_state.stage = 8

elif st.session_state.stage == 6:
    win = r.randint(1, 5)
    gets = []
    extra = "no"
    for i in range(win):
        get = -1
        while get in LOCKED:
            get = r.randint(0, len(st.session_state.petals) - 1)
        st.session_state.petals[get][3] += 1
        gets.append(st.session_state.petals[get][0])
    if r.randint(1, 100):
        what = LOCKED[r.randint(0, len(LOCKED) - 1)]
        st.session_state.petals[what][3] += 1
        extra  = st.session_state.petals[what][0]
    with emp.container():
        ti("You win!")
        he(f"You get: {gets}")
        if extra != "no":
            he("And a secret petal: " + str(extra))
        inv = bu("Check inventory", "inv")
        if inv:
            st.session_state.stage = 3

elif st.session_state.stage == 7:
    with emp.container():
        ti("You guys are in a tie")
        inv = bu("Check inventory", "inv")
        if inv:
            st.session_state.stage = 3

elif st.session_state.stage == 8:
    with emp.container():
        ti("You lost!")
        inv = bu("Check inventory", "inv")
        if inv:
            st.session_state.stage = 3
    # I think I should add lost petals
