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
    if (data.get('field13') is None):
            return u'0'
    if (data['field13'] > 0.01015):
        if (data.get('field3') is None):
            return u'1'
        if (data['field3'] > 0.0068):
            if (data.get('field19') is None):
                return u'1'
            if (data['field19'] > 0.01196):
                if (data.get('field21') is None):
                    return u'1'
                if (data['field21'] > 0.26036):
                    return u'1'
                if (data['field21'] <= 0.26036):
                    if (data.get('field18') is None):
                        return u'1'
                    if (data['field18'] > 0.06993):
                        if (data.get('field6') is None):
                            return u'1'
                        if (data['field6'] > 0.00238):
                            if (data.get('field7') is None):
                                return u'1'
                            if (data['field7'] > 0.06121):
                                return u'1'
                            if (data['field7'] <= 0.06121):
                                return u'1'
                        if (data['field6'] <= 0.00238):
                            return u'1'
                    if (data['field18'] <= 0.06993):
                        return u'1'
            if (data['field19'] <= 0.01196):
                if (data.get('field27') is None):
                    return u'1'
                if (data['field27'] > 0.00549):
                    if (data.get('field18') is None):
                        return u'1'
                    if (data['field18'] > 0.00722):
                        return u'1'
                    if (data['field18'] <= 0.00722):
                        if (data.get('field12') is None):
                            return u'1'
                        if (data['field12'] > 0.08818):
                            if (data.get('field9') is None):
                                return u'1'
                            if (data['field9'] > 0.01459):
                                return u'0'
                            if (data['field9'] <= 0.01459):
                                if (data.get('field21') is None):
                                    return u'1'
                                if (data['field21'] > 0.28423):
                                    return u'0'
                                if (data['field21'] <= 0.28423):
                                    return u'1'
                        if (data['field12'] <= 0.08818):
                            if (data['field13'] > 0.01815):
                                return u'1'
                            if (data['field13'] <= 0.01815):
                                if (data['field3'] > 0.02311):
                                    return u'0'
                                if (data['field3'] <= 0.02311):
                                    return u'1'
                if (data['field27'] <= 0.00549):
                    if (data.get('field10') is None):
                        return u'1'
                    if (data['field10'] > 0.00158):
                        return u'1'
                    if (data['field10'] <= 0.00158):
                        if (data.get('field1') is None):
                            return u'1'
                        if (data['field1'] > 0.00192):
                            if (data.get('field2') is None):
                                return u'1'
                            if (data['field2'] > 0.07762):
                                if (data.get('field11') is None):
                                    return u'0'
                                if (data['field11'] > 0.09159):
                                    return u'1'
                                if (data['field11'] <= 0.09159):
                                    return u'0'
                            if (data['field2'] <= 0.07762):
                                return u'1'
                        if (data['field1'] <= 0.00192):
                            if (data.get('field2') is None):
                                return u'1'
                            if (data['field2'] > 0.00242):
                                if (data.get('field24') is None):
                                    return u'1'
                                if (data['field24'] > 0.15946):
                                    return u'0'
                                if (data['field24'] <= 0.15946):
                                    return u'1'
                            if (data['field2'] <= 0.00242):
                                if (data.get('field21') is None):
                                    return u'0'
                                if (data['field21'] > 0.00091):
                                    if (data.get('field16') is None):
                                        return u'1'
                                    if (data['field16'] > 0.00102):
                                        return u'1'
                                    if (data['field16'] <= 0.00102):
                                        return u'0'
                                if (data['field21'] <= 0.00091):
                                    return u'0'
        if (data['field3'] <= 0.0068):
            if (data['field3'] > 9e-05):
                if (data.get('field30') is None):
                    return u'1'
                if (data['field30'] > 0.00527):
                    if (data['field3'] > 0.0018):
                        if (data.get('field15') is None):
                            return u'1'
                        if (data['field15'] > 0.01303):
                            return u'1'
                        if (data['field15'] <= 0.01303):
                            if (data.get('field20') is None):
                                return u'1'
                            if (data['field20'] > 0.00737):
                                if (data.get('field12') is None):
                                    return u'1'
                                if (data['field12'] > 0.28737):
                                    return u'0'
                                if (data['field12'] <= 0.28737):
                                    if (data.get('field5') is None):
                                        return u'1'
                                    if (data['field5'] > 0.02418):
                                        if (data.get('field11') is None):
                                            return u'1'
                                        if (data['field11'] > 0.01355):
                                            return u'1'
                                        if (data['field11'] <= 0.01355):
                                            return u'0'
                                    if (data['field5'] <= 0.02418):
                                        return u'1'
                            if (data['field20'] <= 0.00737):
                                if (data['field30'] > 0.09425):
                                    if (data.get('field12') is None):
                                        return u'1'
                                    if (data['field12'] > 6e-05):
                                        if (data.get('field10') is None):
                                            return u'1'
                                        if (data['field10'] > 0.00318):
                                            if (data.get('field9') is None):
                                                return u'0'
                                            if (data['field9'] > 0.00459):
                                                return u'1'
                                            if (data['field9'] <= 0.00459):
                                                return u'0'
                                        if (data['field10'] <= 0.00318):
                                            return u'1'
                                    if (data['field12'] <= 6e-05):
                                        return u'0'
                                if (data['field30'] <= 0.09425):
                                    if (data.get('field22') is None):
                                        return u'1'
                                    if (data['field22'] > 0.3402):
                                        return u'0'
                                    if (data['field22'] <= 0.3402):
                                        return u'1'
                    if (data['field3'] <= 0.0018):
                        if (data.get('field2') is None):
                            return u'1'
                        if (data['field2'] > 0.00103):
                            return u'1'
                        if (data['field2'] <= 0.00103):
                            if (data.get('field1') is None):
                                return u'1'
                            if (data['field1'] > 7e-05):
                                return u'1'
                            if (data['field1'] <= 7e-05):
                                if (data.get('field5') is None):
                                    return u'1'
                                if (data['field5'] > 0.00011):
                                    if (data.get('field26') is None):
                                        return u'1'
                                    if (data['field26'] > 0.00867):
                                        return u'1'
                                    if (data['field26'] <= 0.00867):
                                        if (data.get('field15') is None):
                                            return u'0'
                                        if (data['field15'] > 0.13786):
                                            return u'1'
                                        if (data['field15'] <= 0.13786):
                                            return u'0'
                                if (data['field5'] <= 0.00011):
                                    return u'0'
                if (data['field30'] <= 0.00527):
                    if (data.get('field17') is None):
                        return u'1'
                    if (data['field17'] > 0.00693):
                        if (data.get('field5') is None):
                            return u'1'
                        if (data['field5'] > 0.00128):
                            return u'1'
                        if (data['field5'] <= 0.00128):
                            if (data.get('field26') is None):
                                return u'1'
                            if (data['field26'] > 0.00614):
                                if (data.get('field24') is None):
                                    return u'1'
                                if (data['field24'] > 0.09016):
                                    if (data['field3'] > 0.00498):
                                        return u'1'
                                    if (data['field3'] <= 0.00498):
                                        return u'0'
                                if (data['field24'] <= 0.09016):
                                    return u'1'
                            if (data['field26'] <= 0.00614):
                                if (data.get('field8') is None):
                                    return u'0'
                                if (data['field8'] > 1e-05):
                                    return u'1'
                                if (data['field8'] <= 1e-05):
                                    if (data.get('field9') is None):
                                        return u'0'
                                    if (data['field9'] > 0.00102):
                                        return u'1'
                                    if (data['field9'] <= 0.00102):
                                        return u'0'
                    if (data['field17'] <= 0.00693):
                        if (data.get('field1') is None):
                            return u'0'
                        if (data['field1'] > 0.00048):
                            if (data.get('field5') is None):
                                return u'1'
                            if (data['field5'] > 0.00068):
                                return u'1'
                            if (data['field5'] <= 0.00068):
                                if (data['field17'] > 2e-05):
                                    return u'1'
                                if (data['field17'] <= 2e-05):
                                    if (data.get('field29') is None):
                                        return u'0'
                                    if (data['field29'] > 0.00355):
                                        if (data.get('field11') is None):
                                            return u'1'
                                        if (data['field11'] > 0.00228):
                                            return u'1'
                                        if (data['field11'] <= 0.00228):
                                            return u'0'
                                    if (data['field29'] <= 0.00355):
                                        return u'0'
                        if (data['field1'] <= 0.00048):
                            if (data.get('field18') is None):
                                return u'0'
                            if (data['field18'] > 0.01863):
                                return u'1'
                            if (data['field18'] <= 0.01863):
                                if (data.get('field16') is None):
                                    return u'0'
                                if (data['field16'] > 0.03891):
                                    if (data['field3'] > 0.0039):
                                        return u'1'
                                    if (data['field3'] <= 0.0039):
                                        return u'0'
                                if (data['field16'] <= 0.03891):
                                    return u'0'
            if (data['field3'] <= 9e-05):
                if (data.get('field8') is None):
                    return u'0'
                if (data['field8'] > 0.0016):
                    if (data.get('field23') is None):
                        return u'1'
                    if (data['field23'] > 0.05923):
                        if (data.get('field5') is None):
                            return u'0'
                        if (data['field5'] > 0.01103):
                            return u'1'
                        if (data['field5'] <= 0.01103):
                            return u'0'
                    if (data['field23'] <= 0.05923):
                        if (data.get('field1') is None):
                            return u'1'
                        if (data['field1'] > 0.00175):
                            return u'1'
                        if (data['field1'] <= 0.00175):
                            if (data.get('field4') is None):
                                return u'1'
                            if (data['field4'] > 0.00556):
                                return u'1'
                            if (data['field4'] <= 0.00556):
                                if (data.get('field19') is None):
                                    return u'1'
                                if (data['field19'] > 0.00603):
                                    if (data.get('field5') is None):
                                        return u'1'
                                    if (data['field5'] > 0.00037):
                                        return u'1'
                                    if (data['field5'] <= 0.00037):
                                        if (data.get('field24') is None):
                                            return u'0'
                                        if (data['field24'] > 0.01602):
                                            return u'0'
                                        if (data['field24'] <= 0.01602):
                                            return u'1'
                                if (data['field19'] <= 0.00603):
                                    if (data.get('field20') is None):
                                        return u'0'
                                    if (data['field20'] > 0.00201):
                                        return u'1'
                                    if (data['field20'] <= 0.00201):
                                        return u'0'
                if (data['field8'] <= 0.0016):
                    if (data.get('field2') is None):
                        return u'0'
                    if (data['field2'] > 0.00087):
                        if (data.get('field30') is None):
                            return u'1'
                        if (data['field30'] > 0.00469):
                            if (data.get('field23') is None):
                                return u'1'
                            if (data['field23'] > 0.04251):
                                return u'0'
                            if (data['field23'] <= 0.04251):
                                return u'1'
                        if (data['field30'] <= 0.00469):
                            if (data.get('field7') is None):
                                return u'0'
                            if (data['field7'] > 0.00071):
                                if (data.get('field11') is None):
                                    return u'1'
                                if (data['field11'] > 8e-05):
                                    return u'1'
                                if (data['field11'] <= 8e-05):
                                    return u'0'
                            if (data['field7'] <= 0.00071):
                                if (data.get('field4') is None):
                                    return u'0'
                                if (data['field4'] > 0.01779):
                                    return u'1'
                                if (data['field4'] <= 0.01779):
                                    return u'0'
                    if (data['field2'] <= 0.00087):
                        if (data.get('field1') is None):
                            return u'0'
                        if (data['field1'] > 6e-05):
                            if (data.get('field10') is None):
                                return u'0'
                            if (data['field10'] > 5e-05):
                                if (data.get('field20') is None):
                                    return u'1'
                                if (data['field20'] > 0.00021):
                                    return u'1'
                                if (data['field20'] <= 0.00021):
                                    return u'0'
                            if (data['field10'] <= 5e-05):
                                if (data.get('field5') is None):
                                    return u'0'
                                if (data['field5'] > 0.00992):
                                    if (data.get('field19') is None):
                                        return u'1'
                                    if (data['field19'] > 0.14352):
                                        return u'0'
                                    if (data['field19'] <= 0.14352):
                                        return u'1'
                                if (data['field5'] <= 0.00992):
                                    return u'0'
                        if (data['field1'] <= 6e-05):
                            if (data['field2'] > 1e-05):
                                if (data.get('field19') is None):
                                    return u'0'
                                if (data['field19'] > 0.00276):
                                    if (data.get('field9') is None):
                                        return u'1'
                                    if (data['field9'] > 1e-05):
                                        return u'1'
                                    if (data['field9'] <= 1e-05):
                                        if (data.get('field18') is None):
                                            return u'0'
                                        if (data['field18'] > 0.17866):
                                            return u'1'
                                        if (data['field18'] <= 0.17866):
                                            return u'0'
                                if (data['field19'] <= 0.00276):
                                    return u'0'
                            if (data['field2'] <= 1e-05):
                                if (data.get('field9') is None):
                                    return u'0'
                                if (data['field9'] > 2e-05):
                                    if (data.get('field6') is None):
                                        return u'0'
                                    if (data['field6'] > 4e-05):
                                        if (data['field9'] > 0.00049):
                                            if (data.get('field11') is None):
                                                return u'0'
                                            if (data['field11'] > 0.19833):
                                                return u'1'
                                            if (data['field11'] <= 0.19833):
                                                return u'0'
                                        if (data['field9'] <= 0.00049):
                                            return u'1'
                                    if (data['field6'] <= 4e-05):
                                        return u'0'
                                if (data['field9'] <= 2e-05):
                                    return u'0'
    if (data['field13'] <= 0.01015):
        if (data.get('field14') is None):
            return u'0'
        if (data['field14'] > 0.00415):
            if (data.get('field4') is None):
                return u'1'
            if (data['field4'] > 0.00245):
                if (data.get('field28') is None):
                    return u'1'
                if (data['field28'] > 0.00708):
                    if (data.get('field27') is None):
                        return u'1'
                    if (data['field27'] > 0.30915):
                        if (data.get('field9') is None):
                            return u'1'
                        if (data['field9'] > 0.0001):
                            return u'1'
                        if (data['field9'] <= 0.0001):
                            return u'0'
                    if (data['field27'] <= 0.30915):
                        if (data.get('field21') is None):
                            return u'1'
                        if (data['field21'] > 0.38924):
                            if (data.get('field9') is None):
                                return u'1'
                            if (data['field9'] > 0.00319):
                                return u'1'
                            if (data['field9'] <= 0.00319):
                                return u'0'
                        if (data['field21'] <= 0.38924):
                            return u'1'
                if (data['field28'] <= 0.00708):
                    if (data.get('field11') is None):
                        return u'1'
                    if (data['field11'] > 0.00312):
                        return u'1'
                    if (data['field11'] <= 0.00312):
                        if (data.get('field20') is None):
                            return u'1'
                        if (data['field20'] > 0.00768):
                            return u'1'
                        if (data['field20'] <= 0.00768):
                            if (data.get('field12') is None):
                                return u'0'
                            if (data['field12'] > 7e-05):
                                if (data.get('field23') is None):
                                    return u'1'
                                if (data['field23'] > 0.11254):
                                    return u'0'
                                if (data['field23'] <= 0.11254):
                                    return u'1'
                            if (data['field12'] <= 7e-05):
                                if (data.get('field27') is None):
                                    return u'0'
                                if (data['field27'] > 0.02166):
                                    if (data['field27'] > 0.13764):
                                        return u'0'
                                    if (data['field27'] <= 0.13764):
                                        return u'1'
                                if (data['field27'] <= 0.02166):
                                    return u'0'
            if (data['field4'] <= 0.00245):
                if (data.get('field10') is None):
                    return u'1'
                if (data['field10'] > 0.00091):
                    if (data.get('field25') is None):
                        return u'1'
                    if (data['field25'] > 0.23033):
                        if (data['field4'] > 0.00034):
                            if (data.get('field17') is None):
                                return u'1'
                            if (data['field17'] > 0.06965):
                                return u'0'
                            if (data['field17'] <= 0.06965):
                                return u'1'
                        if (data['field4'] <= 0.00034):
                            return u'0'
                    if (data['field25'] <= 0.23033):
                        if (data.get('field29') is None):
                            return u'1'
                        if (data['field29'] > 0.00955):
                            return u'1'
                        if (data['field29'] <= 0.00955):
                            if (data.get('field1') is None):
                                return u'1'
                            if (data['field1'] > 0.00028):
                                return u'1'
                            if (data['field1'] <= 0.00028):
                                if (data.get('field24') is None):
                                    return u'1'
                                if (data['field24'] > 0.04732):
                                    if (data.get('field20') is None):
                                        return u'0'
                                    if (data['field20'] > 0.02921):
                                        return u'1'
                                    if (data['field20'] <= 0.02921):
                                        return u'0'
                                if (data['field24'] <= 0.04732):
                                    if (data['field29'] > 0.00039):
                                        return u'1'
                                    if (data['field29'] <= 0.00039):
                                        if (data.get('field19') is None):
                                            return u'0'
                                        if (data['field19'] > 2e-05):
                                            return u'1'
                                        if (data['field19'] <= 2e-05):
                                            return u'0'
                if (data['field10'] <= 0.00091):
                    if (data.get('field7') is None):
                        return u'0'
                    if (data['field7'] > 0.00033):
                        if (data.get('field1') is None):
                            return u'1'
                        if (data['field1'] > 0.00055):
                            if (data.get('field27') is None):
                                return u'1'
                            if (data['field27'] > 0.00319):
                                return u'1'
                            if (data['field27'] <= 0.00319):
                                if (data['field7'] > 0.00893):
                                    return u'1'
                                if (data['field7'] <= 0.00893):
                                    return u'0'
                        if (data['field1'] <= 0.00055):
                            if (data.get('field6') is None):
                                return u'1'
                            if (data['field6'] > 0.00014):
                                if (data.get('field8') is None):
                                    return u'1'
                                if (data['field8'] > 0.00011):
                                    if (data.get('field17') is None):
                                        return u'1'
                                    if (data['field17'] > 0.00052):
                                        return u'1'
                                    if (data['field17'] <= 0.00052):
                                        return u'0'
                                if (data['field8'] <= 0.00011):
                                    if (data.get('field23') is None):
                                        return u'0'
                                    if (data['field23'] > 0.01429):
                                        return u'0'
                                    if (data['field23'] <= 0.01429):
                                        if (data.get('field28') is None):
                                            return u'1'
                                        if (data['field28'] > 0.01271):
                                            return u'0'
                                        if (data['field28'] <= 0.01271):
                                            return u'1'
                            if (data['field6'] <= 0.00014):
                                if (data.get('field20') is None):
                                    return u'0'
                                if (data['field20'] > 0.06443):
                                    return u'1'
                                if (data['field20'] <= 0.06443):
                                    return u'0'
                    if (data['field7'] <= 0.00033):
                        if (data.get('field1') is None):
                            return u'0'
                        if (data['field1'] > 2e-05):
                            if (data['field4'] > 0.00041):
                                if (data.get('field5') is None):
                                    return u'1'
                                if (data['field5'] > 3e-05):
                                    return u'1'
                                if (data['field5'] <= 3e-05):
                                    return u'0'
                            if (data['field4'] <= 0.00041):
                                if (data.get('field20') is None):
                                    return u'0'
                                if (data['field20'] > 0.00119):
                                    if (data.get('field29') is None):
                                        return u'0'
                                    if (data['field29'] > 0.04062):
                                        return u'0'
                                    if (data['field29'] <= 0.04062):
                                        if (data.get('field27') is None):
                                            return u'1'
                                        if (data['field27'] > 0.00043):
                                            return u'1'
                                        if (data['field27'] <= 0.00043):
                                            return u'0'
                                if (data['field20'] <= 0.00119):
                                    return u'0'
                        if (data['field1'] <= 2e-05):
                            return u'0'
        if (data['field14'] <= 0.00415):
            if (data.get('field17') is None):
                return u'0'
            if (data['field17'] > 0.00359):
                if (data.get('field7') is None):
                    return u'1'
                if (data['field7'] > 0.00082):
                    if (data.get('field5') is None):
                        return u'1'
                    if (data['field5'] > 0.00088):
                        if (data.get('field15') is None):
                            return u'1'
                        if (data['field15'] > 0.00315):
                            if (data.get('field25') is None):
                                return u'1'
                            if (data['field25'] > 0.00738):
                                return u'1'
                            if (data['field25'] <= 0.00738):
                                if (data.get('field26') is None):
                                    return u'1'
                                if (data['field26'] > 0.04841):
                                    if (data.get('field9') is None):
                                        return u'0'
                                    if (data['field9'] > 0.00687):
                                        return u'1'
                                    if (data['field9'] <= 0.00687):
                                        return u'0'
                                if (data['field26'] <= 0.04841):
                                    return u'1'
                        if (data['field15'] <= 0.00315):
                            if (data['field5'] > 0.00678):
                                return u'1'
                            if (data['field5'] <= 0.00678):
                                if (data.get('field16') is None):
                                    return u'1'
                                if (data['field16'] > 0.0073):
                                    return u'1'
                                if (data['field16'] <= 0.0073):
                                    if (data.get('field19') is None):
                                        return u'0'
                                    if (data['field19'] > 0.03817):
                                        return u'1'
                                    if (data['field19'] <= 0.03817):
                                        return u'0'
                    if (data['field5'] <= 0.00088):
                        if (data.get('field21') is None):
                            return u'1'
                        if (data['field21'] > 0.00556):
                            if (data.get('field26') is None):
                                return u'1'
                            if (data['field26'] > 0.24422):
                                if (data['field17'] > 0.02123):
                                    return u'0'
                                if (data['field17'] <= 0.02123):
                                    return u'1'
                            if (data['field26'] <= 0.24422):
                                if (data.get('field24') is None):
                                    return u'1'
                                if (data['field24'] > 0.28055):
                                    return u'0'
                                if (data['field24'] <= 0.28055):
                                    return u'1'
                        if (data['field21'] <= 0.00556):
                            if (data.get('field9') is None):
                                return u'1'
                            if (data['field9'] > 0.00252):
                                if (data.get('field8') is None):
                                    return u'1'
                                if (data['field8'] > 0.00084):
                                    return u'1'
                                if (data['field8'] <= 0.00084):
                                    if (data.get('field6') is None):
                                        return u'1'
                                    if (data['field6'] > 6e-05):
                                        return u'1'
                                    if (data['field6'] <= 6e-05):
                                        if (data.get('field10') is None):
                                            return u'0'
                                        if (data['field10'] > 0.01735):
                                            return u'1'
                                        if (data['field10'] <= 0.01735):
                                            return u'0'
                            if (data['field9'] <= 0.00252):
                                if (data.get('field6') is None):
                                    return u'0'
                                if (data['field6'] > 0.00095):
                                    if (data['field6'] > 0.00771):
                                        if (data.get('field27') is None):
                                            return u'0'
                                        if (data['field27'] > 0.01402):
                                            return u'0'
                                        if (data['field27'] <= 0.01402):
                                            return u'1'
                                    if (data['field6'] <= 0.00771):
                                        return u'1'
                                if (data['field6'] <= 0.00095):
                                    if (data.get('field4') is None):
                                        return u'0'
                                    if (data['field4'] > 1e-05):
                                        return u'1'
                                    if (data['field4'] <= 1e-05):
                                        return u'0'
                if (data['field7'] <= 0.00082):
                    if (data.get('field6') is None):
                        return u'0'
                    if (data['field6'] > 0.00027):
                        if (data.get('field22') is None):
                            return u'1'
                        if (data['field22'] > 0.00041):
                            if (data.get('field5') is None):
                                return u'1'
                            if (data['field5'] > 0.0001):
                                if (data['field7'] > 0.00071):
                                    return u'0'
                                if (data['field7'] <= 0.00071):
                                    return u'1'
                            if (data['field5'] <= 0.0001):
                                if (data.get('field10') is None):
                                    return u'1'
                                if (data['field10'] > 0.00232):
                                    return u'1'
                                if (data['field10'] <= 0.00232):
                                    return u'0'
                        if (data['field22'] <= 0.00041):
                            if (data.get('field10') is None):
                                return u'0'
                            if (data['field10'] > 5e-05):
                                if (data.get('field18') is None):
                                    return u'1'
                                if (data['field18'] > 0.00116):
                                    return u'1'
                                if (data['field18'] <= 0.00116):
                                    return u'0'
                            if (data['field10'] <= 5e-05):
                                return u'0'
                    if (data['field6'] <= 0.00027):
                        if (data.get('field10') is None):
                            return u'0'
                        if (data['field10'] > 0.00024):
                            if (data.get('field11') is None):
                                return u'0'
                            if (data['field11'] > 0.0003):
                                if (data.get('field27') is None):
                                    return u'1'
                                if (data['field27'] > 0.06032):
                                    return u'0'
                                if (data['field27'] <= 0.06032):
                                    return u'1'
                            if (data['field11'] <= 0.0003):
                                if (data.get('field15') is None):
                                    return u'0'
                                if (data['field15'] > 0.05491):
                                    return u'1'
                                if (data['field15'] <= 0.05491):
                                    return u'0'
                        if (data['field10'] <= 0.00024):
                            if (data.get('field8') is None):
                                return u'0'
                            if (data['field8'] > 0.00271):
                                if (data.get('field11') is None):
                                    return u'0'
                                if (data['field11'] > 0.00045):
                                    return u'1'
                                if (data['field11'] <= 0.00045):
                                    return u'0'
                            if (data['field8'] <= 0.00271):
                                return u'0'
            if (data['field17'] <= 0.00359):
                if (data['field13'] > 0.00011):
                    if (data.get('field10') is None):
                        return u'0'
                    if (data['field10'] > 0.0005):
                        if (data.get('field18') is None):
                            return u'1'
                        if (data['field18'] > 0.00088):
                            if (data.get('field26') is None):
                                return u'1'
                            if (data['field26'] > 0.15318):
                                if (data.get('field27') is None):
                                    return u'0'
                                if (data['field27'] > 0.36916):
                                    return u'1'
                                if (data['field27'] <= 0.36916):
                                    return u'0'
                            if (data['field26'] <= 0.15318):
                                if (data.get('field28') is None):
                                    return u'1'
                                if (data['field28'] > 0.21189):
                                    return u'0'
                                if (data['field28'] <= 0.21189):
                                    return u'1'
                        if (data['field18'] <= 0.00088):
                            if (data.get('field15') is None):
                                return u'0'
                            if (data['field15'] > 0.00049):
                                if (data.get('field21') is None):
                                    return u'1'
                                if (data['field21'] > 0.00045):
                                    if (data.get('field3') is None):
                                        return u'1'
                                    if (data['field3'] > 5e-05):
                                        return u'1'
                                    if (data['field3'] <= 5e-05):
                                        if (data.get('field19') is None):
                                            return u'1'
                                        if (data['field19'] > 0.00102):
                                            return u'1'
                                        if (data['field19'] <= 0.00102):
                                            return u'0'
                                if (data['field21'] <= 0.00045):
                                    return u'0'
                            if (data['field15'] <= 0.00049):
                                if (data.get('field1') is None):
                                    return u'0'
                                if (data['field1'] > 5e-05):
                                    if (data.get('field19') is None):
                                        return u'0'
                                    if (data['field19'] > 0.00127):
                                        return u'1'
                                    if (data['field19'] <= 0.00127):
                                        if (data['field10'] > 0.01052):
                                            return u'0'
                                        if (data['field10'] <= 0.01052):
                                            if (data['field19'] > 8e-05):
                                                return u'1'
                                            if (data['field19'] <= 8e-05):
                                                return u'0'
                                if (data['field1'] <= 5e-05):
                                    return u'0'
                    if (data['field10'] <= 0.0005):
                        if (data.get('field1') is None):
                            return u'0'
                        if (data['field1'] > 0.0003):
                            if (data.get('field25') is None):
                                return u'1'
                            if (data['field25'] > 0.00896):
                                if (data.get('field7') is None):
                                    return u'1'
                                if (data['field7'] > 1e-05):
                                    if (data.get('field24') is None):
                                        return u'1'
                                    if (data['field24'] > 0.21982):
                                        return u'0'
                                    if (data['field24'] <= 0.21982):
                                        return u'1'
                                if (data['field7'] <= 1e-05):
                                    if (data.get('field6') is None):
                                        return u'1'
                                    if (data['field6'] > 0.00012):
                                        if (data.get('field3') is None):
                                            return u'1'
                                        if (data['field3'] > 6e-05):
                                            return u'1'
                                        if (data['field3'] <= 6e-05):
                                            return u'0'
                                    if (data['field6'] <= 0.00012):
                                        return u'0'
                            if (data['field25'] <= 0.00896):
                                if (data.get('field20') is None):
                                    return u'0'
                                if (data['field20'] > 0.00031):
                                    if (data.get('field11') is None):
                                        return u'1'
                                    if (data['field11'] > 0.00158):
                                        return u'1'
                                    if (data['field11'] <= 0.00158):
                                        return u'0'
                                if (data['field20'] <= 0.00031):
                                    return u'0'
                        if (data['field1'] <= 0.0003):
                            if (data['field1'] > 1e-05):
                                if (data.get('field7') is None):
                                    return u'0'
                                if (data['field7'] > 1e-05):
                                    if (data.get('field23') is None):
                                        return u'1'
                                    if (data['field23'] > 0.02857):
                                        if (data.get('field28') is None):
                                            return u'0'
                                        if (data['field28'] > 0.02828):
                                            if (data.get('field11') is None):
                                                return u'1'
                                            if (data['field11'] > 0.00519):
                                                return u'0'
                                            if (data['field11'] <= 0.00519):
                                                return u'1'
                                        if (data['field28'] <= 0.02828):
                                            return u'0'
                                    if (data['field23'] <= 0.02857):
                                        return u'1'
                                if (data['field7'] <= 1e-05):
                                    if (data.get('field8') is None):
                                        return u'0'
                                    if (data['field8'] > 1e-05):
                                        if (data.get('field19') is None):
                                            return u'0'
                                        if (data['field19'] > 0.00011):
                                            return u'1'
                                        if (data['field19'] <= 0.00011):
                                            return u'0'
                                    if (data['field8'] <= 1e-05):
                                        return u'0'
                            if (data['field1'] <= 1e-05):
                                if (data.get('field6') is None):
                                    return u'0'
                                if (data['field6'] > 0.00017):
                                    if (data.get('field18') is None):
                                        return u'0'
                                    if (data['field18'] > 0.00017):
                                        if (data.get('field15') is None):
                                            return u'1'
                                        if (data['field15'] > 5e-05):
                                            if (data.get('field27') is None):
                                                return u'1'
                                            if (data['field27'] > 0.15803):
                                                return u'0'
                                            if (data['field27'] <= 0.15803):
                                                return u'1'
                                        if (data['field15'] <= 5e-05):
                                            if (data['field10'] > 1e-05):
                                                return u'1'
                                            if (data['field10'] <= 1e-05):
                                                return u'0'
                                    if (data['field18'] <= 0.00017):
                                        return u'0'
                                if (data['field6'] <= 0.00017):
                                    if (data['field10'] > 1e-05):
                                        if (data['field6'] > 1e-05):
                                            if (data['field6'] > 8e-05):
                                                return u'0'
                                            if (data['field6'] <= 8e-05):
                                                return u'1'
                                        if (data['field6'] <= 1e-05):
                                            return u'0'
                                    if (data['field10'] <= 1e-05):
                                        return u'0'
                if (data['field13'] <= 0.00011):
                    if (data.get('field18') is None):
                        return u'0'
                    if (data['field18'] > 0.00127):
                        if (data.get('field8') is None):
                            return u'0'
                        if (data['field8'] > 0.00035):
                            if (data.get('field20') is None):
                                return u'0'
                            if (data['field20'] > 0.00265):
                                if (data.get('field21') is None):
                                    return u'1'
                                if (data['field21'] > 0.00045):
                                    if (data.get('field25') is None):
                                        return u'1'
                                    if (data['field25'] > 0.17946):
                                        return u'0'
                                    if (data['field25'] <= 0.17946):
                                        return u'1'
                                if (data['field21'] <= 0.00045):
                                    if (data.get('field15') is None):
                                        return u'0'
                                    if (data['field15'] > 5e-05):
                                        if (data.get('field19') is None):
                                            return u'1'
                                        if (data['field19'] > 0.04897):
                                            return u'0'
                                        if (data['field19'] <= 0.04897):
                                            return u'1'
                                    if (data['field15'] <= 5e-05):
                                        return u'0'
                            if (data['field20'] <= 0.00265):
                                if (data.get('field27') is None):
                                    return u'0'
                                if (data['field27'] > 0.0102):
                                    if (data.get('field26') is None):
                                        return u'0'
                                    if (data['field26'] > 0.00289):
                                        if (data['field27'] > 0.10153):
                                            return u'0'
                                        if (data['field27'] <= 0.10153):
                                            if (data['field26'] > 0.08454):
                                                return u'0'
                                            if (data['field26'] <= 0.08454):
                                                return u'1'
                                    if (data['field26'] <= 0.00289):
                                        return u'0'
                                if (data['field27'] <= 0.0102):
                                    return u'0'
                        if (data['field8'] <= 0.00035):
                            if (data.get('field4') is None):
                                return u'0'
                            if (data['field4'] > 1e-05):
                                if (data.get('field9') is None):
                                    return u'0'
                                if (data['field9'] > 1e-05):
                                    if (data.get('field19') is None):
                                        return u'1'
                                    if (data['field19'] > 0.00998):
                                        return u'0'
                                    if (data['field19'] <= 0.00998):
                                        return u'1'
                                if (data['field9'] <= 1e-05):
                                    if (data.get('field12') is None):
                                        return u'0'
                                    if (data['field12'] > 0.03801):
                                        return u'1'
                                    if (data['field12'] <= 0.03801):
                                        return u'0'
                            if (data['field4'] <= 1e-05):
                                return u'0'
                    if (data['field18'] <= 0.00127):
                        if (data.get('field19') is None):
                            return u'0'
                        if (data['field19'] > 0.00102):
                            if (data.get('field2') is None):
                                return u'0'
                            if (data['field2'] > 7e-05):
                                if (data.get('field12') is None):
                                    return u'0'
                                if (data['field12'] > 0.00026):
                                    if (data['field19'] > 0.00168):
                                        if (data.get('field28') is None):
                                            return u'1'
                                        if (data['field28'] > 0.00041):
                                            return u'1'
                                        if (data['field28'] <= 0.00041):
                                            if (data.get('field6') is None):
                                                return u'0'
                                            if (data['field6'] > 2e-05):
                                                return u'1'
                                            if (data['field6'] <= 2e-05):
                                                return u'0'
                                    if (data['field19'] <= 0.00168):
                                        return u'0'
                                if (data['field12'] <= 0.00026):
                                    return u'0'
                            if (data['field2'] <= 7e-05):
                                if (data.get('field11') is None):
                                    return u'0'
                                if (data['field11'] > 0.00544):
                                    if (data.get('field9') is None):
                                        return u'0'
                                    if (data['field9'] > 0.00033):
                                        return u'1'
                                    if (data['field9'] <= 0.00033):
                                        return u'0'
                                if (data['field11'] <= 0.00544):
                                    if (data['field18'] > 0.00069):
                                        if (data.get('field6') is None):
                                            return u'0'
                                        if (data['field6'] > 8e-05):
                                            return u'1'
                                        if (data['field6'] <= 8e-05):
                                            return u'0'
                                    if (data['field18'] <= 0.00069):
                                        return u'0'
                        if (data['field19'] <= 0.00102):
                            if (data['field17'] > 0.00064):
                                if (data.get('field5') is None):
                                    return u'0'
                                if (data['field5'] > 5e-05):
                                    if (data.get('field15') is None):
                                        return u'0'
                                    if (data['field15'] > 0.00086):
                                        if (data.get('field6') is None):
                                            return u'1'
                                        if (data['field6'] > 0.00024):
                                            return u'1'
                                        if (data['field6'] <= 0.00024):
                                            return u'0'
                                    if (data['field15'] <= 0.00086):
                                        return u'0'
                                if (data['field5'] <= 5e-05):
                                    return u'0'
                            if (data['field17'] <= 0.00064):
                                if (data.get('field12') is None):
                                    return u'0'
                                if (data['field12'] > 0.01162):
                                    return u'0'
                                if (data['field12'] <= 0.01162):
                                    return u'0'

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
            true_result = int(sample[30])

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

def tiempoDeteccionZeroDays():
    zeroDay_files = glob.glob("zeroDays_notFiltered/*.csv")
    tiemposDeteccion = {}
    tiempoDeteccion = 0
    maxTiempoDeteccion = 0
    tiempoDeteccionAcumulado = 0
    truePositivos = 0
    for file in zeroDay_files:
        zeroDay_samples = loadtxt(file,delimiter=',',usecols=range(_T*3+2))
        tiempoDeteccion = 0
        alarmasSeguidas = 0
        positivosSample = 0
        for sample in zeroDay_samples:
            input_sample={}
            for i in range(0,len(sample)-2):
                indice = int(i+1)
                field = str('field'+str(indice))
                input_sample[field]=float(sample[i])

            prediction_result = deepnet.predict(input_sample, full=True)
            json_result = json.loads(json.dumps(prediction_result))
            true_result = int(sample[_T*3])
            timestamp = int(sample[_T*3+1])


            if (int(json_result["prediction"]) == 1 and true_result == 1):
                alarmasSeguidas+=1
                tiempoDeteccion+=_T
                
                if (alarmasSeguidas == _REDES):
                    timestampDeteccion = timestamp
                    print ("%s --- %i" % (file,timestamp))
                    break

##################################################################################
##########################---FLUJO DEL PROGRAMA---################################
##################################################################################
_FILE=sys.argv[1]
_REDES=int(sys.argv[2])
start_allTime = time.time()
_T=10
_FILE_TDETECCION="tDeteccion_tree.txt"
caracteristicas = int(_T*3)+1

if (_FILE == "ransomwareIndividuales"):
    ransomwareIndividuales()
    sys.exit()

if (_FILE == "tiempoDeteccionZeroDays"):
    tiempoDeteccionZeroDays()
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
for t in sorted(tiemposDeteccion.keys(), key=lambda item: item[0]):
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