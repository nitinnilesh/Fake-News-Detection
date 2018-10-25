import pandas as pd
import re
import pdb
from nltk import word_tokenize

############ VERSION1 ##############################
# # Pattern to clean apostrophes
# quotePattern = re.compile("[']")
# # Pattern to remove special characters
# specCharsPattern = re.compile("[^A-Za-z0-9' ]")


# def clean(text):
#     if not pd.isnull(text):
#         text = re.sub(quotePattern, "", text)
#         text = re.sub(specCharsPattern, " ", text)
#         tokens = word_tokenize(text.lower())
#         filtered_text = ""
#         for w in tokens:
#             filtered_text += w + " "
#         return filtered_text[:-1]
#     else:
#         return None


# data = pd.read_csv('news_scrap_final.csv', header=0)
# clean_data = pd.DataFrame(columns=['HEADING', 'Real/Fake'])

# for i, row in data.iterrows():
#     heading = clean(row['HEADING'])
#     if heading and row['Real/Fake']:
#         clean_data = clean_data.append({'HEADING': heading, 'Real/Fake': row['Real/Fake']}, ignore_index=True)

# clean_data.dropna(how='any')
# clean_data.to_csv('news_data_final2.csv', encoding='utf-8', index=False)
############ VERSION1 ##############################

############ VERSION2 ##############################

# Pattern to clean apostrophes
quotePattern = re.compile("[']")
# Pattern to remove special characters
specCharsPattern = re.compile("[^A-Za-z0-9' ]")


def clean(text):
    if not pd.isnull(text):
        text = text.lower()
        text = re.sub(quotePattern, "", text)
        text = re.sub(specCharsPattern, " ", text)
        text = ' '.join([i for i in word_tokenize(text)])
        text = text.replace(r'[^\.\w\s]','')
        text = text.replace(r'\.\.+','.')
        text = text.replace(r'\.',' . ')
        text = text.replace(r'\s\s+',' ')
        text = text.strip()
        return text
    else:
        return None


data = pd.read_csv('news_scrap_final.csv', header=0)
clean_data = pd.DataFrame(columns=['title', 'text', 'label'])

for i, row in data.iterrows():
    heading = clean(row['HEADING'])
    body = clean(row['BODY'])
    if heading and body and row['Real/Fake']:
        clean_data = clean_data.append({'title': heading, 'text': body, 'label': row['Real/Fake']}, ignore_index=True)

clean_data.dropna(how='any')
clean_data.to_csv('news_data_final2.csv', encoding='utf-8', index=False)

############ VERSION2 ##############################