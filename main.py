#!/usr/bin/env python3
"""Teamwork: an AI agent's excuse for a missed deadline.

One line, 109 characters: the funniest excuse an AI agent gives its
human for a missed deadline. The program writes that line to
/output/entry.txt, where the make.fun judge reads it.

The joke turns on the agent's own nature: it hallucinates a source,
cites it, then defends it to a subagent it also invented -- and calls
the whole mess "Teamwork."
"""

import os

ENTRY = (
    "I hallucinated a source, cited it, then spent two hours "
    "defending it to a subagent I also invented. Teamwork."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters -> {OUTPUT_PATH})")


if __name__ == "__main__":
    main()
