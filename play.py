#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Mastermind CLI: guess four colours (digits 1–8)."""
from __future__ import annotations
import argparse
from collections import Counter
import secrets

LENGTH = 4
COLORS = "12345678"

def new_secret() -> str:
    return "".join(secrets.choice(COLORS) for _ in range(LENGTH))

def validate_guess(guess: str) -> str:
    if len(guess) != LENGTH or any(char not in COLORS for char in guess):
        raise ValueError(f"Enter exactly {LENGTH} digits from 1 to 8")
    return guess

def feedback(secret: str, guess: str) -> tuple[int, int]:
    validate_guess(secret)
    validate_guess(guess)
    exact = sum(a == b for a, b in zip(secret, guess))
    shared = sum((Counter(secret) & Counter(guess)).values())
    return exact, shared - exact

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempts", type=int, default=10)
    args = parser.parse_args()
    if not 1 <= args.attempts <= 100:
        parser.error("--attempts must be between 1 and 100")
    secret = new_secret()
    print("Mastermind — guess four digits 1–8. Repeated digits are allowed.")
    for turn in range(1, args.attempts + 1):
        try:
            guess = validate_guess(input(f"Guess {turn}/{args.attempts}: ").strip())
        except (EOFError, KeyboardInterrupt):
            print("\nGame cancelled")
            return
        except ValueError as exc:
            print(exc)
            continue
        exact, misplaced = feedback(secret, guess)
        print(f"Correct place: {exact}; right digit wrong place: {misplaced}")
        if exact == LENGTH:
            print("You win!")
            return
    print(f"Game over. Secret: {secret}")

if __name__ == "__main__":
    main()
