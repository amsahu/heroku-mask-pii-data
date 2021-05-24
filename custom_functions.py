import pandas as pd

def create_df(filename:str,filetype:int):
    
    """Creates df, filetype = 1 for csv, filetype = 2 for xlsx"""
    
    if filetype==1:
        return pd.read_csv(filename, dtype=str)
    elif filetype==2:
        return pd.read_excel(filename, dtype=str)
    else:
        return -1

##################################################################


def predict_label(data_ls, model):
    
    """takes test data in df format and 
    predict entity using model and return df with result"""
    
    if len(data_ls)>0:
        
        email=0
        phone=0
        addr=0
        none=0

        for data in data_ls:
            doc = model(data)
            l=[(X.text, X.label_) for X in doc.ents]
            if len(l)>0:
                if l[0][1]=='EMAIL':
                    email+=1
                elif l[0][1]=='PHONE':
                    phone+=1
                else:
                    addr+=1
            else:
                none+=1            
        return {'EMAIL':email,'PHONE':phone,'ADDR':addr,'NONE':none}
    
    else:
        return {'EMAIL':0,'PHONE':0,'ADDR':0,'NONE':1}


#########################################################################


def get_indices(df:pd.DataFrame,model):
    
    """fetch indices of PII data"""
    
    email_id=[]
    phone_id=[]
    addr_id=[]

    for i in range(df.shape[1]):
        ls = list(df.iloc[:,i].dropna())
        a_dictionary = predict_label(ls,model)
        entity = max(a_dictionary, key=a_dictionary.get)
        if entity=='EMAIL':
            email_id.append(i)
        elif entity=='PHONE':
            phone_id.append(i)
        elif entity=='ADDR':
            addr_id.append(i)
        else:
            continue

    return {'EMAIL':email_id,'PHONE':phone_id,'ADDR':addr_id}



#######################################################################


def mask_data(df:pd.DataFrame, indices:dict, masking_rule):
    
    """ takes df and indices of PII data as dictionary and return df after masking"""
    
    for key, val in indices.items():
        if key=='EMAIL':
            for v in val:
                df.iloc[:,v]=df.iloc[:,v].apply(masking_rule)
        elif key=='PHONE':
            for v in val:
                df.iloc[:,v]=df.iloc[:,v].apply(masking_rule)
        else:
            for v in val:
                df.iloc[:,v]=df.iloc[:,v].apply(masking_rule)
    return df

