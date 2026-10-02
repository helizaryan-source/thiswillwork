import streamlit as st

st.header("Hannah's Sweet Treats Quiz 🍰✨")
st.text("What sweet treat should Hannah make you based on your personality? Take the quiz to get your personalized dessert!")

st.image("Lab01_WebDev_Ryan/Images/sweetTreat.jpg", caption = "So many choices...")

st.divider()#########

st.subheader("First, I need to know if you even LIKE sweets! 😋")

sweetTooth = st.slider("How big is your sweet tooth?", 0, 100) 
st.write(sweetTooth) #NEW

dailyTreat = st.selectbox( #NEW
    "How often do you enjoy a sweet treat?",
    ("Once a month", "Once a week", "Every other day", "Every day", "Every meal!!!", "Ew, never"),
    )
st.image("Lab01_WebDev_Ryan/Images/dessertquote.jpg")
st.divider()########

st.subheader("Now, how do you like your sweets?")

dessertType = st.radio( #NEW
    "Hot or Not?",
    ["Hot", "Not", "In between"],
    captions=[
        "Fresh from the oven",
        "Frozen treats for me, please",
        "Love a baked treat, but not one that'll burn my tongue...",
        ],
    )

flavor = st.radio(
    "How about a fav flav?",
    ["Fresh and fruity for me!", "Chocolate.", "Classic vanilla", "Rich and full of depth", "Is cozy a flavor?"],
    captions =[
        "Nature's candy",
        "Always chocolate.",
        "It's ok to be basic, I'm not judging",
        "So chic, love that for you",
        "Yes, and its the best one",
        ],
    )

texture = st.radio(
    "Chewy, Gooey, or Crunchy?",
    ["Chewy", "Gooey", "Crunchy"]
    )

toppings = st.multiselect( #NEW
    "Pick your favorite toppings!",
    ["RAINBOW SPRINKLES!!!", "Fudge", "Caramel", "Frosting", "Whipped cream"],
    )
toppingStorage=""
for item in toppings:
    toppingStorage += item


st.image("Lab01_WebDev_Ryan/Images/baking.jpg", caption = "Baking in progress...")


submission = st.button("Click to submit your preferences!")
if submission:
    st.write("Results Below!")
else:
    st.write("Calculating...")

#####################################################

def finalResults():
    dessertFinal = None
    if dailyTreat=="Ew, never" or sweetTooth <= 10:
        dessertFinal = "No treat for you! 😢😖"
        description = "You're not into sweet treats, and who am I to force you to have one?"
        toppingWords = ""
        

    else:
        if dailyTreat=="Every meal!!!" or sweetTooth == 100:
            st.badge("Certified Sweetheart!", icon=":material/star:", color="yellow")
        
    
        if dessertType == "Hot":
            heat = "Freshly-baked"
        else:
            heat = ""

        if dessertType =="Not":
            description = "Cool off with Hannah's favorite chilled treat!🔥🥵"
            icecreamFlavor = ""
            if flavor == "Fresh and fruity for me!":
                icecreamFlavor += "Mango"
            elif flavor == "Chocolate.":
                icecreamFlavor += "Chocolate"
            elif flavor == "Classic vanilla":
                icecreamFlavor += "Vanilla Bean"
            elif flavor == "Rich and full of depth":
                icecreamFlavor += "Toasted Caramel Coffee"
            else:
                icecreamFlavor += "Pumpkin Spice"
            dessertFinal = f"Homemade {icecreamFlavor} Ice Cream"
        else:
                
               
            if flavor =="Classic vanilla":
                if texture == "Gooey":
                    dessertFinal = "Frosted Vanilla Cake 🍰"
                    description = "You keep it simple when it comes to sweets, and that's all fine by me!"
                else:
                     dessertFinal = f"{heat} Sugar Cookies 🍪"
                     description = "You may be basic, but that doesn't mean you don't have good taste"
                    
            elif flavor =="Is cozy a flavor?":
                 description = "Cozy up with your perfectly spiced treat! You and Hannah would get along well."
                 if texture == "Gooey":
                       dessertFinal = f"{heat} Apple Pie 🍎"
                 else:
                        dessertFinal =f"{heat} Snickerdoodle Cookies 🍪"
            elif flavor == "Rich and full of depth":
                 dessertFinal = "Red Velvet Cheesecake ♛"
                 description = "How does it feel being so chic?"
            elif flavor == "Chocolate.":
                if texture == "Chewy":
                    dessertFinal = f"{heat} Brownies 💩"
                    description = "Enjoy this classic dessert with any of your favorite toppings!"
                else:
                    dessertFinal = "Chocolate Fudge 💩"
                    description = "A classic treat for someone who likes to stray from the standard while still keeping it simple!"
            elif flavor == "Fresh and fruity for me!":
                dessertFinal = f"{heat} Cherry Pie Bites"
                description = "Hannah isn't a big fan of fruit in her desserts, but she'll make an exception just for you!"

            if dessertFinal == None:
                dessertFinal = f"{heat} Chocolate Chip Cookies 🍪"
                description = "The ultimate classic. Enjoy one cookie, two, or maybe the whole batch!"
        toppingWords = "Feel free to add on your favorite toppings!"
        
    st.header(dessertFinal)
    st.text(description)
    st.text(toppingWords)
    st.text(toppings)
    
            
if submission:
    finalResults()
    
    
