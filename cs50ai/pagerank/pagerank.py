import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    probability = {}
    n = len(corpus)

    for pages in corpus:
        probability[pages] = 0

    if corpus[page]:
        links = corpus[page]
    else:
        links = corpus.keys()

    for p in probability:
         probability[p] = (1 - damping_factor) / n
         if p in links:
            probability[p] += damping_factor / len(links)

    return probability

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pagerank = {}
    page_visits = {}

    for page in corpus:
        page_visits[page] = 0

    page = random.choice(list(corpus.keys()))

    for i in range(n-1):
        page_visits[page] += 1
        model = transition_model(corpus, page, damping_factor)
        page = random.choices(list(model.keys()), weights = model.values())[0]

    # calculate pagerank
    for p in page_visits:
        pagerank[p] = page_visits[p] / n

    return pagerank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    if not corpus:
        return {}

    pagerank = {}
    differences = []

    for page in corpus:
        pagerank[page] = 1 / len(corpus)

    margin = 0.001

    while True:
        rank_value = {}
        for page in corpus:
            rank_value[page] = (1 - damping_factor) / len(corpus)

        for page in corpus:
            if corpus[page]:
                num_links = len(corpus[page])
                for p in corpus[page]:
                    rank_value[p] += damping_factor * (pagerank[page] / num_links)
            else:
                for p in corpus:
                    rank_value[p] += damping_factor * (pagerank[page] / len(corpus))

        for page in corpus:
            diff = abs(rank_value[page] - pagerank[page])
            differences.append(diff)

        max_diff = max(differences)

        if max_diff < margin:
            break

        pagerank = rank_value

    return pagerank

if __name__ == "__main__":
    main()
