import random
def scrape_last_multipliers():
    return [round(random.uniform(1.0, 12.0), 2) for _ in range(30)]
