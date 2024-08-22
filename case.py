#місце для твого коду
import pandas as pd

df = pd.read_csv('investments_VC.csv')

df = df.drop(columns=['founded_at', 'founded_quarter'])
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
    else:
        return 'Other'

df['category_list'] = df['category_list'].apply(clean_cata)


def clean_name(name):
    if isinstance(name, str):
        if name.strip() == '':
            return 'Unknown'
        else:
            return name
    else:
        return 'Unknown'

def clean_url(url):
    if isinstance(url, str):
        if url.strip() == '':
            return 'No homepage url'
        else:
            return url
    else:
        return "No homepage url"

df['name'] = df['name'].apply(clean_name)
df['homepage_url'] = df['homepage_url'].apply(clean_url)

def clean_state_code(state):
    if isinstance(state, str):
        if state.strip() == '':
            return 'None'
        else:
            return state
    else:
        return "None"
df['state_code'] = df['state_code'].apply(clean_state_code)
df['country_code'] = df['country_code'].apply(clean_state_code)

df['founded_year'] = df['founded_year'].apply(clean_name)
df['founded_month'] = df['founded_month'].apply(clean_name)
df['city'] = df['city'].apply(clean_name)
df['region'] = df['region'].apply(clean_name)
df['market'] = df['market'].apply(clean_state_code)
df['status'] = df['status'].apply(clean_name)


df.info()
df.to_csv('cleaned.csv', index=False)