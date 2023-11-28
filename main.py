import streamlit as st
import pickle
import numpy as np
from PIL import Image

rfc = pickle.load(open('rfc.pkl', 'rb'))

# Creating web app
st.title('Forest Cover Type Prediction')
image = Image.open('img.png')
st.image(image, caption='myimage', use_column_width=True)
user_input = st.text_input('Input Features')

if user_input:
    user_input = user_input.split(',')
    features = np.array([user_input], dtype=np.float64)
    output = rfc.predict(features).reshape(1, -1)

    # Create the cover type dictionary
    cover_type_dict = {
        1: {"name": "Spruce/Fir", "image": "img1.jpg"},
        2: {"name": "Lodgepole Pine", "image": "img2.jpeg"},
        3: {"name": "Ponderosa Pine", "image": "img3.jpg"},
        4: {"name": "Cottonwood/Willow", "image": "img4.jpg"},
        5: {"name": "Aspen", "image": "img5.jpg"},
        6: {"name": "Douglas-fir", "image": "img6.jpeg"},
        7: {"name": "Krummholz", "image": "img7.jpeg"}
    }

    # Convert the output to integer
    predicted_cover_type = int(output[0])
    cover_type_info = cover_type_dict.get(predicted_cover_type)

    if cover_type_info is not None:
        cover_type_name = cover_type_info["name"]
        cover_type_image_path = cover_type_info["image"]

        # Display the cover type card
        col1, col2 = st.columns([2, 3])

        with col1:
            st.write("Predicted Cover Type:")
            st.write(f"<h1 style='font-size: 40px; font-weight: bold;'>{cover_type_name}</h1>", unsafe_allow_html=True)

        with col2:
            cover_type_image = Image.open(cover_type_image_path)
            st.image(cover_type_image, caption=cover_type_name, use_column_width=True)
    else:
        st.write("Unable to make a prediction")
