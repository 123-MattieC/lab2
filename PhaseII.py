import streamlit as st
import pandas as pd
import json
import numpy as np




#the three NEW functions 
def introSection():
    st.title("All About Me 😆")#NEW
    st.caption("Get Ready to Learn.....")#NEW
    response = st.chat_input()#NEW
    st.subheader("Write your favorite thing about me in the text box at the bottom of the page:) ")
    if response != None:
        st.write(f"Your favorite thing about me is: {response} .... I knew you loved me!")
    else:
        st.write("let's hear it....")
introSection()


#sessionstate
st.header("Fun Facts!")

if "age" not in st.session_state:
    st.session_state.age = 19  

if "favorite_number" not in st.session_state:
    st.session_state.favorite_number = 23  


st.write(f"**My Age:** {st.session_state.age}")
st.write(f"**My Favorite Number:** {st.session_state.favorite_number}")

st.subheader("...Now about you")


st.session_state.age = st.number_input("What is your age", value=st.session_state.age, step=1)
st.session_state.favorite_number = st.number_input("What your favorite number", value=st.session_state.favorite_number, step=1)


st.write("### We are now one in the same:)")
st.write(f"**Age:** {st.session_state.age}")
st.write(f"**Favorite Number:** {st.session_state.favorite_number}")



# two user input interactions (trivia and fav thing)
def trivia():
    st.header("TRIVIA")
    q1 = st.selectbox(
        'How many siblings do I have?',
        ["",0,1,2,3,4,5,6])
    if q1 == 3:
        st.write("Correct!")
    elif q1 != "":
        st.write('Hmmmm not quite right... better luck next tine:)')
    else:
        st.write("...waiting on the answer")

    q2= st.selectbox(
        "What is my favorite color?",
        ["","red","blue","green","purple","pink"])

    if q2== "blue":
        st.write("That's right!")
    elif q1 != "":
        st.write("Sorry, not quite right:(")
    else:
        st.write("...waiting on the answer")

    q3= st.selectbox(
        "Where am I from?",
        ["","AL","GA","NY","MT","RD"])
    
    if q3== "GA":
        st.write("You got it!")
    elif q3 != "":
        st.write("Nope....")
    else:
        
        st.write("...waiting on the answer")
trivia()

#3 uses of Data Visualization (static is My HW, dynamic is table and User HW)
def visuals():

    st.header("Spring Break Locations and their ranking (check where you are going)")
    df = pd.DataFrame(
    [
       {"Spring Break Locations": "PCB", "Rank": 2, "Where are You Going?": False},
       {"Spring Break Locations": "Santa Barbra", "Rank": 1, "Where are You Going?": False},
       {"Spring Break Locations": "Gulf Shores", "Rank": 3, "Where are You Going?": False},
    ]
    )
    edited_df = st.data_editor(df)  


    st.header("How much homework I do in a week")
    frame = pd.DataFrame(
    [
       {"Day": "Monday", "Hours": 2,},
       {"Day": "Tuesday", "Hours": 1.5, },
       {"Day": "Wednesday", "Hours": 4,},
       {"Day": "Thursday", "Hours": 7,},
       {"Day": "Friday", "Hours": 3.5,}
    ])
    
    frame= frame.set_index("Day")
    
    st.bar_chart(frame['Hours'])

    st.header("How much homework YOU do in a week")

    y1 = st.number_input("Monday:", value=0)
    y2 = st.number_input("Tuesday", value=0)
    y3 = st.number_input("Wednesday", value=0)
    y4 = st.number_input("Thursday", value=0)
    y5 = st.number_input("Friday", value=0)

    days = pd.Categorical(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    ordered=True
)

    data = pd.DataFrame({
        'y': [y1, y2, y3, y4, y5]
    }, index = days)

    
    st.line_chart(data)

visuals()

#data plotted from a .json file
def usingjson():
     st.header("Where does my money go?")
     infile=open("data.json") # inside of the parentheses should be the name of your .json file
     myData = json.load(infile)# converts json data into a python dictionary or list

     md= pd.DataFrame(myData)

     md= md.set_index("Category")

     st.bar_chart(md["Money"])
    
usingjson()
