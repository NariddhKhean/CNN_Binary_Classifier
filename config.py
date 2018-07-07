import os


### WEB SCRAPE ###

# Search Terms
search_terms_a = ["apples", "apple"]
search_terms_b = ["oranges", "orange"]

# Output Directores
user_path = os.path.expanduser("~")
data_path = os.path.join(user_path, "Desktop", "data")
output_dir_a = os.path.join(data_path, search_terms_a[0])
output_dir_b = os.path.join(data_path, search_terms_b[0])

# File Format
file_format = "jpg"

# Scrape Limit
scrape_limit = 20


### DATASET DIVISION ###

# Training/Division Ratio
training_factor = 0.6


### CNN HYPERPARAMETERS ###

# TODO
