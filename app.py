import streamlit as st
from multiapp import MultiApp
from views import user_engagement, user_expeirence, user_satisfaction  # import your app modules here

st.set_page_config(page_title='Telecom Data Analysis')

app = MultiApp()
st.title('User Page')
st.markdown('Welcome to the User Page')

app.add_app("User-Engagement", user_engagement.app)
#app.add_app("User-Experience", user_experience.app)
#app.add_app("User-Satisfaction", user_satisfaction.app)

# Get the selected app title
selected_app_title = st.sidebar.selectbox(
    'Navigation',
    [app['title'] for app in app.apps]
)

# Find the selected app by title
selected_app = next(app['function'] for app in app.apps if app['title'] == selected_app_title)

# Run the selected app
selected_app()
