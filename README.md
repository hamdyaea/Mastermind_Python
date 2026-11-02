# Mastermind — Python CLI

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A Python 3 Mastermind game using four digits from 1 to 8, with repeated colours permitted. Scoring correctly distinguishes exact positions from misplaced matching colours, including duplicates. The secret is generated with `secrets`; the number of attempts is configurable.

```sh
python3 play.py
python3 play.py --attempts 12
python3 -m unittest discover -s tests -v
```

No third-party dependencies, shell clearing or recursive input prompts. Original version: [old branch](https://github.com/hamdyaea/Mastermind_Python/tree/old).
