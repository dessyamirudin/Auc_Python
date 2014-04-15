'''
Created on 15 Apr 2014

@author: Dessy Amirudin
'''
import numpy as np
import xlrd
from sklearn import metrics

def readxlsx(inputfile):
    workbook=xlrd.open_workbook(inputfile)
    sheetnames=workbook.sheet_names()
    worksheet=workbook.sheet_by_name(sheetnames[0])
    num_rows=worksheet.nrows-1
    #num_cells=worksheet.ncols-1
    curr_rows=0
    score=[]
    act_class=[]
    while curr_rows<num_rows:
        curr_rows+=1
        #row=worksheet.row(curr_rows)
        score.append(worksheet.cell_value(curr_rows,0))
        act_class.append(worksheet.cell_value(curr_rows,1)+1)
    return np.concatenate((np.array([score]),np.array([act_class])),axis=0)
    
def main():
    '''Sorted data'''
    inputsorted='german-sorted.xlsx'
    datasorted=readxlsx(inputsorted)
    score_sorted=datasorted[0,:]
    act_class_sorted=datasorted[1,:]
        
    '''calculating ROC AUC'''
    fpr_sorted,tpr_sorted,thresholds_sorted=metrics.roc_curve(act_class_sorted,score_sorted,pos_label=2)
    aucvalue_sorted=metrics.auc(fpr_sorted,tpr_sorted)
    print 'AUC value of sorted data'
    print aucvalue_sorted
    #print 'Threshold'
    #print thresholds_sorted
    print ''
    
    '''Unsorted data'''
    inputunsorted='german-unsorted.xlsx'
    dataunsorted=readxlsx(inputunsorted)
    score_unsorted=dataunsorted[0,:]
    act_class_unsorted=dataunsorted[1,:]
        
    '''calculating ROC AUC'''
    fpr_unsorted,tpr_unsorted,thresholds_unsorted=metrics.roc_curve(act_class_unsorted,score_unsorted,pos_label=2)
    aucvalue_unsorted=metrics.auc(fpr_unsorted,tpr_unsorted)
    print 'AUC value of sorted data'
    print aucvalue_unsorted
    #print 'Threshold'
    #print thresholds_unsorted    

if __name__=='__main__':
    main()