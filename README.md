# Berlin flat pricing prediction

Fun DS project trying to predict Berlin flat rental pricing (It is obsolete, but I want to try the knowledge anyway).

## Background

I was trying to find a flat in Berlin. Out of boredome and luck that I found the cool project from https://github.com/diogomatoschaves/berlin-house-prices-analysis. That's why I want to use what I've learned recently and apply to the dataset. This project involves some funny investigation of a few flat properties/features for the Berlin rental housing market (year 2019).

## Libraries used

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- keras (but I can't use it currently as it kills my anaconda kernel)

## Dataset

The dataset used for the analysis can be found in the file `berlin-houses.csv` that I downloaded gracefully from https://github.com/diogomatoschaves/berlin-house-prices-analysis

The features of this dataset are:

- `id` - id of listing
- `lat` - latitude of the listing
- `lon` - longitude of the listing
- `cold_price` - price of the listing before heating and upkeep costs
- `warm_price` - price of the listing after heating and upkeep costs
- `currency` - currency of the listing prices
- `short_listed` - if a given listing has short listed candidates
- `postcode_id` - post code of the listing
- `balcony` - if a listing has a balcony
- `builtin_kitchen` - if a listing has a built-in kitchen
- `created_date` - date the listing was created
- `modified_date` - date the listing was modified
- `published_date` - date the listing was published
- `energy_certificate` - if a listing has an energy certificate
- `has_new_flag` - if a listing is a new build or has been renovated recently.
- `living_space` - the living area in squared meters (m2)
- `new_home_builder` - if a listing has been built by new building company
- `number_rooms` - total number of rooms in listing
- `private_offer` - if a listing is pusblished by private owner
- `address` - address of the listing
- `link` - link to listing page
- `quarter` - district where listing is located
- `garden` - if a listing has a garden
- `listing_type` - listing size category
- `localhost_date` - date when listing data was saved into database
- `no_longer_available` - if listing is no longer available in website
- `no_longer_available_date` - date when listing was no longer available on the website

## Steps to approach the project

1. Preprosess data i.e. PCA finding the make-sense features,
2. EDA the cleansed dataset
3. Modeling
4. Model evaluation
5. Serve the model using FastAPI - still on the to do list
6. Deploy model to streamlit or Heroku - still on the to do list
