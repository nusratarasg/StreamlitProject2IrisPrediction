import streamlit as st

import pickle
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

# method
def show_predict_page():

    st.title('Iris Classifier')

    st.subheader("This app uses 4 inputs to predict the species of iris "
    
             )
    rf_pickle = open('random_forest_iris.pickle', 'rb')

    map_pickle = open('output_iris.pickle', 'rb')

    rfc = pickle.load(rf_pickle)

    unique_iris_mapping = pickle.load(map_pickle)

    #st.write(rfc)
    #st.write('Using:', rfc)
    st.write(f"#####   Using:  {rfc} ")
    #st.write(unique_penguin_mapping)

    rf_pickle.close()

    map_pickle.close()

    #island = st.selectbox('Penguin Island', options=[
        #'Biscoe', 'Dream', 'Torgerson'])

    #sex = st.selectbox('Sex', options=['Female', 'Male'])

    sepal_length = st.number_input('Sepal Length', min_value=0.0)

    sepal_width = st.number_input('Sepal Width', min_value=0.0)

    petal_length = st.number_input('Petal Length', min_value=0.0)

    petal_width = st.number_input('Petal Width', min_value=0.0)
    #island_biscoe, island_dream, island_torgerson = 0, 0, 0



    st.write('User inputs are {}'.format(
        [ sepal_length,
         sepal_width, petal_length, petal_width]))

    new_prediction = rfc.predict([[sepal_length, sepal_width, petal_length,
                                   petal_width]])

    prediction_species = unique_iris_mapping[new_prediction][0]

    st.write('Prediction: Iris is of the {} species'.format(prediction_species))



