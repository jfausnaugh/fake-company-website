import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The Best Company")

# fake test for "description" of company
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pharetra dictum ligula, 
vestibulum finibus augue finibus vel. Nulla facilisi. Curabitur sagittis condimentum mi, 
et tempus quam aliquet in. Ut dictum luctus facilisis. Aenean posuere non quam non dignissim.
 Sed eget tempus orci. Aliquam condimentum consectetur nisi et iaculis. Quisque commodo,
  leo in faucibus hendrerit, mi dolor pretium odio, ut ultricies nisl dui ut risus.
   Maecenas sed mauris eros. Maecenas sit amet risus sit amet dolor vulputate mattis 
   id ut odio. Mauris et tellus at eros luctus ultricies semper in turpis."""

st.write(content)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

# reads the data from the csv file in order to pull information for the columns
df = pandas.read_csv("data_company.csv")

with col1:
    # pulls the first 4 peoples information for the first column
    for index, row in df[:4].iterrows():
        st.image("company_images/" + row["image"])
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])

with col2:
    # pulls information the middle 4 peoples information for the middle column
    for index, row in df[4:8].iterrows():
        st.image("company_images/" + row["image"])
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])


with col3:
    # pulls information for the last 4 people for the last column
    for index, row in df[8:].iterrows():
        st.image("company_images/" + row["image"])
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])

