from bs4 import BeautifulSoup
import requests as re
#import feature_extraction as fee
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pickle
model= pickle.load(open('model.pkl', 'rb'))

from flask import Flask,request,render_template
app= Flask (__name__)

@app.route("/")
def check():
    return render_template('check.html')

@app.route('/checkbutton', methods=['POST', 'GET'])
def checkbutton():
    geturl = request.form['url']
    final=[np.array(geturl)]
    
    prediction = model.predict(final)
    print(prediction)
    output = prediction[0]
    if (output == 1):
        pred = "Your are safe!!  This is a Legitimate Website."
    else:
        pred = "Your are on the wrong site. Be cautious!"
    return render_template('check.html', url_path = geturl, url=pred)



"""
url = st.text_input('Enter the URL')
# check the url is valid or not
if ('Check!'):#this code is for streamlit deployment
        try:
            response = re.get(url, verify=False, timeout=4)
            if response.status_code != 200:
                print(". HTTP connection was not successful for the URL: ", url)
            else:
                url = BeautifulSoup(response.content, "html.parser")
                #vector = [fee.create_vector(soup)]  # it should be 2d array, so I added []
                result = model.predict(url)
                if result[0] == 0:
                    st.success("This web page seems a legitimate!")
                    st.balloons()
                else:
                    st.warning("Attention! This web page is a potential PHISHING!")
                    st.snow()

        except re.exceptions.RequestException as e:
            print("--> ", e)"""

app.run(debug=True)