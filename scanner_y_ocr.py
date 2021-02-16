
#importa los paquetes OpenCV, numpy y pytesseract que usaremos
#para extraer el texto de la imagen.
import cv2
import numpy as np 
import pytesseract

#ruta donde esta ubicado tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#ordenan las 4 vertices del documento 
def ordenar_puntos(puntos):
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    print('n_puntos=',n_puntos)
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])
    print('y_order=',y_order)
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])
    print('x1_order=',x1_order)
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
    #print('x2_order=',x2_order)
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

#leer imagen de entrada 
image = cv2.imread('img_00.jpeg')
#transformar la imagen de entrada en escalas de grises 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detectar bordes y engrosar lineas
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)

# encontramos los contornos externos
cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

	#deteccion de figuras geometricas
for c in cnts:
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    print('approx=',approx)
    if len(approx)==4:
        cv2.drawContours(image, [approx], 0, (0,255,255),2)
        puntos = ordenar_puntos(approx)
        #print('puntos=',puntos)

        #Dibujamos una circunferencia cada una de las coordenadas correspondientes
        #a los vértices del documento que están almacenadas en puntos
        cv2.circle(image, tuple(puntos[0]), 7, (255,0,0), 2)
        cv2.circle(image, tuple(puntos[1]), 7, (0,255,0), 2)
        cv2.circle(image, tuple(puntos[2]), 7, (0,0,255), 2)
        cv2.circle(image, tuple(puntos[3]), 7, (255,255,0), 2)

        #puntos imagen de entrada y destino
        pts1 = np.float32(puntos)
        pts2 = np.float32([[0,0],[270,0],[0,310],[270,310]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(gray,M,(270,310))
        cv2.imshow('dst', dst)

        #se aplica el OCR
        texto = pytesseract.image_to_string(dst, lang='spa')
        print('texto: ', texto)

#visualizacion de imagen y lo que estamos obteniendo en canny
cv2.imshow('image',image)
#cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
