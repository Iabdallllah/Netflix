import pandas as pd
# Load the dataset
netflix_data = pd.read_csv('netflix_data.csv')

# Filter movies from the 1990s
movies_90s = netflix_data[(netflix_data['release_year'] >= 1990) & (netflix_data['release_year'] < 2000)]

# Find the most frequent movie duration in the 1990s
duration = movies_90s['duration'].mode()[0]

# Count the number of short action movies released in the 1990s
short_movie_count = len(movies_90s[(movies_90s['duration'] < 90) & (movies_90s['genre'] == 'Action')])

# Print the results
print(f"Most frequent movie duration in the 1990s: {duration} minutes")
print(f"Number of short action movies released in the 1990s: {short_movie_count}")
