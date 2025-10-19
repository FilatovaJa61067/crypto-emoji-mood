import json
import random

def load_moods(path="data/moods.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    moods = load_moods()
    for coin, coin_moods in moods.items():
        mood = random.choice(coin_moods)
        print(f"{coin.upper():6}: {mood}")

if __name__ == "__main__":
    main()
