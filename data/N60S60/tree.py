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
    if (data.get('field80') is None):
        return u'0'
    if (data['field80'] > 0.00883):
        if (data.get('field16') is None):
            return u'1'
        if (data['field16'] > 0.00461):
            if (data.get('field138') is None):
                return u'1'
            if (data['field138'] > 0.00959):
                return u'1'
            if (data['field138'] <= 0.00959):
                if (data.get('field94') is None):
                    return u'1'
                if (data['field94'] > 0.00454):
                    return u'1'
                if (data['field94'] <= 0.00454):
                    if (data.get('field62') is None):
                        return u'1'
                    if (data['field62'] > 9e-05):
                        if (data.get('field132') is None):
                            return u'1'
                        if (data['field132'] > 0.18845):
                            return u'0'
                        if (data['field132'] <= 0.18845):
                            return u'1'
                    if (data['field62'] <= 9e-05):
                        return u'0'
        if (data['field16'] <= 0.00461):
            if (data.get('field20') is None):
                return u'1'
            if (data['field20'] > 0.0019):
                if (data.get('field150') is None):
                    return u'1'
                if (data['field150'] > 0.00934):
                    return u'1'
                if (data['field150'] <= 0.00934):
                    if (data.get('field117') is None):
                        return u'1'
                    if (data['field117'] > 0.00133):
                        return u'1'
                    if (data['field117'] <= 0.00133):
                        if (data.get('field84') is None):
                            return u'0'
                        if (data['field84'] > 9e-05):
                            if (data.get('field161') is None):
                                return u'1'
                            if (data['field161'] > 0.00039):
                                return u'1'
                            if (data['field161'] <= 0.00039):
                                return u'0'
                        if (data['field84'] <= 9e-05):
                            return u'0'
            if (data['field20'] <= 0.0019):
                if (data.get('field10') is None):
                    return u'0'
                if (data['field10'] > 0.00021):
                    if (data.get('field105') is None):
                        return u'1'
                    if (data['field105'] > 0.00053):
                        return u'1'
                    if (data['field105'] <= 0.00053):
                        if (data.get('field95') is None):
                            return u'0'
                        if (data['field95'] > 0.00058):
                            return u'1'
                        if (data['field95'] <= 0.00058):
                            return u'0'
                if (data['field10'] <= 0.00021):
                    if (data.get('field55') is None):
                        return u'0'
                    if (data['field55'] > 0.0001):
                        if (data.get('field113') is None):
                            return u'1'
                        if (data['field113'] > 0.00015):
                            return u'1'
                        if (data['field113'] <= 0.00015):
                            return u'0'
                    if (data['field55'] <= 0.0001):
                        if (data.get('field9') is None):
                            return u'0'
                        if (data['field9'] > 0.01572):
                            return u'1'
                        if (data['field9'] <= 0.01572):
                            return u'0'
    if (data['field80'] <= 0.00883):
        if (data.get('field99') is None):
            return u'0'
        if (data['field99'] > 0.00492):
            if (data.get('field39') is None):
                return u'1'
            if (data['field39'] > 0.00244):
                if (data.get('field177') is None):
                    return u'1'
                if (data['field177'] > 0.00994):
                    return u'1'
                if (data['field177'] <= 0.00994):
                    if (data.get('field7') is None):
                        return u'1'
                    if (data['field7'] > 0.00035):
                        return u'1'
                    if (data['field7'] <= 0.00035):
                        if (data.get('field76') is None):
                            return u'0'
                        if (data['field76'] > 0.00166):
                            if (data.get('field162') is None):
                                return u'1'
                            if (data['field162'] > 0.06584):
                                return u'0'
                            if (data['field162'] <= 0.06584):
                                return u'1'
                        if (data['field76'] <= 0.00166):
                            return u'0'
            if (data['field39'] <= 0.00244):
                if (data.get('field29') is None):
                    return u'0'
                if (data['field29'] > 0.00193):
                    return u'1'
                if (data['field29'] <= 0.00193):
                    if (data.get('field4') is None):
                        return u'0'
                    if (data['field4'] > 0.00028):
                        if (data.get('field53') is None):
                            return u'1'
                        if (data['field53'] > 8e-05):
                            return u'1'
                        if (data['field53'] <= 8e-05):
                            return u'0'
                    if (data['field4'] <= 0.00028):
                        if (data.get('field22') is None):
                            return u'0'
                        if (data['field22'] > 0.00017):
                            if (data.get('field178') is None):
                                return u'0'
                            if (data['field178'] > 0.00586):
                                return u'1'
                            if (data['field178'] <= 0.00586):
                                return u'0'
                        if (data['field22'] <= 0.00017):
                            return u'0'
        if (data['field99'] <= 0.00492):
            if (data.get('field75') is None):
                return u'0'
            if (data['field75'] > 0.00281):
                if (data.get('field106') is None):
                    return u'0'
                if (data['field106'] > 0.00118):
                    if (data.get('field56') is None):
                        return u'1'
                    if (data['field56'] > 0.0002):
                        return u'1'
                    if (data['field56'] <= 0.0002):
                        if (data.get('field12') is None):
                            return u'1'
                        if (data['field12'] > 1e-05):
                            return u'1'
                        if (data['field12'] <= 1e-05):
                            if (data.get('field9') is None):
                                return u'0'
                            if (data['field9'] > 0.00148):
                                return u'1'
                            if (data['field9'] <= 0.00148):
                                return u'0'
                if (data['field106'] <= 0.00118):
                    if (data.get('field2') is None):
                        return u'0'
                    if (data['field2'] > 0.00223):
                        if (data.get('field50') is None):
                            return u'1'
                        if (data['field50'] > 0.03208):
                            return u'0'
                        if (data['field50'] <= 0.03208):
                            return u'1'
                    if (data['field2'] <= 0.00223):
                        if (data.get('field23') is None):
                            return u'0'
                        if (data['field23'] > 0.00176):
                            if (data.get('field85') is None):
                                return u'1'
                            if (data['field85'] > 9e-05):
                                return u'1'
                            if (data['field85'] <= 9e-05):
                                return u'0'
                        if (data['field23'] <= 0.00176):
                            if (data.get('field84') is None):
                                return u'0'
                            if (data['field84'] > 0.08794):
                                return u'1'
                            if (data['field84'] <= 0.08794):
                                return u'0'
            if (data['field75'] <= 0.00281):
                if (data.get('field108') is None):
                    return u'0'
                if (data['field108'] > 0.00296):
                    if (data.get('field4') is None):
                        return u'0'
                    if (data['field4'] > 1e-05):
                        if (data.get('field54') is None):
                            return u'1'
                        if (data['field54'] > 1e-05):
                            return u'1'
                        if (data['field54'] <= 1e-05):
                            if (data.get('field85') is None):
                                return u'0'
                            if (data['field85'] > 0.0018):
                                return u'1'
                            if (data['field85'] <= 0.0018):
                                return u'0'
                    if (data['field4'] <= 1e-05):
                        if (data.get('field42') is None):
                            return u'0'
                        if (data['field42'] > 0.01053):
                            return u'1'
                        if (data['field42'] <= 0.01053):
                            return u'0'
                if (data['field108'] <= 0.00296):
                    if (data.get('field74') is None):
                        return u'0'
                    if (data['field74'] > 0.00049):
                        if (data.get('field167') is None):
                            return u'0'
                        if (data['field167'] > 0.00839):
                            if (data.get('field30') is None):
                                return u'0'
                            if (data['field30'] > 1e-05):
                                if (data.get('field162') is None):
                                    return u'1'
                                if (data['field162'] > 0.18364):
                                    return u'0'
                                if (data['field162'] <= 0.18364):
                                    return u'1'
                            if (data['field30'] <= 1e-05):
                                return u'0'
                        if (data['field167'] <= 0.00839):
                            return u'0'
                    if (data['field74'] <= 0.00049):
                        if (data.get('field94') is None):
                            return u'0'
                        if (data['field94'] > 0.01051):
                            if (data.get('field24') is None):
                                return u'0'
                            if (data['field24'] > 0.00027):
                                if (data.get('field178') is None):
                                    return u'1'
                                if (data['field178'] > 0.24756):
                                    return u'0'
                                if (data['field178'] <= 0.24756):
                                    return u'1'
                            if (data['field24'] <= 0.00027):
                                return u'0'
                        if (data['field94'] <= 0.01051):
                            if (data.get('field111') is None):
                                return u'0'
                            if (data['field111'] > 0.07744):
                                if (data.get('field85') is None):
                                    return u'0'
                                if (data['field85'] > 0.00532):
                                    return u'1'
                                if (data['field85'] <= 0.00532):
                                    return u'0'
                            if (data['field111'] <= 0.07744):
                                return u'0'

_FILE=sys.argv[1]
_REDES=int(sys.argv[2])
start_allTime = time.time()
_T=60
_FILE_TDETECCION="tDeteccion_tree.txt"
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
        tiempoDeteccion+=_T
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
        tiempoDeteccion+=_T
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