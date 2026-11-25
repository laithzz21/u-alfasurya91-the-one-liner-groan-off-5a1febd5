"""One-liner groan-off entry: a single original dad joke, one line."""

JOKE = "I told my suitcase there'd be no vacation this year - now it's dealing with emotional baggage."


def validate(joke):
    """Competition rules: one line, at most 140 characters, non-empty."""
    if not joke or "\n" in joke:
        raise ValueError("joke must be a single non-empty line")
    if len(joke) > 140:
        raise ValueError("joke exceeds 140 characters")
    return joke


import os


def write_output(joke):
    """Also write the joke to a per-entry output file when requested."""
    path = os.environ.get("MAKEFUN_OUTPUT")
    if path:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(joke + "\n")


def main():
    joke = validate(JOKE)
    print(joke)
    write_output(joke)


if __name__ == "__main__":
    main()
