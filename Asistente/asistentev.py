import PySimpleGUI as sg 
from nltk.chat.util import Chat, reflections
import webbrowser 
import pandas as pd 


data=pd.read_excel('pares.xls') 

pares1=[] 

for i in range(len(data)):
    sub_pares=[] 
    ans=data.iloc[i][0] 
    resp=[data.iloc[i][1]] 
    sub_pares.append(ans)   
    sub_pares.append(resp)     
    pares1.append(sub_pares)   
    
# Se crea la interfaz grafica como un layout
layout = [  [sg.Text('Hola ¡¡¡ Soy el asistente en Fundamentos de Programacion y Machine Learning')],
            [sg.Output(size=(80,10), key='-OUTPUT-')],
            [sg.In(text_color='black')],
            [sg.Button('Pregunta'), sg.Button('Borrar'), sg.Button('Salir del Chat')]  ]

window = sg.Window('ASISTENTE VIRTUAL', layout) 


while True:
    event, values = window.read()
    if event =='Salir del Chat':
        break 
    if event =='Pregunta':
        chat= Chat(pares1) 
        respuesta=chat.respond(values[0]) 

        if respuesta: 
            if respuesta[0:5]!='https':          
                print(' ')  
                print('Usuario: '+values[0]) 
                print('Asistente: '+respuesta if str(respuesta)!='None' else 'Disculpa,No tengo respuesta (intenta de nuevo)')
            else:
                print(' ')
                print('Usuario: '+values[0]) 
                print('Asistente:  Te recomendamos esa web (espera que se abra...)')
                webbrowser.open(respuesta)
        else:
            print('Disculpa,No tengo respuesta (intenta de nuevo)') 
            
    
    if event == 'Borrar':
        window['-OUTPUT-'].update('')
        

window.close()
        
        



