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
    if (data.get('field70') is None):
        return u'0'
    if (data['field70'] > -0.17953):
        if (data.get('field36') is None):
            return u'1'
        if (data['field36'] > -0.07061):
            if (data.get('field101') is None):
                return u'1'
            if (data['field101'] > 5.9981):
                return u'0'
            if (data['field101'] <= 5.9981):
                if (data.get('field86') is None):
                    return u'1'
                if (data['field86'] > -0.09184):
                    if (data.get('field138') is None):
                        return u'1'
                    if (data['field138'] > -0.20986):
                        return u'1'
                    if (data['field138'] <= -0.20986):
                        if (data.get('field141') is None):
                            return u'1'
                        if (data['field141'] > 4.84975):
                            return u'0'
                        if (data['field141'] <= 4.84975):
                            if (data.get('field137') is None):
                                return u'1'
                            if (data['field137'] > 4.08817):
                                return u'0'
                            if (data['field137'] <= 4.08817):
                                if (data.get('field131') is None):
                                    return u'1'
                                if (data['field131'] > 4.49066):
                                    if (data.get('field50') is None):
                                        return u'1'
                                    if (data['field50'] > 0.61752):
                                        return u'0'
                                    if (data['field50'] <= 0.61752):
                                        return u'1'
                                if (data['field131'] <= 4.49066):
                                    return u'1'
                if (data['field86'] <= -0.09184):
                    if (data.get('field99') is None):
                        return u'1'
                    if (data['field99'] > -0.18772):
                        return u'1'
                    if (data['field99'] <= -0.18772):
                        if (data.get('field31') is None):
                            return u'1'
                        if (data['field31'] > 0.01363):
                            return u'1'
                        if (data['field31'] <= 0.01363):
                            if (data.get('field85') is None):
                                return u'0'
                            if (data['field85'] > -0.08691):
                                return u'1'
                            if (data['field85'] <= -0.08691):
                                return u'0'
        if (data['field36'] <= -0.07061):
            if (data.get('field47') is None):
                return u'1'
            if (data['field47'] > -0.1672):
                if (data.get('field97') is None):
                    return u'1'
                if (data['field97'] > -0.21047):
                    if (data.get('field148') is None):
                        return u'1'
                    if (data['field148'] > 6.80068):
                        return u'0'
                    if (data['field148'] <= 6.80068):
                        return u'1'
                if (data['field97'] <= -0.21047):
                    if (data.get('field85') is None):
                        return u'1'
                    if (data['field85'] > -0.30071):
                        return u'1'
                    if (data['field85'] <= -0.30071):
                        return u'0'
            if (data['field47'] <= -0.1672):
                if (data.get('field14') is None):
                    return u'0'
                if (data['field14'] > -0.19865):
                    if (data.get('field106') is None):
                        return u'1'
                    if (data['field106'] > -0.28123):
                        return u'1'
                    if (data['field106'] <= -0.28123):
                        if (data.get('field35') is None):
                            return u'0'
                        if (data['field35'] > -0.19058):
                            return u'1'
                        if (data['field35'] <= -0.19058):
                            return u'0'
                if (data['field14'] <= -0.19865):
                    if (data.get('field7') is None):
                        return u'0'
                    if (data['field7'] > -0.20269):
                        if (data.get('field146') is None):
                            return u'1'
                        if (data['field146'] > -0.01786):
                            return u'1'
                        if (data['field146'] <= -0.01786):
                            if (data.get('field9') is None):
                                return u'0'
                            if (data['field9'] > 0.31635):
                                return u'1'
                            if (data['field9'] <= 0.31635):
                                return u'0'
                    if (data['field7'] <= -0.20269):
                        return u'0'
    if (data['field70'] <= -0.17953):
        if (data.get('field51') is None):
            return u'0'
        if (data['field51'] > -0.16746):
            if (data.get('field139') is None):
                return u'1'
            if (data['field139'] > -0.29304):
                if (data.get('field129') is None):
                    return u'1'
                if (data['field129'] > -0.29238):
                    return u'1'
                if (data['field129'] <= -0.29238):
                    if (data.get('field40') is None):
                        return u'1'
                    if (data['field40'] > -0.18178):
                        return u'1'
                    if (data['field40'] <= -0.18178):
                        if (data.get('field95') is None):
                            return u'0'
                        if (data['field95'] > 0.32109):
                            return u'1'
                        if (data['field95'] <= 0.32109):
                            return u'0'
            if (data['field139'] <= -0.29304):
                if (data.get('field95') is None):
                    return u'0'
                if (data['field95'] > -0.25094):
                    if (data.get('field50') is None):
                        return u'1'
                    if (data['field50'] > -0.20707):
                        return u'1'
                    if (data['field50'] <= -0.20707):
                        return u'0'
                if (data['field95'] <= -0.25094):
                    return u'0'
        if (data['field51'] <= -0.16746):
            if (data.get('field57') is None):
                return u'0'
            if (data['field57'] > -0.24928):
                if (data.get('field89') is None):
                    return u'0'
                if (data['field89'] > -0.28611):
                    if (data.get('field112') is None):
                        return u'1'
                    if (data['field112'] > -0.24311):
                        if (data.get('field148') is None):
                            return u'1'
                        if (data['field148'] > 5.50985):
                            return u'0'
                        if (data['field148'] <= 5.50985):
                            return u'1'
                    if (data['field112'] <= -0.24311):
                        if (data.get('field38') is None):
                            return u'0'
                        if (data['field38'] > -0.20159):
                            return u'1'
                        if (data['field38'] <= -0.20159):
                            return u'0'
                if (data['field89'] <= -0.28611):
                    if (data.get('field73') is None):
                        return u'0'
                    if (data['field73'] > -0.24692):
                        if (data.get('field115') is None):
                            return u'0'
                        if (data['field115'] > -0.26867):
                            return u'1'
                        if (data['field115'] <= -0.26867):
                            return u'0'
                    if (data['field73'] <= -0.24692):
                        return u'0'
            if (data['field57'] <= -0.24928):
                if (data.get('field145') is None):
                    return u'0'
                if (data['field145'] > -0.22354):
                    if (data.get('field60') is None):
                        return u'0'
                    if (data['field60'] > -0.30855):
                        if (data.get('field38') is None):
                            return u'0'
                        if (data['field38'] > -0.22148):
                            if (data.get('field43') is None):
                                return u'1'
                            if (data['field43'] > -0.21379):
                                return u'1'
                            if (data['field43'] <= -0.21379):
                                return u'0'
                        if (data['field38'] <= -0.22148):
                            return u'0'
                    if (data['field60'] <= -0.30855):
                        if (data.get('field52') is None):
                            return u'0'
                        if (data['field52'] > -0.24616):
                            if (data.get('field50') is None):
                                return u'0'
                            if (data['field50'] > -0.19161):
                                return u'1'
                            if (data['field50'] <= -0.19161):
                                return u'0'
                        if (data['field52'] <= -0.24616):
                            return u'0'
                if (data['field145'] <= -0.22354):
                    if (data.get('field92') is None):
                        return u'0'
                    if (data['field92'] > 5.62971):
                        return u'1'
                    if (data['field92'] <= 5.62971):
                        return u'0'

_FILE=sys.argv[1]
_REDES=int(sys.argv[2])
start_allTime = time.time()
_T=50
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