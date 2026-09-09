import streamlit as st
from huggingface_hub import InferenceClient
import base64


# ---------------------------------------------------------
# HUGGING FACE CONNECTION
# ---------------------------------------------------------

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    provider="auto",
    api_key=HF_TOKEN
)


# ---------------------------------------------------------
# AI CLOTHING IDENTIFICATION
# ---------------------------------------------------------

def identify_clothing(image_file):

    image_bytes = image_file.getvalue()

    image_base64 = base64.b64encode(image_bytes).decode()

    response = client.chat.completions.create(
        model="Qwen/Qwen3.8-27B",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": """
You are Oge, an AI fashion assistant.

Look carefully at the uploaded clothing item.

Identify and describe:

1. Garment type
2. Main colour
3. Secondary colours if visible
4. Pattern or print
5. Silhouette
6. Approximate length
7. Fabric or material if reasonably visible
8. Neckline, sleeves, pleats, buttons, pockets,
   seams or other notable design details
9. Overall style of the garment

Be concise and factual.

Do not identify the person's body.
Do not make assumptions about the person's body.
Only describe what can reasonably be observed from the image.
"""
                    }
                ]
            }
        ],
        max_tokens=300

          )


    return response.choices[0].message.content


# ---------------------------------------------------------
# OGE APP
# ---------------------------------------------------------

st.title("Oge")

st.subheader("Your AI Fashion Assistant")

st.write("Snap what you have. See how to style it.")

st.divider()


# ---------------------------------------------------------
# UPLOAD CLOTHING
# ---------------------------------------------------------

st.write("### 📸 Upload what you want to style")

uploaded_file = st.file_uploader(
    "Take a photo or upload a photo of your clothing",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file:

    st.image(
        uploaded_file,
        caption="Your item",
        width="stretch"
    )

    st.divider()


    # -----------------------------------------------------
    # OCCASION
    # -----------------------------------------------------

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
            "Alumni Event",
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


    # -----------------------------------------------------
    # STYLE PREFERENCE
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # BODY / FIT PREFERENCE
    # -----------------------------------------------------

    st.write("### 👗 Tell Oge about your fit preference")

    body_preference = st.selectbox(
        "Choose an option",
        [
            "Petite",
            "Average height",
            "Tall",
            "Curvy",
            "Plus-size",
            "Straight / Rectangular",
            "Pear",
            "Apple",
            "Hourglass",
            "Inverted Triangle",
            "Prefer not to specify"
        ]
    )


    fit_preference = st.selectbox(
        "How do you prefer your clothes to fit?",
        [
            "Fitted",
            "Relaxed",
            "Oversized",
            "Structured",
            "Flowy",
            "Balanced mix"
        ]
    )


    # -----------------------------------------------------
    # FASHION RULES
    # -----------------------------------------------------

    st.write("### 📐 Oge's styling rules")

    st.caption(
        "Oge considers proportion, silhouette, colour balance, "
        "garment length, comfort and occasion when creating suggestions."
    )


    # -----------------------------------------------------
    # STYLE BUTTON
    # -----------------------------------------------------

    if st.button("✨ Style it with Oge"):

        # ---------------------------------------------
        # IDENTIFY CLOTHING
        # ---------------------------------------------

        with st.spinner(
            "Oge is looking at your clothing..."
        ):

            clothing_description = identify_clothing(
                uploaded_file
            )


        # ---------------------------------------------
        # SHOW IDENTIFICATION
        # ---------------------------------------------

        st.write(
            "### 🔍 Oge identified your item"
        )

        st.info(
            clothing_description
        )


        st.divider()


        # ---------------------------------------------
        # INTRODUCTION
        # ---------------------------------------------

        st.success(
            f"Here are 3 {style_preference.lower()} looks "
            f"for your {custom_occasion.lower()}."
        )


        # ---------------------------------------------
        # LOOK 1
        # ---------------------------------------------

        st.write(
            "## 👗 Look 1 — Polished"
        )

        st.write(
            f"Build the outfit around the uploaded garment. "
            f"Use complementary colours and a balanced silhouette. "
            f"Choose a {fit_preference.lower()} fit and coordinate "
            f"the footwear, bag and accessories for a polished "
            f"{style_preference.lower()} look suitable for "
            f"{custom_occasion.lower()}."
        )

        st.write(
            "**Styling rule:** Balance proportion and avoid "
            "letting multiple statement pieces compete."
        )


        # ---------------------------------------------
        # LOOK 2
        # ---------------------------------------------

        st.write(
            "## 👗 Look 2 — Elevated"
        )

        st.write(
            f"Create a more elevated combination using the uploaded "
            f"garment as the foundation. Add a complementary top, "
            f"refined footwear, a coordinated bag and carefully "
            f"selected accessories. Maintain your preferred "
            f"{fit_preference.lower()} fit while keeping the "
            f"overall proportions balanced."
        )

        st.write(
            "**Styling rule:** Use one main focal point and keep "
            "the remaining pieces supportive."
        )


        # ---------------------------------------------
        # LOOK 3
        # ---------------------------------------------

        st.write(
            "## 👗 Look 3 — Effortless"
        )

        st.write(
            f"Create an easier everyday combination around the "
            f"uploaded garment. Use a simple complementary top, "
            f"practical footwear and minimal accessories. Keep "
            f"the proportions comfortable and appropriate for "
            f"{custom_occasion.lower()}."
        )

        st.write(
            "**Styling rule:** Comfort, proportion and colour "
            "coordination should work together."
        )


        # ---------------------------------------------
        # CURRENT DEVELOPMENT STATUS
        # ---------------------------------------------

        st.divider()

        st.info(
            "✨ Oge has analysed your clothing photo. "
            "The next stage is to use the identified garment, "
            "occasion and fit preferences to generate genuinely "
            "personalised outfit combinations."
        )
