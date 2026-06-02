from collections import deque


# -----------------------------------------------------------------------------
# Problem 1
# -----------------------------------------------------------------------------

def count_evidence(evidence):
    """
    Return a dictionary counting how many times each evidence label appears.
    """

    frequency_map = {}

    for label in evidence:
        frequency_map[label] = frequency_map.get(label, 0) + 1

    return frequency_map


# -----------------------------------------------------------------------------
# Problem 2
# -----------------------------------------------------------------------------

def first_repeated_id(ids):
    """
    Return the first suspect ID that appears a second time.
    """

    seen_ids = set()

    for suspect_id in ids:

        if suspect_id in seen_ids:
            return suspect_id

        seen_ids.add(suspect_id)

    return None


# -----------------------------------------------------------------------------
# Problem 3
# -----------------------------------------------------------------------------

def valid_tags(tags):
    """
    Return True if all bracket-style evidence tags are balanced.
    """

    stack = []

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

            # Invalid if stack is empty
            if not stack:
                return False

            top_element = stack.pop()

            # Check matching bracket
            if top_element != bracket_pairs[character]:
                return False

    return len(stack) == 0


# -----------------------------------------------------------------------------
# Problem 4
# -----------------------------------------------------------------------------

def lookup_alias(aliases, alias):
    """
    Return the real name connected to an alias.
    """

    return aliases.get(alias)


# -----------------------------------------------------------------------------
# Optional Challenge 1
# -----------------------------------------------------------------------------

def process_reports(reports):
    """
    Return case reports in first-in, first-out processing order.
    """

    report_queue = deque(reports)

    processed_reports = []

    while report_queue:
        processed_reports.append(report_queue.popleft())

    return processed_reports


# -----------------------------------------------------------------------------
# Optional Challenge 2
# -----------------------------------------------------------------------------

def largest_time_gap(times):
    """
    Return the largest gap between neighboring event times after sorting.
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

        if current_gap > maximum_gap:
            maximum_gap = current_gap

    return maximum_gap