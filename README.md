# -W3-pipelines-project-

![madrid](https://user-images.githubusercontent.com/80899361/114438783-7e520100-9bc8-11eb-9927-cdb85ac0dd5f.png)


# Introduction
What are the most popular monuments near you (Madrid)?

# Purpose
This is the second project I do at Ironhack and the purpose of this analysis is to find out which are the most popular monuments near where you are staying in Madrid.

We have conducted the research out of a dataset we've downloaded from Kaggle named 'listings.csv'.

# Method
We have chosen a database of a well-known online marketplace that connects people who want to rent out their homes with people who are looking for accommodations in that locale. The database has over 20 thousand rows and 16 columns. Within the database we can see several apartments in Madrid, with its prices, location and room types within others. 

Steps:

- Dataset analysis and cleaning: firstly, we analyse the dataset, observe the columns and decide which ones are relevant and which are not. Although the dataset is pretty clean, some columns are redundant. After this, every null values and duplicates are removed from the dataset. We name this jupyter as Clean_listing.ipynb.

- Web scraping: once we have a clean dataset, we use web scraping to add additional and useful information to our dataset with popular monuments in Madrid. We use Nominatim from geopy.geocoders library. We name this document Web_scrapping_listing.

- Visualization: We use the pricings and the districts to make visual graphs.

# Conclusions

- The districts where most appartments are being rented are: Centro, Salamanca y Chamberí.

![top3d](https://user-images.githubusercontent.com/80899361/114438980-bd805200-9bc8-11eb-8b41-e40e05dc1531.png)

- Most of the appartments are in concurred areas of Madrid: Malasaña, Barrio de las Letras y el Estadio Santiago Bernabeu.


# Libraries

 - numpy
 - pandas
 - matplotlib.pyplot
 - seaborn
 - statistics 
 - requests
 - pandas
 - json
 - BeautifulSoup

