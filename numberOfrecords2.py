import pandas as pd  # Handles CSV reading


filenames = [ 
    'data/credits.csv',
    'data/keywords.csv',
    'data/links_small.csv',  # Can't read it
    'data/links.csv',
    'data/movies_metadata.csv',
    'data/ratings_small.csv',
    'data/ratings.csv'
]


total_records = 0

# loop over files and sum the number of records
for file in filenames:
    try:
        df = pd.read_csv(file)  # Read the CSV file
        num_records = len(df)  # Get the number of records 'number'
        total_records += num_records 
        # Print the number 
        print(file + " has " + str(num_records) + " records.") #in py concat needs to be all str
    except Exception as e:
   
        print("Could not read " + file + ": " + str(e))

# Print the total number of records across all files
print("The total number of records across all files is " + str(total_records) + ".")

