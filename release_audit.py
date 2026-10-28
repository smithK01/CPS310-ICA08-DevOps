"""CPS 310 DevOps Fundamentals starter project.

This program reads a small support-ticket data file and prints a summary.
The project intentionally needs some release-readiness improvements.
"""
import json
from tabulate import tabulate

CONFIG_FILE = "config.json"

def load_config(filename):
    """Load project configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

def load_tickets(filename):
    """Load support tickets from a pipe-delimited text file."""
    tickets = []

    try:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                ticket_id, status, priority = line.split("|")
                tickets.append(
                    {
                        "id": ticket_id,
                        "status": status,
                        "priority": int(priority),
                    }
                )
    except FileNotFoundError:
        return []

    return tickets


def count_open_tickets(tickets):
    """Return the number of tickets whose status is open."""
    count = 0

    for ticket in tickets:
        if ticket["status"] == "open":
            count += 1

    return count


def count_high_priority_tickets(tickets, threshold):
    """Return the number of tickets at or above the priority threshold."""
    count = 0

    for ticket in tickets:
        if ticket["priority"] >= threshold:
            count += 1

    return count


def build_summary(tickets, threshold):
    """Return summary information for the current ticket list."""
    return {
        "total": len(tickets),
        "open": count_open_tickets(tickets),
        "high_priority": count_high_priority_tickets(tickets, threshold),
    }


def display_tickets(tickets):
    """Display ticket data in a formatted table."""
    if not tickets:
        print("No tickets found.")
        return

    rows = []

    for ticket in tickets:
        rows.append(
            [ticket["id"], ticket["status"], ticket["priority"]]
        )

    print(tabulate(rows, headers=["Ticket", "Status", "Priority"]))


def main():
    """Run the support-ticket report."""
    config = load_config(CONFIG_FILE)
    tickets = load_tickets(config["data_file"])
    summary = build_summary(tickets, config["high_priority_threshold"])

    print(config["report_title"])
    print("-" * len(config["report_title"]))
    display_tickets(tickets)
    print()
    print(f"Total tickets: {summary['total']}")
    print(f"Open tickets: {summary['open']}")
    print(f"High-priority tickets: {summary['high_priority']}")


if __name__ == "__main__":
    main()
