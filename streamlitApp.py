import streamlit as st
import pickle

model=pickle.load(open('model/model_rf.pkl','rb'))

# st.title("New app in streamlit")
# st.header("This is header in the page")
# st.subheader("this is subheader")
# st.write("hello")
# st.badge("thalle")
# st.text("Enter your name: ")
# st.radio("Select your option:",options=['Option1','Option2','Option3'])

# import pandas as pd
# data=pd.DataFrame({'city': ['kochi','chennai','banglore']})       
# st.dataframe(data)
# st.slider("Select your age:",10,16)

# st.selectbox('Drop down menu:',options=['table','chair','tree'])

st.header("Iris Species Prediction")

predictions={0:"Setosa",
             1:"Versicolor",
             2:"Virginica"}

species_images = {
    "Setosa": "images/setosa.jpg",
    "Versicolor": "images/versicolor.jpg",
    "Virginica": "images/virginica.jpg"
}

with st.form("iris_app_form"):
    pl=st.text_input("Enter Petal length:")
    pw=st.text_input("Enter Petal width:")
    sl=st.text_input("Enter Sepal length:")
    sw=st.text_input("Enter Sepal width:")
    submitted=st.form_submit_button("Predict")

if submitted:
    prediction= model.predict([[sl,sw,pl,pw]])
    predicted_species=predictions.get(prediction[0],'Unknown')
    st.success(f"Predicted Species: {predicted_species}")

    image_path = species_images.get(predicted_species)
    if image_path:
        st.image(image_path, caption=predicted_species, use_container_width=True)
    else:
        st.warning("No image available for this species.")