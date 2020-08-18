#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import re
import time
import reg_titanic
from reg_titanic import Surviving
external_stylesheets = ['https://github.com/plotly/dash-app-stylesheets/blob/master/dash-uber-ride-demo.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([html.H1(children="Please input your name age sex and class(1,2,3)", 
                               id = "teext",
                               style= {'vertical-align': 'middle', 'width': '49%', 'display': 'inline-block'}),
                       dcc.Input(
                        id="input",
                        type= "text"
                          ),
#                        html.Button(id='submit-button', 
#                                    type='submit', 
#                                    children='Submit'),
                       html.H1(id="result")
                      ])

@app.callback(Output('result', 'children'),
                  [Input('input', 'value')]
                  )
def surv(input_value):
    pattern_num = r"\d+"
    pattern_name = r"[A-Z][a-z]+"
    pattern_sex = r"male|female"
    name = re.findall(pattern_name, str(input_value))[0]
    age = int(re.findall(pattern_num, str(input_value))[0])
    sex= re.findall(pattern_sex, str(input_value))[0]
    class_p = int(re.findall(pattern_num, str(input_value))[1])
    time.sleep(4)
    print(name,sex,age,class_p)
    survivor=Surviving(age, sex, int(class_p))
    will_survive= int(survivor.will_survive())
    print(will_survive)
    if will_survive==1:
        return f"Dear {name}, according to our estimations you will probably survive in titanic"
    else:
        return f"Dear {name}, according to our estimations you will probably not survive in titanic :((((((("

if __name__ == '__main__':
    app.run_server(debug=False)

