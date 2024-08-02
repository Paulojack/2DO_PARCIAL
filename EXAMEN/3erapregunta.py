import cv2
# Cargar la imagen 
imagen = cv2.imread('imagen1.png')
if imagen is None:
    print("Error: La imagen no se pudo cargar.")
    exit()
# Redimensionar la imagen a 300x300 píxeles
dimensiones = (300, 300)
imagen_redimensionada = cv2.resize(imagen, dimensiones)
# Mostrar la imagen redimensionada
cv2.imshow('Imagen Redimensionada', imagen_redimensionada)
# Guardar la imagen redimensionada
cv2.imwrite('REDIMENSIONADA.jpg', imagen_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
