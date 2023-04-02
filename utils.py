import pandas as pd, numpy as np
from scipy import stats
import re, pickle, json, sklearn

classifier = pickle.load(open('models/rf_1.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer_1.pkl', 'rb'))


def clean_sheet(sheet):
    #clean nan cols and rows
    sheet = sheet.dropna(how='all', axis=1).dropna(how='all', axis=0)
    #most frequent row nans pattern
    mode = stats.mode(sheet.isna().sum(axis=1), keepdims=True)[0][0]
    #assuming this as where to scrap data
    data = pd.concat([row for _, row in sheet.iterrows() if row.isna().sum() == mode], axis=1).T

    valid_data = pd.concat(
        [
            col for _, col in data.items() 
            if col.isna().sum() < len(col)*0.1
        ], 
    axis=1).reset_index()

    return valid_data


def data_scraping(sheet, doc_type):
    
    valid_data = clean_sheet(sheet).astype(str)
    
    # EXTRACT ACCOUNTING FIELDS
    fields_pattern = r'[^0-9\.,-]+' if doc_type == 2 else r'\D+'

    fields = []
    strings = valid_data.applymap(lambda x: re.findall(fields_pattern, x)) #[^0-9\.,-]
    for _, col in strings.items():
        # check valid columns
        if col.tolist().count([]) < len(col):
            for row in col:
                if len(row) > 0:
                    fields.extend(row)

    # EXTRACT FIELDS VALUE
    all_values = []
    numbers = valid_data.applymap(lambda x: re.findall(r'\d+', x))
    for _, col in numbers.items():
        values = []
        # check valid columns
        if col.tolist().count([]) < len(col):
            for row in col:
                if len(row) > 1:
                    try:
                        decimal = float( int(row[-1])/100 )
                        integer = int(''.join(row[:-1]))
                        values.append(integer + decimal)
                    except:
                        pass
                else:
                    values.append(np.nan)
        if len(values) > 0:    
            all_values.append(values)

    if doc_type == 1:
        data = pd.DataFrame(data=[fields, *all_values]).T
    
    elif doc_type == 2:
        data = pd.DataFrame(data=[fields, *all_values]).T

    return data.dropna(how='all', axis=1)

# data_scraping(dre_test, 1).head(50)
# data_scraping(balan_test, 2).head(50)
def vectorize_csv(df, vectorizer, only_strings=False):
    
    if isinstance(df, np.ndarray): df = pd.DataFrame(df)

    if only_strings is True:
        is_word = r'[A-Za-z\s]+'
        words = []
        for column in df.select_dtypes(include=['object']):
            for cell in df[column]:
                if isinstance(cell, str):
                    matches = re.findall(is_word, cell)
                    words.extend(matches)
        text = ' '.join(words)
    else:
        flatten = df.astype(str).values.flatten()
        text = ' '.join(flatten)
    # Fit the vectorizer with a 1-D array, only if it has not been fitted before
    if not hasattr(vectorizer, 'vocabulary_'):
        vectorizer.fit([text])
    # Transforming text placed in a 2-D array using the transform method
    vector=[]
    # vectorize many
    if len(df.columns) == 1:
        for doc in df.iloc[:, 0]:
            vec = vectorizer.transform([doc]).toarray()
            vector.extend(vec)
    # vectorize only one document
    else:
        vec = vectorizer.transform([text]).toarray()
        vector.extend(vec)
    vector=np.array(vector)

    if not hasattr(vectorizer, 'vocabulary_'):
        return vector, vectorizer
    return vector

