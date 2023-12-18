import streamlit as st

class MultiApp:
    """
    Framework for combining multiple streamlit applications.
    """
    def __init__(self):
        self.apps = []
    def add_app(self, title, func):
        """
        Adds a new application.
        Parameters
        ----------
        title: str
            The title of the app which will be displayed in the dropdown menu
        func:
            The python function to render this app.
        """
        self.apps.append({
            "title": title,
            "function": func
        })
    def run(self):
        # app = st.sidebar.selectbox(
        #     'Navigation',
        #     self.apps,
        #     format_func=lambda app: app['title'])
        app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title']
        )