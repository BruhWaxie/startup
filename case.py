#місце для твого коду
import pandas as pd

df = pd.read_csv('investments_VC.csv')


def clean_data(data):
    if data.strip() != '-':
        result = data.replace(',', '')
        return int(result)
    else:
        return 0

df['funding_total_usd'] = df['funding_total_usd'].apply(clean_data)
df.info()

def clean_cata(category_list):
    if isinstance(category_list, str):
        if category_list.strip() != '':
            category_list=category_list.split('|')
            return category_list[0]
        else:
            return "Other"


df['category_list'] = df['category_list'].apply(clean_cata)


def clean_name(name):
    if isinstance(name, str):
        if name.strip() == '':
            return 'Unknown'
    else:
        return 'Unknown'

def clean_url(url):
    if isinstance(url, str):
        if url.strip() == '':
            return 'No homepage url'
    else:
        return "No homepage url"
df['name'] = df['name'].apply(clean_name)
df['homepage_url'] = df['homepage_url'].apply(clean_url)

df.info()
df.to_csv('cleaned.csv', index=False)