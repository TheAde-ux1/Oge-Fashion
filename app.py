import streamlit as st
import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ.get("HF_TOKEN")
client = InferenceClient(
    provider="auto",
    api_key=HF_TOKEN
)

def identify_clothing(image_file):

    image_bytes = image_file.getvalue()

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-VL-7B-Instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{__import__('base64').b64encode(image_bytes).decode()}"
                        }
                    },
                    {
                        "type": "text",
                        "text": """Identify the clothing item in this image.

Describe:
- garment type
- colour
- pattern
- silhouette
- apparent length
- fabric or material if reasonably visible
- notable design details

Keep the description concise and factual.
Do not identify the person's body or make assumptions about their body."""
                    }
                ]
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content

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

    st.write("### 📐 Oge's styling rules")

    st.caption(
        "Oge considers proportion, silhouette, colour balance, "
        "garment length, comfort and occasion when creating suggestions."
    )

    if st.button("✨ Style it with Oge"):

        st.divider()

        st.success(
            f"Here are 3 {style_preference.lower()} looks "
            f"for your {custom_occasion.lower()}."
        )

        st.write("## 👗 Look 1 — Polished")

        st.write(
            f"Build the outfit around your uploaded piece using "
            f"a balanced silhouette and colours that complement it. "
            f"Choose a {fit_preference.lower()} fit and keep the "
            f"accessories coordinated for a polished "
            f"{style_preference.lower()} look suitable for "
            f"{custom_occasion.lower()}."
        )

        st.write(
            "**Styling rule:** Balance proportion and avoid "
            "letting multiple statement pieces compete."
        )

        st.write("## 👗 Look 2 — Elevated")

        st.write(
            f"Create a more elevated combination with a complementary "
            f"top, refined footwear, a structured or coordinated bag "
            f"and carefully selected accessories. The outfit should "
            f"work with your preferred {fit_preference.lower()} fit "
            f"while maintaining visual balance."
        )

        st.write(
            "**Styling rule:** Use one main focal point and keep "
            "the remaining pieces supportive."
        )

        st.write("## 👗 Look 3 — Effortless")

        st.write(
            f"Create an easier combination using your uploaded piece "
            f"with a simple complementary top, practical footwear "
            f"and minimal accessories. Keep the proportions comfortable "
            f"and appropriate for {custom_occasion.lower()}."
        )

        st.write(
            "**Styling rule:** Comfort, proportion and colour "
            "coordination should work together."
        )

        st.divider()

        st.info(
            "✨ Oge will soon be able to identify the actual clothing "
            "item in your photo and use that information to personalise "
            "each recommendation."
        )
