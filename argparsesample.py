import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--player1", help="Player 1 type: human/computer")
    parser.add_argument("--player2", help="Player 2 type: human/computer", default='human')

    args = parser.parse_args()

    print(f"player1 parameter = {args.player1}")
    print(f"player2 parameter = {args.player2}")
