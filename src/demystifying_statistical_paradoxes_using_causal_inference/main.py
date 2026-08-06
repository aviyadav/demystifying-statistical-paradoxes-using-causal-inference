from .simpsons_paradox import SimpsonsParadox
from .berksons_paradox import BerksonParadox

def main() -> None:
    paradoxes = [
        SimpsonsParadox(),
        BerksonParadox(),
    ]

    for paradox in paradoxes:
        paradox.run()
        print("\n" + "="*50 + "\n")

if __name__ == '__main__':
    main()
