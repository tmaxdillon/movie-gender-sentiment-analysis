# movie-gender-sentiment-analysis
Project for CSE 583, Autumn 2018.
Group members: Eric Gomez, Kate Van Ness, Rachel Franz, Trent Dillon, Jamie Park

[movie_analysis](https://github.com/tmaxdillon/movie-gender-sentiment-analysis/tree/master/movie_analysis) folder contains the python codes for the entire process. 

## Computing Diversity Score
Use [diversity_score_module.py] (https://github.com/tmaxdillon/movie-gender-sentiment-analysis/blob/master/movie_analysis/diversity_score_module.py) to compute the diversity score of a selection of movies from IMDB data, do analytics on the dataset and extract a subset of the movies for further analysis.

### Computing Diversity Score
def computing_diversity_score
Run this function in a for loop on IMDB JSON data to extract cast and gender information for a collection of movies.
Inputs: Cast in list format (extracted from JSON), wanttoweight (bool) that toggles whether lead roles are weighted or unweighted.
Output: Diversity score of movie, Cast size of movie

### Visualize Distribution
def viz_distribution
Run this function to produce distribution visuals for cast size and gender diversity score.
Inputs: data, type of plot (cast size or gender diversity score)
Output: (if run in notebook) figure, figure saved to separate 'Figures' folder within directory

### Getting Subset
def get_subset
Run this function to retrieve a subset of the full dataset based on gender diversity score.
Inputs: dataframe (with gender diversity score added as column), number of data strata, number of movies in the subset
Output: subset dataframe

### Example
For an example/demo on how these functions can be used, refer to [create_subset_demo.ipynb] (https://github.com/tmaxdillon/movie-gender-sentiment-analysis/blob/master/movie_analysis/create_subset.ipynb) 

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
## Directory Structure

The package is organized as follows:

```bash
├── Demo.ipynb
├── LICENSE
├── README.md
├── __pycache__
│   ├── analyze_comments_tblob.cpython-36.pyc
│   ├── analyze_comments_tblob.cpython-37.pyc
│   ├── get_sentiment_score.cpython-36.pyc
│   ├── get_sentiment_score.cpython-37.pyc
│   ├── make_comments_df.cpython-36.pyc
│   └── make_comments_df.cpython-37.pyc
├── dist
│   ├── movie_analysis-1.0-py3.6.egg
│   └── movie_analysis-1.0-py3.7.egg
├── doc
│   ├── README.txt
│   └── project_management
│       ├── Component\ Specification.pdf
│       ├── Functional\ Specification.pdf
│       └── whiteboard_11-1
├── environment.yml
├── examples
│   └── correlation_visualization.ipynb
├── movie_analysis
│   ├── Demo.ipynb
│   ├── Figures
│   │   ├── Cast_Size_dist.pdf
│   │   ├── Full_Diversity_Dist.pdf
│   │   ├── linear_fit.pdf
│   │   ├── scatter.pdf
│   │   └── tmp.pdf
│   ├── Untitled.ipynb
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── analyze_comments_tblob.cpython-36.pyc
│   │   ├── analyze_comments_tblob.cpython-37.pyc
│   │   ├── diversity_score_module.cpython-36.pyc
│   │   ├── diversity_score_module.cpython-37.pyc
│   │   ├── get_YT_URL.cpython-36.pyc
│   │   ├── get_sentiment_score.cpython-36.pyc
│   │   ├── get_sentiment_score.cpython-37.pyc
│   │   ├── make_comments_df.cpython-36.pyc
│   │   ├── make_comments_df.cpython-37.pyc
│   │   ├── movie_analysis.cpython-36.pyc
│   │   ├── movie_correlation_plots.cpython-36.pyc
│   │   ├── movie_correlation_plots.cpython-37.pyc
│   │   ├── plot_functions.cpython-36.pyc
│   │   ├── plot_functions.cpython-37.pyc
│   │   ├── version.cpython-36.pyc
│   │   └── version.cpython-37.pyc
│   ├── analyze_comments_tblob.py
│   ├── comment_downloader.py
│   ├── create_subset_demo.ipynb
│   ├── data
│   │   ├── configured_data
│   │   │   └── imdb_subset_100_10strats
│   │   ├── imdb_subset_100_10strats
│   │   ├── movie_comments
│   │   │   ├── comment_files.csv
│   │   ├── raw_data
│   │   │   ├── emptydir.txt
│   │   │   ├── tmdb_5000_credits.csv
│   │   │   └── tmdb_5000_movies.csv
│   │   ├── sentiment_scores.csv
│   │   └── subsetData_withURLS.csv
│   ├── diversity_score_module.py
│   ├── download_YT_URLs.ipynb
│   ├── get_YT_URL.py
│   ├── get_YT_videoIDs.py
│   ├── get_diversity_score.ipynb
│   ├── get_sentiment_score.py
│   ├── movie_correlation_plots.py
│   ├── other_developers_code
│   │   ├── Egbert
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   ├── TestFile.json
│   │   │   └── downloader.py
│   │   └── emptydir.txt
│   ├── plot_functions.py
│   ├── tests
│   │   ├── Figures
│   │   │   └── tmp.pdf
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── test_divscore.cpython-36-PYTEST.pyc
│   │   │   ├── test_divscore.cpython-37-PYTEST.pyc
│   │   │   ├── test_plot_functions.cpython-36-PYTEST.pyc
│   │   │   ├── test_plot_functions.cpython-37-PYTEST.pyc
│   │   │   ├── test_sentiment.cpython-36-PYTEST.pyc
│   │   │   ├── test_sentiment.cpython-36.pyc
│   │   │   └── test_sentiment.cpython-37-PYTEST.pyc
│   │   ├── test1
│   │   │   └── testing.csv
│   │   ├── test_divscore.py
│   │   ├── test_plot_functions.py
│   │   └── test_sentiment.py
│   └── version.py
├── movie_analysis.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
└── setup.py
```
