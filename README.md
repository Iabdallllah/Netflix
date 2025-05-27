# Netflix 1990s Movies Data Analysis

This project performs exploratory data analysis (EDA) on a sample Netflix dataset to answer questions about movies from the 1990s.

## Files
- `netflix_data.csv`: Sample dataset containing Netflix movie data, including release year, duration, genre, and more.
- `test.py`: Python script that loads the dataset and computes:
  - The most frequent movie duration in the 1990s (as `duration`)
  - The number of short action movies (<90 minutes) released in the 1990s (as `short_movie_count`)

## How to Run
1. Make sure you have Python 3 and `pandas` installed. You can install pandas with:
   ```sh
   pip install pandas
   ```
2. Place both `test.py` and `netflix_data.csv` in the same directory.
3. Run the script:
   ```sh
   python test.py
   ```

## Output
The script will print:
- The most frequent movie duration in the 1990s
- The number of short action movies released in the 1990s

## Example Output
```
Most frequent movie duration in the 1990s: 95 minutes
Number of short action movies released in the 1990s: 3
```

## Notes
- The dataset provided is a sample and can be replaced with a larger or real Netflix dataset for more comprehensive analysis.
- The script assumes the `duration` column is in minutes and the `genre` column contains the movie genre.
