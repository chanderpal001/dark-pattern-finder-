from flask import Flask, request
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

with open('model.pkl','rb') as f:
    model=pickle.load(f)
    
@app.route('/')
def hello_world():
    return 'Hello,world!.'


@app.route('/receive-url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data.get('url')
    print(url)
    current = webdriver.Chrome()  
    current.get(url)
    html_data=current.page_source
    current.quit()
    soup = BeautifulSoup(html_data, 'html.parser')
    text_data = soup.get_text()
    text_data = text_data.replace("\n","")
    for text in text_data.split('.'):
        predictions = model.predict([text])
        if predictions[0] >= 0.50000:
            print("Detected")
        else :
            print("Not Detected")
    
    

if __name__ == '__main__':
    app.run(port=4000)






