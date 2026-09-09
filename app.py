import streamlit as st
import os
HF_TOKEN = os.environ.get("HF_TOKEN")
st.title("Oge")
st.subheader("Your AI Fashion Assistant")

st.write("Snap what you have. See how to style it.")

st.divider()

st.write("### 📸 Upload what you want to style")

uploaded_file = st.file_uploader(
    "Take a photo or upload a photo of your clothing",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Your item",
        use_container_width=True
    )

    st.divider()

    st.write("### ✨ Where are you going?")

    occasion = st.selectbox(
        "Choose an occasion",
        [
            "Office / Work",
            "Business Meeting",
            "Conference",
            "Job Interview",
            "Networking Event",
            "School Reunion",
            "Graduation / Convocation",
            "Award Ceremony",
            "Concert",
            "Sip & Paint",
            "Game Night",
            "Party",
            "Birthday",
            "Girls' Night Out",
            "Dinner",
            "Brunch",
            "Date",
            "Wedding",
            "Traditional Wedding",
            "Aso-Ebi Event",
            "Naming Ceremony",
            "Church",
            "Thanksgiving",
            "Beach",
            "Travel",
            "Shopping",
            "Casual Outing",
            "Weekend Outing",
            "Other"
        ]
    )

    if occasion == "Other":
        custom_occasion = st.text_input(
            "Tell Oge where you're going"
        )
    else:
        custom_occasion = occasion

    st.write("### 💭 What kind of look do you want?")

    style_preference = st.selectbox(
        "Choose your preferred style",
        [
            "Chic",
            "Elegant",
            "Casual",
            "Classy",
            "Trendy",
            "Minimal",
            "Feminine",
            "Bold",
            "Modest",
            "Comfortable",
            "Surprise me"
        ]
    )

    if st.button("✨ Style it with Ògè"):

        st.divider()

        st.success(
            f"Here are 3 {style_preference.lower()} "
            f"looks for your {custom_occasion.lower()}."
        )

        st.write("## 👗 Look 1 — Polished")

        st.write(
            f"Style your uploaded piece with a clean, well-fitted "
            f"top in a neutral colour. Add simple jewellery, "
            f"a structured handbag and polished shoes. "
            f"This works especially well for {custom_occasion.lower()}."
        )

        st.write("## 👗 Look 2 — Elevated")

        st.write(
            f"Create a more elevated outfit by pairing your piece "
            f"with a contrasting top, refined accessories and "
            f"a statement shoe. Keep the accessories coordinated "
            f"for a balanced {style_preference.lower()} look."
        )

        st.write("## 👗 Look 3 — Effortless")

        st.write(
            f"For a more relaxed option, combine your piece with "
            f"a simple top, comfortable shoes and minimal accessories. "
            f"This gives you an effortless outfit suitable for "
            f"{custom_occasion.lower()}."
        )

        st.info(
            "✨ Oge will soon be able to identify your actual clothing "
            "item and create personalised outfit images."
        )
