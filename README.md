# movie-gender-sentiment-analysis
Project for CSE 583, autumn 2018.

[movie_analysis](https://github.com/tmaxdillon/movie-gender-sentiment-analysis/tree/master/movie_analysis) folder contains the python codes for the entire process. 

## Comment Extraction: 
Use [comment_downloader.py](https://github.com/tmaxdillon/movie-gender-sentiment-analysis/blob/master/movie_analysis/comment_downloader.py) to download comments from each movie trailer.
Input: csv file containing (youtube_id, movie_id)s. The header name should be "youtube_id" and "movie_id"
Output: {movie_id}.csv which contains all the comments from each movie's trailer

### Usage 
From terminal
```bash
python comment_downloader.py input.csv
```
From another python code
```python
from comment_downloader import download_from_the_list

download_from_the_list(input) #input should be a pandas dataframe with the columns "youtube_id" and "movie_id"
```

