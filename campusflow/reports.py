"""Reporting (Engineer B)."""

STATUSES = ["open", "in_progress", "resolved"]
PRIORITIES = ["critical", "high", "medium", "low"]


def build_report(tickets):
    """Return totals and counts by status and priority.

    Every status and priority is included, with 0 when there are none,
    so an empty ticket list still produces a correct report.
    """
    by_status = {status: 0 for status in STATUSES}
    by_priority = {priority: 0 for priority in PRIORITIES}

    for ticket in tickets:
        by_status[ticket["status"]] += 1
        by_priority[ticket["priority"]] += 1

    return {
        "total": len(tickets),
        "by_status": by_status,
        "by_priority": by_priority,
    }