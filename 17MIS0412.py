import pandas as pd
path=r"C:\Users\Rajeev\Desktop\main.csv"
data=pd.read_csv(path)
newdata=data.loc[data['COUNTRY'].str.contains('USA')]
newdata.to_csv('filteredCountry.csv',index=False);
new_data = newdata[['SKU','PRICE']]

def clean_currency(x):
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', '').replace('?', ''))
    return(x)

new_data['PRICE'] = new_data['PRICE'].apply(clean_currency).astype('float')
new_data.to_csv('modified_filtered_country.csv',index=False)

first_and_second_min_prices = pd.read_csv(r"C:\Users\Rajeev\Desktop\modified_filtered_country.csv")
first_and_second_min_prices.head()
temp_data = first_and_second_min_prices.sort_values(['SKU','PRICE']).groupby('SKU').nth(1)
temp_data['FIRST_MINIMUM_PRICE'] = first_and_second_min_prices.sort_values(['SKU','PRICE']).groupby('SKU').min()
temp_data['SECOND_MINIMUM_PRICE'] = first_and_second_min_prices.sort_values(['SKU','PRICE']).groupby('SKU').nth(1)
temp_data.to_csv('temp_lowest_price.csv',index_label="SKU")
df = pd.read_csv(r"C:\Users\Rajeev\Desktop\temp_lowest_price.csv")
final_data_frame = df.drop(labels='PRICE',axis='columns')
final_data_frame.to_csv('lowestPrice.csv',index=False)
