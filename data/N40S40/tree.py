import numpy as np
import sys
from numpy import loadtxt
import json
import time
from collections import Counter, OrderedDict
import glob
def orderInt(x):
    return int(x)
def predict(data={}):
    """ Predictor for field121 from model/5eb3fd50e84f942c65000ee8

        Pruebas y experimentos para la conferencia 2020. Se probará con distinto número de entradas, distinta limpieza de muestras de usuario, etc.
    """
    if (data.get('field47') is None):
        return u'0'
    if (data['field47'] > -0.18022):
        if (data.get('field7') is None):
            return u'1'
        if (data['field7'] > -0.07483):
            if (data.get('field68') is None):
                return u'1'
            if (data['field68'] > -0.14746):
                if (data.get('field97') is None):
                    return u'1'
                if (data['field97'] > 7.0361):
                    return u'0'
                if (data['field97'] <= 7.0361):
                    if (data.get('field111') is None):
                        return u'1'
                    if (data['field111'] > 4.67557):
                        if (data.get('field81') is None):
                            return u'1'
                        if (data['field81'] > -0.15012):
                            return u'1'
                        if (data['field81'] <= -0.15012):
                            return u'0'
                    if (data['field111'] <= 4.67557):
                        return u'1'
            if (data['field68'] <= -0.14746):
                if (data.get('field102') is None):
                    return u'1'
                if (data['field102'] > -0.2369):
                    if (data.get('field107') is None):
                        return u'1'
                    if (data['field107'] > 2.61045):
                        if (data.get('field64') is None):
                            return u'1'
                        if (data['field64'] > -0.21933):
                            return u'1'
                        if (data['field64'] <= -0.21933):
                            return u'0'
                    if (data['field107'] <= 2.61045):
                        return u'1'
                if (data['field102'] <= -0.2369):
                    if (data.get('field78') is None):
                        return u'1'
                    if (data['field78'] > -0.28358):
                        return u'1'
                    if (data['field78'] <= -0.28358):
                        if (data.get('field74') is None):
                            return u'0'
                        if (data['field74'] > -0.29947):
                            return u'1'
                        if (data['field74'] <= -0.29947):
                            return u'0'
        if (data['field7'] <= -0.07483):
            if (data.get('field4') is None):
                return u'1'
            if (data['field4'] > -0.16562):
                if (data.get('field82') is None):
                    return u'1'
                if (data['field82'] > 4.95102):
                    return u'0'
                if (data['field82'] <= 4.95102):
                    if (data.get('field106') is None):
                        return u'1'
                    if (data['field106'] > -0.37028):
                        return u'1'
                    if (data['field106'] <= -0.37028):
                        if (data.get('field95') is None):
                            return u'1'
                        if (data['field95'] > -0.41588):
                            return u'1'
                        if (data['field95'] <= -0.41588):
                            return u'0'
            if (data['field4'] <= -0.16562):
                if (data.get('field27') is None):
                    return u'0'
                if (data['field27'] > -0.20235):
                    if (data.get('field63') is None):
                        return u'1'
                    if (data['field63'] > -0.28585):
                        if (data.get('field115') is None):
                            return u'1'
                        if (data['field115'] > 5.21022):
                            return u'0'
                        if (data['field115'] <= 5.21022):
                            if (data.get('field88') is None):
                                return u'1'
                            if (data['field88'] > 4.73252):
                                return u'0'
                            if (data['field88'] <= 4.73252):
                                return u'1'
                    if (data['field63'] <= -0.28585):
                        if (data.get('field39') is None):
                            return u'0'
                        if (data['field39'] > -0.12465):
                            return u'1'
                        if (data['field39'] <= -0.12465):
                            return u'0'
                if (data['field27'] <= -0.20235):
                    if (data.get('field2') is None):
                        return u'0'
                    if (data['field2'] > -0.20667):
                        if (data.get('field24') is None):
                            return u'1'
                        if (data['field24'] > -0.2416):
                            if (data.get('field50') is None):
                                return u'1'
                            if (data['field50'] > -0.32667):
                                return u'1'
                            if (data['field50'] <= -0.32667):
                                return u'0'
                        if (data['field24'] <= -0.2416):
                            return u'0'
                    if (data['field2'] <= -0.20667):
                        return u'0'
    if (data['field47'] <= -0.18022):
        if (data.get('field70') is None):
            return u'0'
        if (data['field70'] > -0.22108):
            if (data.get('field20') is None):
                return u'1'
            if (data['field20'] > -0.1715):
                if (data.get('field96') is None):
                    return u'1'
                if (data['field96'] > -0.33072):
                    return u'1'
                if (data['field96'] <= -0.33072):
                    if (data.get('field74') is None):
                        return u'1'
                    if (data['field74'] > -0.31669):
                        return u'1'
                    if (data['field74'] <= -0.31669):
                        return u'0'
            if (data['field20'] <= -0.1715):
                if (data.get('field19') is None):
                    return u'0'
                if (data['field19'] > -0.21752):
                    if (data.get('field30') is None):
                        return u'1'
                    if (data['field30'] > -0.17751):
                        return u'1'
                    if (data['field30'] <= -0.17751):
                        if (data.get('field31') is None):
                            return u'0'
                        if (data['field31'] > -0.1968):
                            return u'1'
                        if (data['field31'] <= -0.1968):
                            return u'0'
                if (data['field19'] <= -0.21752):
                    if (data.get('field10') is None):
                        return u'0'
                    if (data['field10'] > -0.21514):
                        if (data.get('field24') is None):
                            return u'0'
                        if (data['field24'] > -0.24006):
                            if (data.get('field50') is None):
                                return u'1'
                            if (data['field50'] > -0.32276):
                                return u'1'
                            if (data['field50'] <= -0.32276):
                                return u'0'
                        if (data['field24'] <= -0.24006):
                            return u'0'
                    if (data['field10'] <= -0.21514):
                        return u'0'
        if (data['field70'] <= -0.22108):
            if (data.get('field43') is None):
                return u'0'
            if (data['field43'] > -0.2673):
                if (data.get('field76') is None):
                    return u'0'
                if (data['field76'] > -0.29611):
                    if (data.get('field101') is None):
                        return u'1'
                    if (data['field101'] > -0.31069):
                        return u'1'
                    if (data['field101'] <= -0.31069):
                        if (data.get('field50') is None):
                            return u'0'
                        if (data['field50'] > -0.30992):
                            return u'1'
                        if (data['field50'] <= -0.30992):
                            return u'0'
                if (data['field76'] <= -0.29611):
                    if (data.get('field69') is None):
                        return u'0'
                    if (data['field69'] > -0.28488):
                        if (data.get('field29') is None):
                            return u'1'
                        if (data['field29'] > -0.20425):
                            return u'1'
                        if (data['field29'] <= -0.20425):
                            return u'0'
                    if (data['field69'] <= -0.28488):
                        return u'0'
            if (data['field43'] <= -0.2673):
                if (data.get('field90') is None):
                    return u'0'
                if (data['field90'] > -0.31159):
                    if (data.get('field63') is None):
                        return u'0'
                    if (data['field63'] > -0.29841):
                        if (data.get('field19') is None):
                            return u'0'
                        if (data['field19'] > -0.22319):
                            if (data.get('field38') is None):
                                return u'1'
                            if (data['field38'] > -0.22514):
                                return u'1'
                            if (data['field38'] <= -0.22514):
                                return u'0'
                        if (data['field19'] <= -0.22319):
                            return u'0'
                    if (data['field63'] <= -0.29841):
                        if (data.get('field69') is None):
                            return u'0'
                        if (data['field69'] > 0.51724):
                            if (data.get('field85') is None):
                                return u'0'
                            if (data['field85'] > -0.03533):
                                return u'1'
                            if (data['field85'] <= -0.03533):
                                return u'0'
                        if (data['field69'] <= 0.51724):
                            return u'0'
                if (data['field90'] <= -0.31159):
                    if (data.get('field6') is None):
                        return u'0'
                    if (data['field6'] > 5.77392):
                        if (data.get('field50') is None):
                            return u'0'
                        if (data['field50'] > -0.32496):
                            return u'1'
                        if (data['field50'] <= -0.32496):
                            return u'0'
                    if (data['field6'] <= 5.77392):
                        return u'0'

_REDES = int(sys.argv[2])
_FILE=sys.argv[1]
_T=40
_FILE_TDETECCION="tDeteccion_tree.txt"
start_allTime = time.time()
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

    prediction = predict(input_sample)
    true_result = sample[len(sample)-1]

    sys.stdout.write("\r")
    sys.stdout.write("%.2f%% Tiempo restante (estimado): %i:%i FPs: %i" % (i*100/samples,int(oneSampleTime*(samples-i)/60),oneSampleTime*(samples-i)%60,falsosPositivos))
    sys.stdout.flush()
    
    if (int(prediction) == 1 and true_result == 0):
        falsosPositivos+=1
        seguidos_FP+=1
        for j in range(1,seguidos_FP+1):
            counter_FP[j]+=1
    else:
        seguidos_FP = 0 #No es un FP así que se pone el contador de seguidos a 0 

    if (int(prediction) == 1 and true_result == 1):
        alarmasSeguidas+=1
        tiempoDeteccion+=40
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

    if (int(prediction) == 0 and true_result == 0):
        alarmasSeguidas = 0
        trueNegativos+=1

    if (int(prediction) == 0 and true_result == 1.0):
        alarmasSeguidas = 0
        seguidos_FN+=1
        falsosNegativos+=1
        tiempoDeteccion+=40
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