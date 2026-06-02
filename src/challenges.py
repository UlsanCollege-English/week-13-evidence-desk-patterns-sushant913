from collections import deque


def count_evidence(evidence: list[str]) -> dict[str, int]:
    frequency_map = {}

    for label in evidence:
        frequency_map[label] = frequency_map.get(label, 0) + 1

    return frequency_map


def first_repeated_id(ids: list[str]) -> str | None:
    seen_ids = set()

    for suspect_id in ids:

        if suspect_id in seen_ids:
            return suspect_id

        seen_ids.add(suspect_id)

    return None


def valid_tags(tags: str) -> bool:
    stack = []

    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    opening_brackets = set(bracket_pairs.values())

    for character in tags:

        if character in opening_brackets:
            stack.append(character)

        elif character in bracket_pairs:

            if not stack:
                return False

            top_element = stack.pop()

            if top_element != bracket_pairs[character]:
                return False

    return len(stack) == 0


def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    return aliases.get(alias)


def process_reports(reports: list[str]) -> list[str]:
    report_queue = deque(reports)

    processed_reports = []

    while report_queue:
        processed_reports.append(report_queue.popleft())

    return processed_reports


def largest_time_gap(times: list[int]) -> int:

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