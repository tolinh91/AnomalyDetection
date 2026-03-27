import numpy as np
import sys
from numpy import loadtxt
import json
import time
from collections import Counter, OrderedDict
import glob

def orderInt(x):
    return int(x)

def predict(data):
    """ Predictor for field61 from model/5eb3f89babfdeb2da3001641

        Pruebas y experimentos para la conferencia 2020. Se probará con distinto número de entradas, distinta limpieza de muestras de usuario, etc.
    """
    if (data.get('field30') is None):
        return u'0'
    if (data['field30'] > -0.23259):
        if (data.get('field6') is None):
            return u'1'
        if (data['field6'] > -0.12032):
            if (data.get('field55') is None):
                return u'1'
            if (data['field55'] > -0.38427):
                if (data.get('field26') is None):
                    return u'1'
                if (data['field26'] > -0.11782):
                    if (data.get('field51') is None):
                        return u'1'
                    if (data['field51'] > 4.04627):
                        if (data.get('field19') is None):
                            return u'1'
                        if (data['field19'] > 0.56164):
                            if (data.get('field50') is None):
                                return u'0'
                            if (data['field50'] > 2.88598):
                                return u'1'
                            if (data['field50'] <= 2.88598):
                                return u'0'
                        if (data['field19'] <= 0.56164):
                            return u'1'
                    if (data['field51'] <= 4.04627):
                        if (data.get('field43') is None):
                            return u'1'
                        if (data['field43'] > 5.44065):
                            if (data.get('field50') is None):
                                return u'1'
                            if (data['field50'] > 0.0486):
                                return u'1'
                            if (data['field50'] <= 0.0486):
                                return u'0'
                        if (data['field43'] <= 5.44065):
                            return u'1'
                if (data['field26'] <= -0.11782):
                    if (data.get('field56') is None):
                        return u'1'
                    if (data['field56'] > 1.91966):
                        if (data.get('field29') is None):
                            return u'1'
                        if (data['field29'] > -0.12306):
                            return u'1'
                        if (data['field29'] <= -0.12306):
                            if (data.get('field53') is None):
                                return u'0'
                            if (data['field53'] > 1.30545):
                                return u'0'
                            if (data['field53'] <= 1.30545):
                                return u'1'
                    if (data['field56'] <= 1.91966):
                        if (data.get('field7') is None):
                            return u'1'
                        if (data['field7'] > 2.81843):
                            if (data.get('field38') is None):
                                return u'1'
                            if (data['field38'] > -0.36407):
                                return u'1'
                            if (data['field38'] <= -0.36407):
                                return u'0'
                        if (data['field7'] <= 2.81843):
                            return u'1'
            if (data['field55'] <= -0.38427):
                if (data.get('field3') is None):
                    return u'1'
                if (data['field3'] > -0.09102):
                    return u'1'
                if (data['field3'] <= -0.09102):
                    if (data.get('field9') is None):
                        return u'1'
                    if (data['field9'] > -0.22833):
                        return u'1'
                    if (data['field9'] <= -0.22833):
                        if (data.get('field18') is None):
                            return u'0'
                        if (data['field18'] > -0.2543):
                            return u'1'
                        if (data['field18'] <= -0.2543):
                            return u'0'
        if (data['field6'] <= -0.12032):
            if (data.get('field10') is None):
                return u'1'
            if (data['field10'] > -0.18015):
                if (data.get('field57') is None):
                    return u'1'
                if (data['field57'] > -0.3998):
                    if (data['field6'] > -0.25969):
                        return u'1'
                    if (data['field6'] <= -0.25969):
                        if (data.get('field33') is None):
                            return u'1'
                        if (data['field33'] > -0.29484):
                            return u'1'
                        if (data['field33'] <= -0.29484):
                            if (data.get('field1') is None):
                                return u'1'
                            if (data['field1'] > -0.24132):
                                return u'1'
                            if (data['field1'] <= -0.24132):
                                if (data.get('field4') is None):
                                    return u'0'
                                if (data['field4'] > -0.23302):
                                    return u'1'
                                if (data['field4'] <= -0.23302):
                                    return u'0'
                if (data['field57'] <= -0.3998):
                    if (data.get('field36') is None):
                        return u'1'
                    if (data['field36'] > -0.29578):
                        if (data.get('field46') is None):
                            return u'1'
                        if (data['field46'] > 5.698):
                            return u'0'
                        if (data['field46'] <= 5.698):
                            return u'1'
                    if (data['field36'] <= -0.29578):
                        if (data.get('field2') is None):
                            return u'0'
                        if (data['field2'] > -0.23901):
                            if (data.get('field13') is None):
                                return u'1'
                            if (data['field13'] > -0.25337):
                                return u'1'
                            if (data['field13'] <= -0.25337):
                                if (data.get('field38') is None):
                                    return u'0'
                                if (data['field38'] > -0.24118):
                                    return u'1'
                                if (data['field38'] <= -0.24118):
                                    return u'0'
                        if (data['field2'] <= -0.23901):
                            return u'0'
            if (data['field10'] <= -0.18015):
                if (data.get('field1') is None):
                    return u'0'
                if (data['field1'] > -0.22597):
                    if (data.get('field25') is None):
                        return u'1'
                    if (data['field25'] > -0.34201):
                        if (data.get('field50') is None):
                            return u'1'
                        if (data['field50'] > 3.37719):
                            return u'0'
                        if (data['field50'] <= 3.37719):
                            return u'1'
                    if (data['field25'] <= -0.34201):
                        if (data.get('field39') is None):
                            return u'1'
                        if (data['field39'] > -0.36566):
                            return u'1'
                        if (data['field39'] <= -0.36566):
                            return u'0'
                if (data['field1'] <= -0.22597):
                    if (data.get('field20') is None):
                        return u'0'
                    if (data['field20'] > -0.24597):
                        if (data['field10'] > -0.24858):
                            if (data.get('field38') is None):
                                return u'1'
                            if (data['field38'] > -0.34208):
                                return u'1'
                            if (data['field38'] <= -0.34208):
                                return u'0'
                        if (data['field10'] <= -0.24858):
                            if (data.get('field11') is None):
                                return u'0'
                            if (data['field11'] > 0.69263):
                                return u'1'
                            if (data['field11'] <= 0.69263):
                                return u'0'
                    if (data['field20'] <= -0.24597):
                        if (data.get('field2') is None):
                            return u'0'
                        if (data['field2'] > -0.24362):
                            if (data.get('field36') is None):
                                return u'0'
                            if (data['field36'] > -0.06735):
                                if (data.get('field50') is None):
                                    return u'1'
                                if (data['field50'] > -0.06774):
                                    return u'1'
                                if (data['field50'] <= -0.06774):
                                    return u'0'
                            if (data['field36'] <= -0.06735):
                                return u'0'
                        if (data['field2'] <= -0.24362):
                            return u'0'
    if (data['field30'] <= -0.23259):
        if (data.get('field40') is None):
            return u'0'
        if (data['field40'] > -0.286):
            if (data.get('field45') is None):
                return u'1'
            if (data['field45'] > -0.38012):
                if (data.get('field20') is None):
                    return u'1'
                if (data['field20'] > -0.19487):
                    if (data.get('field23') is None):
                        return u'1'
                    if (data['field23'] > -0.2741):
                        return u'1'
                    if (data['field23'] <= -0.2741):
                        if (data.get('field2') is None):
                            return u'1'
                        if (data['field2'] > -0.22336):
                            return u'1'
                        if (data['field2'] <= -0.22336):
                            if (data.get('field12') is None):
                                return u'1'
                            if (data['field12'] > -0.24407):
                                if (data.get('field9') is None):
                                    return u'1'
                                if (data['field9'] > 1.84276):
                                    if (data.get('field50') is None):
                                        return u'0'
                                    if (data['field50'] > 0.63676):
                                        return u'0'
                                    if (data['field50'] <= 0.63676):
                                        return u'1'
                                if (data['field9'] <= 1.84276):
                                    return u'1'
                            if (data['field12'] <= -0.24407):
                                if (data.get('field13') is None):
                                    return u'0'
                                if (data['field13'] > -0.25001):
                                    if (data.get('field50') is None):
                                        return u'1'
                                    if (data['field50'] > 1.47698):
                                        return u'0'
                                    if (data['field50'] <= 1.47698):
                                        return u'1'
                                if (data['field13'] <= -0.25001):
                                    return u'0'
                if (data['field20'] <= -0.19487):
                    if (data.get('field3') is None):
                        return u'1'
                    if (data['field3'] > -0.24359):
                        if (data.get('field60') is None):
                            return u'1'
                        if (data['field60'] > 4.68473):
                            return u'0'
                        if (data['field60'] <= 4.68473):
                            if (data.get('field27') is None):
                                return u'1'
                            if (data['field27'] > 5.94614):
                                if (data.get('field50') is None):
                                    return u'0'
                                if (data['field50'] > 0.0486):
                                    return u'0'
                                if (data['field50'] <= 0.0486):
                                    return u'1'
                            if (data['field27'] <= 5.94614):
                                return u'1'
                    if (data['field3'] <= -0.24359):
                        if (data.get('field19') is None):
                            return u'0'
                        if (data['field19'] > -0.24746):
                            if (data.get('field53') is None):
                                return u'1'
                            if (data['field53'] > 2.34102):
                                return u'0'
                            if (data['field53'] <= 2.34102):
                                return u'1'
                        if (data['field19'] <= -0.24746):
                            return u'0'
            if (data['field45'] <= -0.38012):
                if (data.get('field16') is None):
                    return u'0'
                if (data['field16'] > -0.21956):
                    if (data.get('field15') is None):
                        return u'1'
                    if (data['field15'] > -0.22875):
                        if (data.get('field56') is None):
                            return u'1'
                        if (data['field56'] > 4.76185):
                            return u'0'
                        if (data['field56'] <= 4.76185):
                            return u'1'
                    if (data['field15'] <= -0.22875):
                        if (data.get('field22') is None):
                            return u'0'
                        if (data['field22'] > 1.15379):
                            return u'1'
                        if (data['field22'] <= 1.15379):
                            return u'0'
                if (data['field16'] <= -0.21956):
                    if (data.get('field17') is None):
                        return u'0'
                    if (data['field17'] > 0.30384):
                        return u'1'
                    if (data['field17'] <= 0.30384):
                        return u'0'
        if (data['field40'] <= -0.286):
            if (data.get('field36') is None):
                return u'0'
            if (data['field36'] > -0.33472):
                if (data.get('field3') is None):
                    return u'0'
                if (data['field3'] > -0.22785):
                    if (data.get('field16') is None):
                        return u'1'
                    if (data['field16'] > -0.22349):
                        if (data.get('field23') is None):
                            return u'1'
                        if (data['field23'] > -0.33438):
                            return u'1'
                        if (data['field23'] <= -0.33438):
                            if (data.get('field38') is None):
                                return u'0'
                            if (data['field38'] > -0.36513):
                                return u'1'
                            if (data['field38'] <= -0.36513):
                                return u'0'
                    if (data['field16'] <= -0.22349):
                        if (data.get('field31') is None):
                            return u'0'
                        if (data['field31'] > -0.25109):
                            return u'1'
                        if (data['field31'] <= -0.25109):
                            if (data.get('field39') is None):
                                return u'0'
                            if (data['field39'] > -0.15375):
                                return u'1'
                            if (data['field39'] <= -0.15375):
                                return u'0'
                if (data['field3'] <= -0.22785):
                    if (data.get('field1') is None):
                        return u'0'
                    if (data['field1'] > -0.24039):
                        if (data.get('field46') is None):
                            return u'1'
                        if (data['field46'] > -0.30663):
                            return u'1'
                        if (data['field46'] <= -0.30663):
                            if (data.get('field11') is None):
                                return u'0'
                            if (data['field11'] > -0.23497):
                                return u'1'
                            if (data['field11'] <= -0.23497):
                                return u'0'
                    if (data['field1'] <= -0.24039):
                        if (data.get('field6') is None):
                            return u'0'
                        if (data['field6'] > -0.25829):
                            if (data.get('field48') is None):
                                return u'0'
                            if (data['field48'] > -0.27734):
                                if (data.get('field50') is None):
                                    return u'1'
                                if (data['field50'] > -0.30688):
                                    return u'1'
                                if (data['field50'] <= -0.30688):
                                    return u'0'
                            if (data['field48'] <= -0.27734):
                                return u'0'
                        if (data['field6'] <= -0.25829):
                            return u'0'
            if (data['field36'] <= -0.33472):
                if (data.get('field31') is None):
                    return u'0'
                if (data['field31'] > -0.3377):
                    if (data.get('field7') is None):
                        return u'0'
                    if (data['field7'] > -0.23477):
                        if (data.get('field23') is None):
                            return u'1'
                        if (data['field23'] > -0.37557):
                            if (data.get('field10') is None):
                                return u'1'
                            if (data['field10'] > -0.25004):
                                if (data.get('field43') is None):
                                    return u'1'
                                if (data['field43'] > 2.12946):
                                    return u'0'
                                if (data['field43'] <= 2.12946):
                                    return u'1'
                            if (data['field10'] <= -0.25004):
                                if (data.get('field43') is None):
                                    return u'0'
                                if (data['field43'] > 2.70933):
                                    return u'1'
                                if (data['field43'] <= 2.70933):
                                    return u'0'
                        if (data['field23'] <= -0.37557):
                            return u'0'
                    if (data['field7'] <= -0.23477):
                        if (data.get('field2') is None):
                            return u'0'
                        if (data['field2'] > -0.24138):
                            if (data.get('field39') is None):
                                return u'0'
                            if (data['field39'] > -0.36572):
                                return u'1'
                            if (data['field39'] <= -0.36572):
                                return u'0'
                        if (data['field2'] <= -0.24138):
                            return u'0'
                if (data['field31'] <= -0.3377):
                    if (data['field31'] > -0.37535):
                        if (data.get('field19') is None):
                            return u'0'
                        if (data['field19'] > -0.24174):
                            if (data.get('field28') is None):
                                return u'0'
                            if (data['field28'] > -0.37422):
                                if (data.get('field53') is None):
                                    return u'1'
                                if (data['field53'] > -0.46226):
                                    return u'1'
                                if (data['field53'] <= -0.46226):
                                    return u'0'
                            if (data['field28'] <= -0.37422):
                                return u'0'
                        if (data['field19'] <= -0.24174):
                            if (data.get('field2') is None):
                                return u'0'
                            if (data['field2'] > -0.24161):
                                if (data.get('field17') is None):
                                    return u'0'
                                if (data['field17'] > -0.25874):
                                    if (data['field17'] > -0.23895):
                                        return u'0'
                                    if (data['field17'] <= -0.23895):
                                        return u'1'
                                if (data['field17'] <= -0.25874):
                                    return u'0'
                            if (data['field2'] <= -0.24161):
                                return u'0'
                    if (data['field31'] <= -0.37535):
                        if (data['field36'] > -0.33668):
                            if (data.get('field9') is None):
                                return u'0'
                            if (data['field9'] > -0.24982):
                                return u'1'
                            if (data['field9'] <= -0.24982):
                                return u'0'
                        if (data['field36'] <= -0.33668):
                            return u'0'

_FILE=sys.argv[1]
_REDES=int(sys.argv[2])
start_allTime = time.time()
_FILE_TDETECCION="tDeteccion_tree.txt"
_T=20
def ransomwareIndividuales():
    ransomwareIndividuales_files = glob.glob("ransomwareIndividuales/*.csv")
    tiemposDeteccion = {}
    tiempoDeteccion = 0
    maxTiempoDeteccion = 0
    tiempoDeteccionAcumulado = 0
    truePositivos = 0
    for file in ransomwareIndividuales_files:
        ransomwareIndividuales_samples = loadtxt(file,delimiter=',',usecols=range(_T*3+1))
        tiempoDeteccion = 0
        alarmasSeguidas = 0
        positivosSample = 0
        for sample in ransomwareIndividuales_samples:
            input_sample={}
            for i in range(0,len(sample)-1):
                indice = int(i+1)
                field = str('field'+str(indice))
                input_sample[field]=float(sample[i])

            prediction_result = int(predict(input_sample))
            true_result = int(sample[_T*3])
            
            if (prediction_result == 1 and true_result == 1):
                alarmasSeguidas+=1
                tiempoDeteccion+=_T
                if (alarmasSeguidas == _REDES):
                    truePositivos+=1
                    positivosSample=1
                    if (str(tiempoDeteccion) in tiemposDeteccion):
                        tiemposDeteccion[str(tiempoDeteccion)]+=1

                    else:
                        tiemposDeteccion[str(tiempoDeteccion)]=1
                        
                    if (tiempoDeteccion > maxTiempoDeteccion):
                        maxTiempoDeteccion = tiempoDeteccion

                    tiempoDeteccionAcumulado+=tiempoDeteccion
                    tiempoDeteccion = 0
                    break

            if (prediction_result == 0 and true_result == 1.0):
                tiempoDeteccion+=_T

        if (positivosSample == 0):     
            print ("-----NO DETECTADO %s -----" % file)

    file = open(_FILE_TDETECCION,"w")
    probAcum=0
    for t in sorted(tiemposDeteccion.keys(),key=orderInt):
        probAcum += tiemposDeteccion[t]/(truePositivos)
        file.write("%i %i %.4f %.4f\n" % (int(t),tiemposDeteccion[t],tiemposDeteccion[t]/(truePositivos),probAcum));
    file.close()

     
caracteristicas = int(_T*3)+1

if (_FILE == "ransomwareIndividuales"):
    ransomwareIndividuales()
    sys.exit()

samples_set = loadtxt(_FILE,delimiter=',',usecols=range(caracteristicas))
fields = len(samples_set[0])
samples = len(samples_set)
# To make predictions fill the desired input_data in next line.
falsosPositivos = 0
falsosNegativos = 0
truePositivos = 0
trueNegativos = 0
i = 0
oneSampleTime = 0
start_samplesTime = time.time()
counter_FP = Counter()
counter_FN = Counter()
tiempoDeteccion = 0
maxTiempoDeteccion = 0
tiempoDeteccionAcumulado = 0
seguidos_FP = 0
seguidos_FN = 0
alarmasSeguidas = 0
tiemposDeteccion = {}
for sample in samples_set:
    input_sample={}
    for j in range(0,len(sample)-1):
        indice = int(j+1)
        field = str('field'+str(indice))
        input_sample[field]=float(sample[j])

    prediction_result = int(predict(input_sample))
    #print (prediction_result)
    #input("PAUSE")
    true_result = sample[len(sample)-1]
    
    sys.stdout.write("\r")
    sys.stdout.write("%.2f%% Tiempo restante (estimado): %i:%i FPs: %i" % (i*100/samples,int(oneSampleTime*(samples-i)/60),oneSampleTime*(samples-i)%60,falsosPositivos))
    sys.stdout.flush()
    
    if (int(prediction_result) == 1 and true_result == 0):
        falsosPositivos+=1
        seguidos_FP+=1
        for j in range(1,seguidos_FP+1):
            counter_FP[j]+=1
    else:
        seguidos_FP = 0 #No es un FP así que se pone el contador de seguidos a 0 

    if (int(prediction_result) == 1 and true_result == 1):
        alarmasSeguidas+=1
        tiempoDeteccion+=20
        if (alarmasSeguidas == _REDES):
            truePositivos+=1
            alarmasSeguidas = 0
            if (str(tiempoDeteccion) in tiemposDeteccion):
                tiemposDeteccion[str(tiempoDeteccion)]+=1
            else:
                tiemposDeteccion[str(tiempoDeteccion)]=1
            if (tiempoDeteccion > maxTiempoDeteccion):
                maxTiempoDeteccion = tiempoDeteccion

            tiempoDeteccionAcumulado+=tiempoDeteccion
            tiempoDeteccion = 0
            seguidos_FN = 0

    if (int(prediction_result) == 0 and true_result == 0):
        alarmasSeguidas = 0
        trueNegativos+=1

    if (int(prediction_result) == 0 and true_result == 1.0):
        alarmasSeguidas = 0
        seguidos_FN+=1
        falsosNegativos+=1
        tiempoDeteccion+=20
        for j in range(1,seguidos_FN+1):
            counter_FN[j]+=1
    
    i+=1 
    end_samplesTime = time.time()
    samplesTime = end_samplesTime - start_samplesTime
    oneSampleTime = samplesTime/i

if (truePositivos == 0):
    truePositivos=1 #Sino con las muestras de usuario no puede imprimir la línea siguiente porque hay una división entre 0.
print ("\nTotal samples: %i\nFalsos positivos: %i(%.2f%%)\nFalsos negativos: %i(%.2f%%)\nTiempo detección: %.2f (max: %i)" % (samples,falsosPositivos,falsosPositivos*100/samples,falsosNegativos,falsosNegativos*100/samples,tiempoDeteccionAcumulado/truePositivos,maxTiempoDeteccion))
end_allTime = time.time()
print("Time for all evaluation: %i (%.2fh)\n" % ((end_allTime - start_allTime),(end_allTime - start_allTime)/3600))

print ("-----Falsos Positivos Seguidos----------")
for c in OrderedDict(sorted(counter_FP.items(), key=lambda t: t[0])):
    print ('  %i          %i' % (c, counter_FP[c]))
    
print ("-----Falsos Negativos Seguidos----------")
for c in OrderedDict(sorted(counter_FN.items(), key=lambda t: t[0])):
    print ('  %i          %i' % (c, counter_FN[c]))

if (_FILE != "zeroDays.csv"):
    sys.exit()

file = open(_FILE_TDETECCION,"w")
probAcum=0
for t in sorted(tiemposDeteccion.keys(), key=orderInt):
    probAcum += tiemposDeteccion[t]/(truePositivos)
    file.write("%i %i %.4f %.4f\n" % (int(t),tiemposDeteccion[t],tiemposDeteccion[t]/(truePositivos),probAcum));
file.close()

zeroDays_files = glob.glob("zeroDays/*.csv")
for file in zeroDays_files:
    zeroDays_samples = loadtxt(file,delimiter=',',usecols=range(caracteristicas))
    tiempoDeteccion = 0
    alarmasSeguidas = 0
    for sample in zeroDays_samples:
        input_sample={}
        for i in range(0,len(sample)-1):
            indice = int(i+1)
            field = str('field'+str(indice))
            input_sample[field]=float(sample[i])

        
        prediction_result = int(predict(input_sample))
        true_result = sample[len(sample)-1]

        if (int(prediction_result) == 1 and true_result == 1):
            alarmasSeguidas+=1
            tiempoDeteccion+=_T
            
            if (alarmasSeguidas == _REDES):
                break

        if (int(prediction_result) == 0 and true_result == 1.0):
            tiempoDeteccion+=_T
            


    print ("%s: %is" % (file,tiempoDeteccion))