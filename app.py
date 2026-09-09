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
        max_tokens=500
    )

    return response.choices[0].message.content


# ---------------------------------------------------------
# AI OUTFIT STYLING
# ---------------------------------------------------------

def generate_outfits(
    clothing_description,
    occasion,
    style_preference,
    body_preference,
    fit_preference
):

    prompt = f"""
You are Oge, an expert AI fashion stylist.

The user uploaded a clothing item and Oge identified it as:

{clothing_description}

The user's occasion is:
{occasion}

The user's preferred style is:
{style_preference}

The user's fit/body preference is:
{body_preference}

The user's preferred clothing fit is:
{fit_preference}

Create EXACTLY 3 complete outfit recommendations using the identified
clothing item as the main piece.

The outfits must be specific and practical.

For EACH look include:

LOOK 1 — [creative name]

CLOTHING:
- Main item: [use the uploaded item]
- Top: [specific item and colour]
- Other clothing: [specific item and colour]

SHOES:
- [specific shoe and colour]

BAG:
- [specific bag and colour]

ACCESSORIES:
- [specific accessories]

WHY IT WORKS:
[2–3 sentences explaining the colour coordination,
proportion, silhouette and suitability for the occasion.]

Then create LOOK 2 and LOOK 3 in the same format.

IMPORTANT:
- Use the actual uploaded clothing item.
- Do not give generic advice.
- Do not say "add a complementary top."
- Name actual clothing pieces and colours.
- Make all three outfits different.
- Consider the occasion and preferred style.
- Consider proportion and garment length.
- Do not make negative comments about the user's body.
- Do not assume body measurements.
- Keep the recommendations realistic and wearable.

Return ONLY the three outfit recommendations.
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen3.8-27B",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content

    prompt = f"""
You are Oge, an AI fashion stylist.

The clothing item identified from the user's photo is:

{clothing_description}

The user is going to:
{occasion}

Preferred style:
{style_preference}

Fit/body preference:
{body_preference}

Preferred clothing fit:
{fit_preference}

Create exactly 3 specific and complete outfit recommendations
using the uploaded clothing item as the main piece.

Each outfit must include:

- The uploaded item
- Other clothing pieces
- Specific colours
- Shoes
- Bag
- Accessories

Make the three looks clearly different.

Consider:

- colour coordination
- proportion
- silhouette
- garment length
- occasion
- fit preference
- practicality
- overall styling

Do not give generic advice.

Do not say things such as:
"add a complementary top"
or
"choose suitable shoes."

Instead, name the actual clothing items and colours.

For each look provide:

LOOK 1 — [short name]

OUTFIT:
- [specific clothing item and colour]
- [specific clothing item and colour]
- [shoes]
- [bag]
- [accessories]

WHY IT WORKS:
[Brief explanation]

LOOK 2 — [short name]

OUTFIT:
- [specific clothing item and colour]
- [specific clothing item and colour]
- [shoes]
- [bag]
- [accessories]

WHY IT WORKS:
[Brief explanation]

LOOK 3 — [short name]

OUTFIT:
- [specific clothing item and colour]
- [specific clothing item and colour]
- [shoes]
- [bag]
- [accessories]

WHY IT WORKS:
[Brief explanation]

Do not discuss the user's body negatively.
Do not make assumptions about measurements.
Keep the recommendations practical and stylish.
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen3.8-27B",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=700
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
        # GENERATE OUTFITS
        # ---------------------------------------------

        with st.spinner(
            "Oge is creating your outfits..."
        ):

            outfit_recommendations = generate_outfits(
                clothing_description,
                custom_occasion,
                style_preference,
                body_preference,
                fit_preference
            )


        st.success(
            f"Here are 3 {style_preference.lower()} looks "
            f"for your {custom_occasion.lower()}."
        )


        st.write(
            "## 👗 Oge's outfit recommendations"
        )

        st.markdown(
            outfit_recommendations
        )


        # ---------------------------------------------
        # CURRENT DEVELOPMENT STATUS
        # ---------------------------------------------

        st.divider()

        st.info(
            "✨ Oge has analysed your clothing photo and "
            "created personalised outfit recommendations. "
            "The next stage is visual outfit generation."
        )
