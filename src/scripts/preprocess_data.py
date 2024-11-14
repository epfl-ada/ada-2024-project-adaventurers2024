import pandas as pd

from jsonargparse import CLI
from pathlib import Path


def preprocess_data(
    cmu_movie_metadata_path: Path =  '../../data/cmu/movie.metadata.tsv',
    cmu_plot_summaries_path: Path = '../../data/cmu/plot_summaries.txt',
    cmu_character_metadata_path: Path = '../../data/cmu/character.metadata.tsv',
    tropes_path: Path = '../../data/tropes/tropes.csv',
    imdb_movie_tropes_path: Path = '../../data/tropes/film_imdb_match.csv',
    imdb_title_basics_path: Path = '../../data/imdb/title.basics.tsv',
    imdb_title_ratings_path: Path = '../../data/imdb/title.ratings.tsv',
    imdb_title_crew_path: Path = '../../data/imdb/title.crew.tsv',
    imdb_name_basics_path: Path = '../../data/imdb/name.basics.tsv',
    imdb_title_principals_path: Path = '../../data/imdb/title.principals.tsv',
    tmdb_path: Path = '../../data/tmdb/TMDB_movie_dataset_v11.csv',
    output_dir: Path = '../../data'
):
    print("Preprocessing df_cmu_movie_metadata...")
    df_cmu_movie_metadata = preprocess_cmu_movie_metadata(cmu_movie_metadata_path, cmu_plot_summaries_path)

    print("Preprocessing df_tmdb...")
    df_tmdb = preprocess_tmdb_data(tmdb_path)
    
    print("Preprocessing df_cmu_character_metadata...")
    df_cmu_character_metadata = preprocess_character_metadata(cmu_character_metadata_path)

    print("Preprocessing df_imdb_tropes...")
    df_imdb_tropes = preprocess_tropes(tropes_path, imdb_movie_tropes_path)

    print("Preprocessing df_imdb_data...")
    df_imdb_movie_tropes, df_imdb_directors_actors, df_imdb_complete = preprocess_imdb_data(
        imdb_title_basics_path,
        imdb_title_ratings_path,
        imdb_title_crew_path,
        imdb_name_basics_path,
        imdb_title_principals_path,
        df_cmu_movie_metadata,
        df_imdb_tropes
    )
    save_data_csv(df_imdb_movie_tropes, f"{output_dir}/movie_tropes.csv")
    save_data_csv(df_imdb_complete, f"{output_dir}/movie_directors_actors.csv")

    df_cmu_tmdb = merge_cmu_movie_metadata_and_tmdb(df_cmu_movie_metadata, df_tmdb)
    save_data_csv(df_cmu_tmdb, f"{output_dir}/cmu_tmdb.csv")

    df_movie_actors = merge_cmu_and_imdb_directors_actors(
        df_cmu_character_metadata,
        df_cmu_movie_metadata,
        df_imdb_directors_actors
    )
    save_data_csv(df_movie_actors, f"{output_dir}/movie_actors.csv")


def preprocess_cmu_movie_metadata(cmu_movie_metadata_path, cmu_plot_summaries_path):
    df_cmu_movie_metadata = pd.read_csv(cmu_movie_metadata_path, sep='\t', header=None)
    df_cmu_movie_metadata.columns = ['wikipedia_movie_id', 'freebase_movie_id', 'name', 'release_date', 'revenue', 'runtime', 'languages', 'countries', 'genres']

    # Drop rows with missing release date, and extract year from the remaining release dates
    df_cmu_movie_metadata.dropna(subset=['release_date'], inplace=True)
    df_cmu_movie_metadata['release_year'] = df_cmu_movie_metadata['release_date'].apply(extract_year)
    return df_cmu_movie_metadata


def preprocess_character_metadata(cmu_character_metadata_path):
    df_cmu_character_metadata = pd.read_csv(cmu_character_metadata_path, sep='\t', header=None)
    df_cmu_character_metadata.columns = [
        "wikipedia_movie_id", "freebase_movie_id", "release_date", "character_name",
        "actor_date_of_birth", "actor_gender", "actor_height_in_meters", "actor_ethnicity_freebase_id",
        "actor_name", "actor_age_at_movie_release", "freebase_character_actor_map_id",
        "freebase_character_id", "freebase_actor_id"
    ]

    # Drop rows with missing release date, and extract year from each release date
    df_cmu_character_metadata.dropna(subset=['release_date'], inplace=True)
    df_cmu_character_metadata['release_year'] = df_cmu_character_metadata['release_date'].apply(extract_year)

    return df_cmu_character_metadata


def preprocess_tropes(tropes_path, imdb_movie_tropes_path):
    df_tropes = pd.read_csv(tropes_path, index_col=0)
    df_tropes.columns = ['trope_id', 'trope', 'description']

    df_imdb_movie_tropes = pd.read_csv(imdb_movie_tropes_path, index_col=0)
    df_imdb_movie_tropes.columns = ['title', 'trope', 'example', 'clean_title', 'tconst', 'trope_id', 'title_id']
    df_imdb_movie_tropes = df_imdb_movie_tropes.drop(columns=['trope'])

    # Merge imdb movie tropes with tropes to add more information
    df_imdb_movie_tropes = df_imdb_movie_tropes.merge(df_tropes, how='inner', left_on='trope_id', right_on='trope_id')
    df_imdb_movie_tropes = df_imdb_movie_tropes[['tconst', 'title_id', 'clean_title', 'trope_id', 'trope', 'description', 'example']]
    df_imdb_movie_tropes.rename(columns={'tconst': 'imdb_id'}, inplace=True)
    return df_imdb_movie_tropes


def preprocess_imdb_data(
    imdb_title_basics_path,
    imdb_title_ratings_path,
    imdb_title_crew_path,
    imdb_name_basics_path,
    imdb_title_principals_path,
    df_cmu_movie_metadata,
    df_imdb_tropes
):
    # Load title.basics for movie details
    df_imdb_title_basics = pd.read_csv(imdb_title_basics_path, sep='\t')
    df_imdb_title_basics = df_imdb_title_basics[df_imdb_title_basics['titleType'] == 'movie'] 

    # Load title.ratings for movie ratings
    df_imdb_title_ratings = pd.read_csv(imdb_title_ratings_path, sep='\t', usecols=['tconst', 'averageRating', 'numVotes'])

    # Load title.crew for director information, remove rows with missing directors, and expand multiple directors
    df_imdb_title_crew = pd.read_csv(imdb_title_crew_path, sep='\t', usecols=['tconst', 'directors'])
    df_imdb_title_crew = df_imdb_title_crew[df_imdb_title_crew['directors'] != '\\N']
    df_imdb_title_crew = df_imdb_title_crew.assign(director=df_imdb_title_crew['directors'].str.split(',')).explode('director')

    # Load name.basics for director details
    df_imdb_name_basics = pd.read_csv(imdb_name_basics_path, sep='\t', usecols=['nconst', 'primaryName', 'birthYear', 'primaryProfession', 'knownForTitles'])

    # Load title.principals for actor information. We already handle director information through title.crew and name.basics. 
    # We will only load actor information here.
    df_imdb_title_principals = pd.read_csv(imdb_title_principals_path, sep='\t', usecols=['tconst', 'nconst', 'category'])
    df_imdb_title_principals = df_imdb_title_principals[df_imdb_title_principals['category'] == 'actor']

    # -----------------------------------------------------------------------------------------------
    # Obtain complete IMDb dataset for analyzing directors and revenue in CMU dataset, and merging
    # tropes dataset with IMDb dataset

    # Merge IMDb titles.basics information with tropes for tropes analysis
    df_imdb_movie_tropes = pd.merge(df_imdb_tropes, df_imdb_title_basics, how='inner', left_on='imdb_id', right_on='tconst')

    # Merge title.basics and title.ratings to get movie details with ratings
    df_imdb_movies = pd.merge(df_imdb_title_basics, df_imdb_title_ratings, on='tconst', how='left')

    # Merge with title.crew to add director information
    df_imdb_directors = pd.merge(df_imdb_movies, df_imdb_title_crew, on='tconst', how='left')

    # Merge with name.basics to get director's name and known titles
    df_imdb_directors = pd.merge(df_imdb_directors, df_imdb_name_basics, left_on='director', right_on='nconst', how='left')

    # Merge with title.principals to add actor information
    df_imdb_directors_actors = pd.merge(df_imdb_directors, df_imdb_title_principals, on='tconst', how='left')

    # Now, merge again with name.basics to get the actor's name (for the `actor_id` from `title.principals`)
    df_imdb_directors_actors = pd.merge(df_imdb_directors_actors, df_imdb_name_basics[['nconst', 'primaryName']], left_on='nconst_y', right_on='nconst', how='left')

    # Keep only relevant columns in the final merged DataFrame
    df_imdb_directors_actors = df_imdb_directors_actors[['tconst', 'primaryTitle', 'startYear', 'genres', 
                                                        'averageRating', 'numVotes', 'primaryName_x', 
                                                        'birthYear', 'knownForTitles', 'nconst_y', 'primaryName_y']]

    df_imdb_directors_actors.columns = ['movie_id', 'movie_name', 'movie_release_year', 'genres', 'average_rating', 
                                        'num_votes', 'director_name', 'director_birth_year', 'director_known_titles', 
                                        'actor_id', 'actor_name']

    # Merge IMDb data with CMU data to include revenue
    df_cmu_movie_revenue = df_cmu_movie_metadata[['name', 'revenue']]
    df_imdb_complete = pd.merge(
        df_imdb_directors_actors,
        df_cmu_movie_metadata,
        left_on='movie_name',    # IMDb movie name
        right_on='name',         # CMU movie name
        how='left'
    )

    # Drop redundant `name` column from CMU meta data after merge
    df_imdb_complete = df_imdb_complete.drop(columns=['name'])

    return df_imdb_movie_tropes, df_imdb_directors_actors, df_imdb_complete


def preprocess_tmdb_data(tmdb_path):
    df_tmdb = pd.read_csv(tmdb_path)
    df_tmdb['release_year'] = df_tmdb['release_date'].apply(extract_year)

    # Clean tmdb dataset before merging it with the cmu dataset. First, filter released movies
    df_tmdb = df_tmdb[df_tmdb['status'] == 'Released']

    # Drop movies with missing release date
    df_tmdb.dropna(subset=['release_date'], inplace=True)

    return df_tmdb


def save_data_csv(df, path):
    """
    Save dataframe to csv file

    Args:
        df (pd.DataFrame): dataframe to save
        path (str): path to save the dataframe
    """
    try:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
        print(f"Data saved to {path}, shape: {df.shape}")
    except Exception as e:
        print(f"Error saving data: {e}")


def extract_year(date):
    """
    Extract year from date string

    Args:
        date: date separated by '-' where the first element is the year
    Returns:
        year (str): year extracted from the date string
    """
    if date:
        return str(date).split('-')[0]
    return None


def merge_cmu_movie_metadata_and_tmdb(df_cmu_movie_metadata, df_tmdb):
    # Merge CMU movie metadata with TMDB dataset to fill in missing information such as revenue which has a lot of missing values
    df_cmu_movie_metadata_selected = df_cmu_movie_metadata[['wikipedia_movie_id', 'freebase_movie_id', 'name', 'release_year']]
    df_cmu_tmdb = pd.merge(
        df_tmdb,
        df_cmu_movie_metadata_selected,
        how='inner',
        left_on=['title','release_year'],
        right_on=['name', 'release_year']
    )

    # Remove movies with missing imdb because we need it for the tropes analysis
    df_cmu_tmdb.dropna(subset=['imdb_id'], inplace=True)
    return df_cmu_tmdb


def merge_cmu_and_imdb_directors_actors(
    df_cmu_character_metadata,
    df_cmu_movie_metadata,
    df_imdb_directors_actors
):
    df_cmu_movie_character = pd.merge(df_cmu_character_metadata, df_cmu_movie_metadata, on=['wikipedia_movie_id', 'freebase_movie_id', 'release_year'], how='inner')

    # Merge the result with movie ratings
    df_imdb_movie_rating = df_imdb_directors_actors[['movie_name', 'average_rating', 'num_votes']]
    df_movie_actors = pd.merge(df_cmu_movie_character, df_imdb_movie_rating, left_on='name', right_on='movie_name', how='inner')

    # Drop redundant `name` column from CMU movie meta data after merge
    df_movie_actors = df_movie_actors.drop(columns=['name'])
    return df_movie_actors


if __name__ == '__main__':
    CLI(preprocess_data)
