# Alex_Bot
So far, the bot can have a simple conversation with a human, solve math problems, make some jokes, say what time it is, ask for an introduction when someone gets into the channel, and understand some commands


## How Alex_Bot works
The Core library used to make Alex being able to have a conversation is "Chatterbot" which is a python library that uses a selection of machine learning algorithms to produce different types of responses making use of different NLP libraries like NLTK, spaCy, etc.


In this case Alex starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As Alex receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase.


The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then chooses a response from the selection of known responses to that statement.

Process Flow Diagram: 

![Screenshot 2022-08-08 031225](https://user-images.githubusercontent.com/95022282/183484355-a37e2ede-79b5-4044-a440-c5679a2e66ea.png)




How the logic adapters select a response: 


![Screenshot 2022-08-08 053744](https://user-images.githubusercontent.com/95022282/183484556-5cb8adbe-7e7e-4ce5-a5ef-418f9034bb45.png)



To work with this app you need:

Python Virtual Environment

Change the tokens

You can use VScode or any IDE

And install the following libraries:

astroid==2.11.7
chatbot==1.5.2b0
ChatterBot==1.0.0
chatterbot-corpus==1.2.0
click==8.1.3
colorama==0.4.5
dill==0.3.5.1
isort==5.10.1
joblib==1.1.0
lazy-object-proxy==1.7.1
mathparse==0.1.2
mccabe==0.7.0
nltk==3.7
Pint==0.19.2
platformdirs==2.5.2
pycryptodome==3.15.0
pylint==2.14.5
pymongo==3.12.3
pyt==1.0.5
python-dateutil==2.7.5
python-dotenv==0.20.0
pytz==2022.1
PyYAML==3.13
regex==2022.7.25
six==1.16.0
slack-bolt==1.14.2
slack-sdk==3.18.0
SQLAlchemy==1.2.19
tomli==2.0.1
tomlkit==0.11.1
tqdm==4.64.0
typing_extensions==4.3.0
wrapt==1.14.1


## Please see the attached link for a deep explanation of the project

https://express.adobe.com/page/4jptPA95vwemf/



Created by Tian Hong Zhu Zhou 

Apache License
