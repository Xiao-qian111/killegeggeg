# Some codes are by AI
import streamlit as st
import random as r
import datetime

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

# Petals setting

def dice():
    item = st.session_state.petals[8].copy()
    item[1] = r.randint(1, 6) * 5
    st.session_state.petals[8] = item

def gamble():
    item = st.session_state.petals[9].copy()
    ran = r.randint(1, 3)
    if ran == 1:
        item[1] = 15
        item[2] = 0
    elif ran == 2:
        item[1] = 35
        item[2] = 0
    else:
        item[1] = 0
        item[2] = -30
    st.session_state.petals[9] = item

def sword(sheild):
    item = st.session_state.petals[10].copy()
    item[1] = sheild // 2
    st.session_state.petals[10] = item

def DMCA():
    item = st.session_state.petals[11].copy()
    ran = r.randint(0, 1)
    if ran:
        item[1] = 10000
    else:
        item[2] = 10000
    st.session_state.petals[11] = item

def killend(sheild):
    dice()
    gamble()
    sword(sheild)
    DMCA()
    del st.session_state["e_spawned"]
    if "DMCA" in st.session_state.using:
        st.session_state.petals[11][3]

if "petals" not in st.session_state:
    st.session_state.petals = [
        ["None", 0, 0, 5],
        ["Basic", 10, 0, 5],
        ["Gunmu", 0, 10, 0],
        ["SC's Cutter", 15, 0, 0],
        ["Egeggeg", -5, 25, 0],
        ["Cutegay", 5, 5, 0],
        ["Bbl15-Antagonisms", 100, -50, 0],
        ["Unknow", -10, 50, 0],
        ["Dice", 0, 0, 0],
        ["Gamble", 0, 0, 0],
        ["Sword", 0, 0, 0],
        ["DMCA", 0, 0, 0]
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

dice()
gamble()
sword(0)
DMCA()

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
    now = datetime.datetime.now()
    year = now.year
    with emp.container():
        ti("Killegeggeg Game")
        he("v1.0.0 Bug ver XD")
        su(str(year) + " SCXG Games")
        gogogo = bu("Start▶️", "gogogo")
        if gogogo:
            # su("Please click it again after a while (this is a bug, idk why)")
            st.session_state.stage = 3
            st.rerun()

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
            st.rerun()

elif st.session_state.stage == 4:
    with emp.container():
        ti("What to do?")
        inv = bu("Check inventory", "inv")
        kill = bu("Fight", "kill")
        clog = bu("Check change log", "clog")
        if inv:
            st.session_state.stage = 3
            st.rerun()
        if kill:
            st.session_state.stage = 5
            st.rerun()
        if clog:
            st.session_state.stage = 9
            st.rerun()

elif st.session_state.stage == 5:
    if "e_spawned" not in st.session_state or st.session_state.e_spawned == False:
        st.session_state.edamage = r.randint(10, 75)
        st.session_state.esheild = r.randint(0, 25)
        st.session_state.e_spawned = True
    with emp.container():
        ti("You meet an Egeggeg")
        he("Damage: " + str(st.session_state.edamage))
        he("Sheild: " + str(st.session_state.esheild))
        killit = bu("Kill", "killit")
        if killit:
            player = st.session_state.damage - st.session_state.esheild
            enemy = st.session_state.edamage - st.session_state.sheild
            if player > enemy:
                killend(st.session_state.esheild)
                st.session_state.stage = 6
                st.rerun()
            elif player == enemy:
                killend(st.session_state.esheild)
                st.session_state.stage = 7
                st.rerun()
            else:
                killend(st.session_state.esheild)
                st.session_state.stage = 8
                st.rerun()

elif st.session_state.stage == 6:
    win = r.randint(1, 5)
    gets = []
    extra = "no"
    for i in range(win):
        get = -1
        while get in LOCKED:
            get = r.randint(2, len(st.session_state.petals) - 1)
        st.session_state.petals[get][3] += 1
        gets.append(st.session_state.petals[get][0])
    if r.randint(1, 100) == 1:
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
            st.rerun()

elif st.session_state.stage == 7:
    with emp.container():
        ti("You guys are in a tie")
        inv = bu("Check inventory", "inv")
        if inv:
            st.session_state.stage = 3
            st.rerun()

elif st.session_state.stage == 8:
    with emp.container():
        ti("You lost!")
        inv = bu("Check inventory", "inv")
        if inv:
            st.session_state.stage = 3
            st.rerun()
    # I think I should add lost petals

elif st.session_state.stage == 9:
    with emp.container():
        # v1.0.1
        st.title("Sep 8th, 2026 v1.0.1")
        st.write("Add 4 new petals: Dice, Gamble, Sword and DMCA")
        # v1.0.0
        st.title("Sep 7th, 2026 v1.0.0")
        st.write("The first version lol")
        clogback = bu("Back", "clogback")
        if clogback:
            st.session_state.stage = 4
            st.rerun()
