"""
Week 1 Homework: Evidence Desk Patterns

Author: Sushant Thapa
Python Version: 3.11+

Patterns Used:
1. Frequency Counting
2. Seen-Before Detection
3. Stack Matching
4. Lookup Table
5. Queue Processing
6. Sorting + Scanning
"""

from collections import deque


# -----------------------------------------------------------------------------
# Problem 1 — Frequency Counting
# -----------------------------------------------------------------------------

def count_evidence(evidence: list[str]) -> dict[str, int]:
    """
    Count how many times each evidence label appears.

    Args:
        evidence: List of evidence labels.

    Returns:
        Dictionary containing evidence counts.
    """

    frequency_map: dict[str, int] = {}

    for label in evidence:
        frequency_map[label] = frequency_map.get(label, 0) + 1

    return frequency_map


# -----------------------------------------------------------------------------
# Problem 2 — Seen-Before Pattern
# -----------------------------------------------------------------------------

def first_repeated_id(ids: list[str]) -> str | None:
    """
    Find the first suspect ID that appears twice.

    Args:
        ids: List of suspect IDs.

    Returns:
        First repeated ID or None.
    """

    seen_ids: set[str] = set()

    for suspect_id in ids:

        if suspect_id in seen_ids:
            return suspect_id

        seen_ids.add(suspect_id)

    return None


# -----------------------------------------------------------------------------
# Problem 3 — Stack Matching
# -----------------------------------------------------------------------------

def valid_tags(tags: str) -> bool:
    """
    Validate whether all brackets are balanced.

    Supported brackets:
        (), [], {}

    Args:
        tags: String containing possible bracket characters.

    Returns:
        True if brackets are balanced, otherwise False.
    """

    stack: list[str] = []

    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    opening_brackets = set(bracket_pairs.values())

    for character in tags:

        # Opening bracket
        if character in opening_brackets:
            stack.append(character)

        # Closing bracket
        elif character in bracket_pairs:

            if not stack:
                return False

            top_element = stack.pop()

            if top_element != bracket_pairs[character]:
                return False

    return len(stack) == 0


# -----------------------------------------------------------------------------
# Problem 4 — Lookup Table
# -----------------------------------------------------------------------------

def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    """
    Retrieve the real name associated with an alias.

    Args:
        aliases: Dictionary mapping aliases to real names.
        alias: Alias to search.

    Returns:
        Real name if found, otherwise None.
    """

    return aliases.get(alias)


# -----------------------------------------------------------------------------
# Optional Challenge 1 — Queue Processing
# -----------------------------------------------------------------------------

def process_reports(reports: list[str]) -> list[str]:
    """
    Process reports using FIFO order.

    Args:
        reports: Incoming reports in arrival order.

    Returns:
        Processed reports in FIFO order.
    """

    report_queue: deque[str] = deque(reports)

    processed_reports: list[str] = []

    while report_queue:
        processed_reports.append(report_queue.popleft())

    return processed_reports


# -----------------------------------------------------------------------------
# Optional Challenge 2 — Sorting + Scan
# -----------------------------------------------------------------------------

def largest_time_gap(times: list[int]) -> int:
    """
    Find the largest gap between neighboring timestamps.

    Args:
        times: List of integer timestamps.

    Returns:
        Largest neighboring gap after sorting.
    """

    if len(times) < 2:
        return 0

    sorted_times = sorted(times)

    maximum_gap = 0

    for current_index in range(len(sorted_times) - 1):

        current_gap = (
            sorted_times[current_index + 1]
            - sorted_times[current_index]
        )

        maximum_gap = max(maximum_gap, current_gap)

    return maximum_gap


# -----------------------------------------------------------------------------
# Manual Testing
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    print("Problem 1")
    print(count_evidence(["phone", "receipt", "phone"]))

    print("\nProblem 2")
    print(first_repeated_id(["A17", "B22", "C91", "B22"]))

    print("\nProblem 3")
    print(valid_tags("{[()]}"))
    print(valid_tags("{[(])}"))

    print("\nProblem 4")
    aliases = {
        "Big Red": "Marco Silva",
        "Ghostline": "Eli Brooks"
    }
    print(lookup_alias(aliases, "Ghostline"))

    print("\nOptional Challenge 1")
    print(process_reports([
        "burglary",
        "traffic stop",
        "noise complaint"
    ]))

    print("\nOptional Challenge 2")
    print(largest_time_gap([1300, 915, 1600, 945]))