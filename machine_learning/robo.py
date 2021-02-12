# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:45:31 2021

@author: andre
"""
#importamos las librerias
import nltk
#import numpy as np
import random
import string
#Esto se usará para encontrar la similitud entre las palabras ingresadas por el usuario y las palabras en el corpus
#convertir una colección de documentos en bruto en una matriz de características TF-IDF.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#cargar el archibo chatbot.txt
f=open('chatbot.txt','r',errors = 'ignore')
#se lee
raw=f.read()
raw=raw.lower()# convierte a minúsculas
#descargar paquetes de nltk
nltk.download('punkt') # fientrenado para el ingles
nltk.download('wordnet') # first-time use only

sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words
#Ahora definiremos una función llamada LemTokens que tomará como entrada los tokens y devolverá tokens normalizados.
lemmer = nltk.stem.WordNetLemmatizer()
#Ahora definiremos una función llamada LemTokens que tomará como entrada los tokens y devolverá tokens normalizados
#WordNet es un diccionario de inglés de orientación semántica incluido en NLTK.
def LemTokens(tokens):
 return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
 return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
#definiremos una función para un saludo a través el bot, es decir, si la entrada de un usuario es un saludo, el bot devolverá una respuesta de saludo
GREETING_INPUTS = ("hola", "como estas", "bien", "que","no",)
GREETING_RESPONSES = ["hola","como estas","bien", "animo","que",]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
#Definimos una respuesta de función que busca la expresión del usuario para una o más palabras clave conocidas y devuelve una de las varias respuestas posibles.         
def response(user_response):
 robo_response=''
 sent_tokens.append(user_response)
 TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
 tfidf = TfidfVec.fit_transform(sent_tokens)
 vals = cosine_similarity(tfidf[-1], tfidf)
 idx=vals.argsort()[0][-2]
 flat = vals.flatten()
 flat.sort()
 req_tfidf = flat[-2]
 if(req_tfidf==0):
  robo_response=robo_response+"no comprendo lo que me quieres decir"
  return robo_response
 else:
  robo_response = robo_response+sent_tokens[idx]
  return robo_response
flag=True
print("ROBO: Mi nombre es Robo. te saludare y preguntare. si desea salir copie gracias")
#alimentaremos las líneas que queremos que diga nuestro robot al iniciar y finalizar una conversación, según la información del usuario
while(flag==True):
 user_response = input()
 user_response=user_response.lower()
 if(user_response!='bye'):
  if(user_response=='gracias' or user_response=='chao' ):
   flag=False
   print("ROBO: con gusto")
  else:
   if(greeting(user_response)!=None):
    print("ROBO: "+greeting(user_response))
   else:
    print("ROBO: ",end="")
    print(response(user_response))
    sent_tokens.remove(user_response)
else:
 flag=False
 print("ROBO: Bye! ")