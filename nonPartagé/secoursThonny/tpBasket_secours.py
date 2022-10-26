## ================= SECTION 0 : IMPORTATION DES EXTENSIONS (ne pas modifier) =======================
from vecteur import Vecteur                                                  #ne pas modifier
from modelisation import Modelisation                                        #ne pas modifier
import cv2                                                                   #ne pas modifier
import matplotlib.pyplot as plt                                              #ne pas modifier
modelisation = Modelisation()                                                #ne pas modifier
cv2.destroyAllWindows()                                                      #ne pas modifier

#===================SECTION 1 : POSITION INITIALE DU BALON (x, y) =========================
x  =  8           # Position initiale (en m) du ballon                         (A COMPLETER)
y  =   4.0          #                                                            (A COMPLETER)
OM = Vecteur(x,y) # vecteur position initial                                   ne pas modifier

#===================SECTION 2 : VITESSE INITIALE DU BALLON (vx, vy) =========================
vx =  -4.3   # vitesse initiale en m/s (composante suivant l'axe des x)     (A COMPLETER)
vy =   6   # vitesse initiale en m/s(composante suivant l'axe des x)      (A COMPLETER)
v = Vecteur(vx,vy) # Vecteur vitesse                                        Ne pas modifier

#===================SECTION 3 : BILAN DES FORCES EXERCEES SUR LE BALLON =========================
m = 0.600   #masse du ballon de basket en kg                                    (A COMPLETER) 
g = 9.81   #Intensité de pesanteur en N/kg                                      (A COMPLETER)

F_x = 0          # Force résultante en N (composante suivant l'axe des x)          (A COMPLETER)
F_y = -m*g       # Force résultante en N (composante suivant l'axe des x)       (A COMPLETER)
F   = Vecteur (F_x ,F_y ) # Vecteur force résultante                            (A COMPLETER) 

modelisation.show(OM,v,F)   #Affichage des résultats                  Ne pas modifier

#===================SECTION 4 : Sauvegarde des paramètres NE PAS MODIFIER =========================
OMi =OM  #sauvegarde du vecteur position initiale dans la variable "OMi"        Ne pas modifier                                
Fi = F   #sauvegarde du vecteur force résultante initiale dans la variable "Fi" Ne pas modifier
vi = v   #sauvegarde du vecteur vitesse initiale dans la variable "vi"          Ne pas modifier

#=====================SECTION A- CHARGEMENT DES PARAMETRES INITIAUX (NE PAS MODIFIER)================
OM = OMi                                                                                  #ne pas modifier
F  = Fi                                                                                   #ne pas modifier
v  = vi                                                                                   #ne pas modifier
modelisation = Modelisation()                                                             #ne pas modifier
modelisation.show(OM,v,F)                                                                 #ne pas modifier 

#=====================SECTION B- CALCUL DES POSITIONS ET VITESSES SUIVANTES GRACE A LA SECONDE LOI DE NEWTON

deltat = 40e-3  #durée (en seconde) entre 2 images successives                            (A COMPLETER)          

for i in range(38): #On répète pour les 38 images de la vidéos       #ne pas modifier
    v = v + deltat*F/m               # vitesse suivante = vitesse précédente + ......... # (A COMPLETER) 
    
    OM = OM + v*deltat               # position suivante = position précédente + ......... # (A COMPLETER)                                                   
    
    modelisation.show(OM,v,F) # Affichage des positions successives                    (ne pas modifier)

cv2.destroyAllWindows()                                                                   #ne pas modifier