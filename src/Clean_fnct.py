import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import statistics 
import src.Clean_fnct as clean
import requests
from bs4 import BeautifulSoup




def clean_listing(stay):
    
    # We consider the next columns not relevant.
    
    stay = stay.drop(['minimum_nights', 'last_review', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365'], axis = 1 )
    

    stay.isnull().sum().sort_values(ascending=False)
    
    # Sum and remove null values.
    
    stay.dropna()
    
    # Remove duplicates.
    
    stay.drop_duplicates()
    


    # Remove special characters in districts and neighbourhoods.
    
def vowels(nombre):
    if 'Ã¡' in nombre:
        return nombre.replace('Ã¡','á')
    elif 'Ã©' in nombre:
        return nombre.replace('Ã©','é')
    elif 'Ã\xad' in nombre: 
        return nombre.replace('Ã\xad','í')
    elif 'Ã³'in nombre:
        return nombre.replace('Ã³','ó')
    elif 'Ãº'in nombre:
        return nombre.replace('Ãº', 'ú')
    elif 'Ã¼' in nombre:
        return nombre.replace('Ã¼','ü')
    else:
        return nombre
    
