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
    if (data.get('field52') is None):
        return u'0'
    if (data['field52'] > 0.00523):
        if (data.get('field13') is None):
            return u'1'
        if (data['field13'] > 0.00524):
            if (data.get('field81') is None):
                return u'1'
            if (data['field81'] > 0.41568):
                if (data.get('field50') is None):
                    return u'0'
                if (data['field50'] > 0.08272):
                    return u'1'
                if (data['field50'] <= 0.08272):
                    return u'0'
            if (data['field81'] <= 0.41568):
                if (data.get('field71') is None):
                    return u'1'
                if (data['field71'] > 0.38428):
                    if (data.get('field68') is None):
                        return u'1'
                    if (data['field68'] > 0.02426):
                        return u'1'
                    if (data['field68'] <= 0.02426):
                        return u'0'
                if (data['field71'] <= 0.38428):
                    if (data.get('field80') is None):
                        return u'1'
                    if (data['field80'] > 0.44521):
                        return u'0'
                    if (data['field80'] <= 0.44521):
                        if (data.get('field60') is None):
                            return u'1'
                        if (data['field60'] > 0.00858):
                            return u'1'
                        if (data['field60'] <= 0.00858):
                            if (data.get('field50') is None):
                                return u'1'
                            if (data['field50'] > 0.02643):
                                return u'1'
                            if (data['field50'] <= 0.02643):
                                if (data.get('field33') is None):
                                    return u'1'
                                if (data['field33'] > 0.00804):
                                    return u'1'
                                if (data['field33'] <= 0.00804):
                                    return u'1'
        if (data['field13'] <= 0.00524):
            if (data.get('field22') is None):
                return u'1'
            if (data['field22'] > 0.00201):
                if (data.get('field89') is None):
                    return u'1'
                if (data['field89'] > 0.01591):
                    return u'1'
                if (data['field89'] <= 0.01591):
                    if (data.get('field15') is None):
                        return u'1'
                    if (data['field15'] > 0.00097):
                        return u'1'
                    if (data['field15'] <= 0.00097):
                        if (data.get('field4') is None):
                            return u'1'
                        if (data['field4'] > 0.00131):
                            return u'1'
                        if (data['field4'] <= 0.00131):
                            if (data.get('field9') is None):
                                return u'0'
                            if (data['field9'] > 0.00087):
                                return u'1'
                            if (data['field9'] <= 0.00087):
                                if (data.get('field17') is None):
                                    return u'0'
                                if (data['field17'] > 0.00194):
                                    if (data.get('field85') is None):
                                        return u'1'
                                    if (data['field85'] > 0.11434):
                                        return u'0'
                                    if (data['field85'] <= 0.11434):
                                        return u'1'
                                if (data['field17'] <= 0.00194):
                                    return u'0'
            if (data['field22'] <= 0.00201):
                if (data.get('field4') is None):
                    return u'0'
                if (data['field4'] > 0.00043):
                    if (data.get('field34') is None):
                        return u'1'
                    if (data['field34'] > 0.00207):
                        return u'1'
                    if (data['field34'] <= 0.00207):
                        if (data.get('field38') is None):
                            return u'1'
                        if (data['field38'] > 9e-05):
                            return u'1'
                        if (data['field38'] <= 9e-05):
                            return u'0'
                if (data['field4'] <= 0.00043):
                    if (data.get('field6') is None):
                        return u'0'
                    if (data['field6'] > 1e-05):
                        if (data.get('field19') is None):
                            return u'1'
                        if (data['field19'] > 1e-05):
                            if (data.get('field82') is None):
                                return u'1'
                            if (data['field82'] > 0.39148):
                                return u'0'
                            if (data['field82'] <= 0.39148):
                                return u'1'
                        if (data['field19'] <= 1e-05):
                            if (data.get('field64') is None):
                                return u'0'
                            if (data['field64'] > 0.15648):
                                return u'1'
                            if (data['field64'] <= 0.15648):
                                return u'0'
                    if (data['field6'] <= 1e-05):
                        if (data.get('field15') is None):
                            return u'0'
                        if (data['field15'] > 0.00481):
                            if (data.get('field58') is None):
                                return u'1'
                            if (data['field58'] > 0.00483):
                                return u'1'
                            if (data['field58'] <= 0.00483):
                                return u'0'
                        if (data['field15'] <= 0.00481):
                            if (data.get('field20') is None):
                                return u'0'
                            if (data['field20'] > 0):
                                if (data.get('field89') is None):
                                    return u'0'
                                if (data['field89'] > 0.03024):
                                    if (data.get('field85') is None):
                                        return u'1'
                                    if (data['field85'] > 0.22171):
                                        return u'0'
                                    if (data['field85'] <= 0.22171):
                                        return u'1'
                                if (data['field89'] <= 0.03024):
                                    return u'0'
                            if (data['field20'] <= 0):
                                return u'0'
    if (data['field52'] <= 0.00523):
        if (data.get('field31') is None):
            return u'0'
        if (data['field31'] > 0.00663):
            if (data.get('field1') is None):
                return u'1'
            if (data['field1'] > 0.0015):
                if (data.get('field47') is None):
                    return u'1'
                if (data['field47'] > 0.00837):
                    return u'1'
                if (data['field47'] <= 0.00837):
                    if (data.get('field68') is None):
                        return u'1'
                    if (data['field68'] > 0.00888):
                        if (data['field68'] > 0.14851):
                            if (data.get('field9') is None):
                                return u'1'
                            if (data['field9'] > 0.00133):
                                if (data['field68'] > 0.15447):
                                    return u'1'
                                if (data['field68'] <= 0.15447):
                                    return u'0'
                            if (data['field9'] <= 0.00133):
                                return u'0'
                        if (data['field68'] <= 0.14851):
                            return u'1'
                    if (data['field68'] <= 0.00888):
                        if (data.get('field58') is None):
                            return u'1'
                        if (data['field58'] > 0.00035):
                            return u'1'
                        if (data['field58'] <= 0.00035):
                            if (data.get('field43') is None):
                                return u'0'
                            if (data['field43'] > 0.00117):
                                if (data.get('field64') is None):
                                    return u'1'
                                if (data['field64'] > 0.00224):
                                    return u'1'
                                if (data['field64'] <= 0.00224):
                                    return u'0'
                            if (data['field43'] <= 0.00117):
                                return u'0'
            if (data['field1'] <= 0.0015):
                if (data.get('field55') is None):
                    return u'0'
                if (data['field55'] > 0.00094):
                    if (data.get('field25') is None):
                        return u'1'
                    if (data['field25'] > 0.00028):
                        return u'1'
                    if (data['field25'] <= 0.00028):
                        if (data.get('field16') is None):
                            return u'1'
                        if (data['field16'] > 1e-05):
                            return u'1'
                        if (data['field16'] <= 1e-05):
                            if (data.get('field50') is None):
                                return u'0'
                            if (data['field50'] > 0.44034):
                                return u'1'
                            if (data['field50'] <= 0.44034):
                                return u'0'
                if (data['field55'] <= 0.00094):
                    if (data.get('field15') is None):
                        return u'0'
                    if (data['field15'] > 5e-05):
                        if (data.get('field10') is None):
                            return u'1'
                        if (data['field10'] > 0.00014):
                            return u'1'
                        if (data['field10'] <= 0.00014):
                            if (data.get('field17') is None):
                                return u'0'
                            if (data['field17'] > 0.00059):
                                return u'1'
                            if (data['field17'] <= 0.00059):
                                return u'0'
                    if (data['field15'] <= 5e-05):
                        return u'0'
        if (data['field31'] <= 0.00663):
            if (data.get('field41') is None):
                return u'0'
            if (data['field41'] > 0.00367):
                if (data.get('field11') is None):
                    return u'0'
                if (data['field11'] > 0.00128):
                    if (data.get('field57') is None):
                        return u'1'
                    if (data['field57'] > 0.00222):
                        return u'1'
                    if (data['field57'] <= 0.00222):
                        if (data.get('field2') is None):
                            return u'1'
                        if (data['field2'] > 7e-05):
                            if (data.get('field64') is None):
                                return u'1'
                            if (data['field64'] > 0.29359):
                                return u'0'
                            if (data['field64'] <= 0.29359):
                                return u'1'
                        if (data['field2'] <= 7e-05):
                            if (data.get('field47') is None):
                                return u'0'
                            if (data['field47'] > 0.00267):
                                if (data.get('field43') is None):
                                    return u'1'
                                if (data['field43'] > 0.19046):
                                    return u'0'
                                if (data['field43'] <= 0.19046):
                                    return u'1'
                            if (data['field47'] <= 0.00267):
                                if (data.get('field39') is None):
                                    return u'0'
                                if (data['field39'] > 0.01921):
                                    if (data.get('field27') is None):
                                        return u'1'
                                    if (data['field27'] > 1e-05):
                                        return u'1'
                                    if (data['field27'] <= 1e-05):
                                        return u'0'
                                if (data['field39'] <= 0.01921):
                                    return u'0'
                if (data['field11'] <= 0.00128):
                    if (data.get('field7') is None):
                        return u'0'
                    if (data['field7'] > 0.00018):
                        if (data.get('field55') is None):
                            return u'1'
                        if (data['field55'] > 0.0017):
                            return u'1'
                        if (data['field55'] <= 0.0017):
                            if (data.get('field85') is None):
                                return u'0'
                            if (data['field85'] > 0.01357):
                                return u'1'
                            if (data['field85'] <= 0.01357):
                                return u'0'
                    if (data['field7'] <= 0.00018):
                        if (data.get('field23') is None):
                            return u'0'
                        if (data['field23'] > 0.00018):
                            if (data.get('field86') is None):
                                return u'0'
                            if (data['field86'] > 0.01482):
                                if (data.get('field53') is None):
                                    return u'1'
                                if (data['field53'] > 0.01651):
                                    return u'0'
                                if (data['field53'] <= 0.01651):
                                    return u'1'
                            if (data['field86'] <= 0.01482):
                                return u'0'
                        if (data['field23'] <= 0.00018):
                            return u'0'
            if (data['field41'] <= 0.00367):
                if (data.get('field47') is None):
                    return u'0'
                if (data['field47'] > 0.00382):
                    if (data.get('field17') is None):
                        return u'0'
                    if (data['field17'] > 0.00033):
                        if (data.get('field57') is None):
                            return u'1'
                        if (data['field57'] > 0.00223):
                            return u'1'
                        if (data['field57'] <= 0.00223):
                            if (data.get('field38') is None):
                                return u'0'
                            if (data['field38'] > 0.0004):
                                if (data.get('field78') is None):
                                    return u'1'
                                if (data['field78'] > 0.00123):
                                    return u'1'
                                if (data['field78'] <= 0.00123):
                                    if (data.get('field85') is None):
                                        return u'0'
                                    if (data['field85'] > 0.04031):
                                        return u'1'
                                    if (data['field85'] <= 0.04031):
                                        return u'0'
                            if (data['field38'] <= 0.0004):
                                if (data.get('field33') is None):
                                    return u'0'
                                if (data['field33'] > 0.00059):
                                    if (data.get('field79') is None):
                                        return u'1'
                                    if (data['field79'] > 0.01465):
                                        return u'1'
                                    if (data['field79'] <= 0.01465):
                                        return u'0'
                                if (data['field33'] <= 0.00059):
                                    if (data.get('field9') is None):
                                        return u'0'
                                    if (data['field9'] > 0.12062):
                                        return u'1'
                                    if (data['field9'] <= 0.12062):
                                        return u'0'
                    if (data['field17'] <= 0.00033):
                        if (data.get('field4') is None):
                            return u'0'
                        if (data['field4'] > 0.00735):
                            return u'1'
                        if (data['field4'] <= 0.00735):
                            if (data.get('field6') is None):
                                return u'0'
                            if (data['field6'] > 0.03668):
                                return u'1'
                            if (data['field6'] <= 0.03668):
                                return u'0'
                if (data['field47'] <= 0.00382):
                    if (data.get('field46') is None):
                        return u'0'
                    if (data['field46'] > 0.00181):
                        if (data.get('field29') is None):
                            return u'0'
                        if (data['field29'] > 0.00021):
                            if (data.get('field48') is None):
                                return u'1'
                            if (data['field48'] > 3e-05):
                                if (data.get('field16') is None):
                                    return u'1'
                                if (data['field16'] > 1e-05):
                                    return u'1'
                                if (data['field16'] <= 1e-05):
                                    if (data.get('field85') is None):
                                        return u'0'
                                    if (data['field85'] > 0.00969):
                                        return u'1'
                                    if (data['field85'] <= 0.00969):
                                        return u'0'
                            if (data['field48'] <= 3e-05):
                                return u'0'
                        if (data['field29'] <= 0.00021):
                            if (data.get('field2') is None):
                                return u'0'
                            if (data['field2'] > 1e-05):
                                if (data.get('field82') is None):
                                    return u'0'
                                if (data['field82'] > 0.00406):
                                    if (data.get('field72') is None):
                                        return u'1'
                                    if (data['field72'] > 0.00206):
                                        return u'1'
                                    if (data['field72'] <= 0.00206):
                                        return u'0'
                                if (data['field82'] <= 0.00406):
                                    return u'0'
                            if (data['field2'] <= 1e-05):
                                return u'0'
                    if (data['field46'] <= 0.00181):
                        if (data.get('field44') is None):
                            return u'0'
                        if (data['field44'] > 0.00159):
                            if (data.get('field30') is None):
                                return u'0'
                            if (data['field30'] > 0.00034):
                                if (data.get('field63') is None):
                                    return u'1'
                                if (data['field63'] > 0.00133):
                                    if (data.get('field88') is None):
                                        return u'1'
                                    if (data['field88'] > 0.00049):
                                        return u'1'
                                    if (data['field88'] <= 0.00049):
                                        return u'0'
                                if (data['field63'] <= 0.00133):
                                    return u'0'
                            if (data['field30'] <= 0.00034):
                                if (data.get('field6') is None):
                                    return u'0'
                                if (data['field6'] > 0.00039):
                                    if (data.get('field50') is None):
                                        return u'0'
                                    if (data['field50'] > 0.001):
                                        return u'1'
                                    if (data['field50'] <= 0.001):
                                        return u'0'
                                if (data['field6'] <= 0.00039):
                                    return u'0'
                        if (data['field44'] <= 0.00159):
                            if (data['field47'] > 5e-05):
                                if (data.get('field4') is None):
                                    return u'0'
                                if (data['field4'] > 1e-05):
                                    if (data.get('field61') is None):
                                        return u'0'
                                    if (data['field61'] > 0.00886):
                                        if (data.get('field85') is None):
                                            return u'1'
                                        if (data['field85'] > 0.00078):
                                            return u'1'
                                        if (data['field85'] <= 0.00078):
                                            return u'0'
                                    if (data['field61'] <= 0.00886):
                                        return u'0'
                                if (data['field4'] <= 1e-05):
                                    return u'0'
                            if (data['field47'] <= 5e-05):
                                return u'0'

_FILE=sys.argv[1]
_REDES=int(sys.argv[2])
start_allTime = time.time()
_T=30
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