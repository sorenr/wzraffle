import argparse
import random
import time

candidates = [
    'Seba',
    'Elan',
    'XRay',
    'Greg',
    'Rich'
]

def raffle( seed = None ):
    if not seed:
        seed = int(1000*time.time())

    random.seed(seed)

    winner = random.choice(candidates)
    print(f"Seed {seed} = {winner}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pick a winner.')
    parser.add_argument('-s', dest='seed', type=int, help="seed value")
    args = parser.parse_args()

    raffle( args.seed )
