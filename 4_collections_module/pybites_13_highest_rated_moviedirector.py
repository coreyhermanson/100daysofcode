from typing import NamedTuple
import collections
from urllib.request import urlretrieve
import csv
from pprint import pprint

# VARIABLES
url = r'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
data_file = 'movies.csv'
urlretrieve(url, data_file)


# CODE
def main():
    """
    1. Create defaultdict w/ key=director, values=list of movies
    2. Get 5 directors w/ the most movies
    :return: print top 5 directors
    """
    # Create defaultdict of {director: [movies]}
    directors_dict = get_movies_by_director(data_file)

    # print example of NamedTuple output
    pprint(directors_dict['Christopher Nolan'])
    print('\n')

    # Use Counter to output top 5 directors by volume
    counter = collections.Counter()
    for director, movies in directors_dict.items():
        counter[director] += len(movies)

    pprint(counter.most_common(5))


class Movie(NamedTuple):
    title: str
    year: int
    score: float


def get_movies_by_director(data):
    directors = collections.defaultdict(list)

    with open(data, 'r', encoding='utf8', ) as inf:
        reader = csv.DictReader(inf)
        for line in reader:
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


if __name__ == '__main__':
    main()
