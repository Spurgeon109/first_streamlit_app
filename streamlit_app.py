import streamlit

streamlit.title("My parents New Health Dinner")


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index))

streamlit.dataframe(my_fruit_list)
