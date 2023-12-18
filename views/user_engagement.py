import streamlit as st
from PIL import Image
import os
import sys


def app():
    
    rpath = os.path.abspath('..')
    if rpath not in sys.path:
        sys.path.insert(0,rpath)

    st.title('User Engagement App')
    st.markdown('This is the User Engagement App.')

    # Load images
    st.write('These are the users with the highest engagement scores')
    image1 = Image.open("images/high_user_engagement.png")  # Replace with the actual path to your image
    st.image(image1, caption='Image 1',use_column_width=True)

    st.write("This is what the user when it's diveded ")

    image2 = Image.open("images/engagement_cluster.png")  # Replace with the actual path to your image
    st.image(image2, caption='Image 2',use_column_width=True)

    st.write("This is the division among cluster when they are divided")

    image3 = Image.open("images/engagement_cluster_dist.png")

    st.image(image3, caption='Image 3',use_column_width=True)


if __name__ == "__main__":
    app()
