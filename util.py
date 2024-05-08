import numpy as np
def mathew_correlation_coefficient(metrics_dict):
    PPV = metrics_dict['PPV']
    TPR = metrics_dict['TPR']
    TNR = metrics_dict['TNR']
    NPV = metrics_dict['NPV']

    FDR = metrics_dict['FDR']
    FNR = metrics_dict['FNR']
    FPR = metrics_dict['FPR']
    FOR = metrics_dict['FOR']

    return np.sqrt(PPV*TPR*TNR*NPV) - np.sqrt(FDR*FNR*FPR*FOR)

def f1_score(metrics_dict):
    precision = metrics_dict['PPV']
    recall = metrics_dict['TPR']

    if (precision + recall) > 0:
        return 2*(precision*recall)/(precision+recall)
    return 0