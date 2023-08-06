from googlesearch import search


def googleSearch(query):

    results = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        results.append(j)
    return results
