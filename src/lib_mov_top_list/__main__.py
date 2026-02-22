import os
import time

import requests
import sruthi

TMDB_TOKEN = os.environ["TMDB_TOKEN"]


def get_lib_movie_list() -> set[str]:
    records = sruthi.searchretrieve(
        "https://sru.k10plus.de/gvk",
        query="pica.bib=0115 and pica.mat=v*",
        record_schema="mods",
        maximum_records=20,
    )
    title_infos = [
        rec["mods"]["titleInfo"]
        for rec in records
        if rec["mods"]["typeOfResource"] == "moving image"
    ]
    titles = set()
    for title_info in title_infos:
        if isinstance(title_info, list):
            title_info = {ti.get("type"): ti for ti in title_info}
            if "uniform" in title_info and "title" in title_info["uniform"]:
                titles.add(title_info["uniform"]["title"])
            elif "nonSort" in title_info and "title" in title_info["nonSort"]:
                titles.add(
                    f"{title_info['nonSort']['text']} {title_info['nonSort']['title']}"
                )
            elif None in title_info and "title" in title_info[None]:
                titles.add(title_info[None]["title"])
            else:
                raise NotImplementedError
        elif "title" in title_info:
            titles.add(title_info["title"])
        else:
            raise NotImplementedError
    return titles


def get_movie_rating(title: str) -> tuple[float, int] | None:
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        params={"query": title, "language": "de-de", "include_adult": "true"},
        headers={"Authorization": f"Bearer {TMDB_TOKEN}"},
    )
    response.raise_for_status()
    tmdb_data = response.json()
    if len(tmdb_data["results"]) == 0:
        return None
    movie_data = tmdb_data["results"][0]
    vote = movie_data["vote_average"]
    vote_count = movie_data["vote_count"]
    print(f"{title} = {vote} ({vote_count} votes)")
    time.sleep(1.5)
    return vote, vote_count


def main():
    lib_movie_titles = get_lib_movie_list()
    lib_movies = {title: get_movie_rating(title) for title in lib_movie_titles}
    print(lib_movies)


if __name__ == "__main__":
    main()
