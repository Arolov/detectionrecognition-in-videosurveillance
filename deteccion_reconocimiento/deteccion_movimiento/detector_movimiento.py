import cv2
class DetectorMovimiento(object):
    def __init__(self,sustractor=None, metodo='MOG2'):
        if sustractor:
            self.sustractor = sustractor
        elif metodo:
            self.sustractor = self.crear_sustractor(metodo)
    def crear_sustractor(self, metodo="GSOC"):
        sustractor = cv2.bgsegm.createBackgroundSubtractorGSOC()
        if metodo == 'CNT':
            sustractor = cv2.bgsegm.createBackgroundSubtractorCNT()
        elif metodo == 'LSBP':
            sustractor = cv2.bgsegm.createBackgroundSubtractorLSBP()
        elif metodo == 'MOG2':
            sustractor = cv2.createBackgroundSubtractorMOG2()
        return sustractor
        
    def detectar(self, image):
        self.imagen = image
        mascaraPrimerPlano = self.sustractor.apply(image)
        contornos = mascaraPrimerPlano.copy()
        im2, contornos, h = cv2.findContours(contornos, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        puntosRecta = [cv2.boundingRect(contorno) for contorno in contornos if cv2.contourArea(contorno) >= 500]

        cuadros = [image[y:y+h,x:x+w] for (x,y,w,h) in puntosRecta]
        return (puntosRecta, cuadros)
