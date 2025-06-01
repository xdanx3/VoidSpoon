#!/usr/bin/env python3

import argparse

def stir_the_void():
    print("The void stares back... But nothing happens")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VoidSpoon CLI")
    parser.add_argument("--stir", action="store_true", help="Stir the void")
    args = parser.parse_args()
    if args.stir:
        stir_the_void()
    else:
        print("The void awaits...")
