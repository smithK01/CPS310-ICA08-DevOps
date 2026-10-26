"""CPS 310 DevOps Fundamentals starter project.

This program reads a small support-ticket data file and prints a summary.
The project intentionally needs some release-readiness improvements.
"""

from tabulate import tabulate

DATA_FILE = "tickets.txt"
REPORT_TITLE = "Support Ticket Summary"
HIGH_PRIORITY_THRESHOLD = 4


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
    # Starter defect: this currently counts every ticket.
    return len(tickets)


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
    tickets = load_tickets(DATA_FILE)
    summary = build_summary(tickets, HIGH_PRIORITY_THRESHOLD)

    print(REPORT_TITLE)
    print("-" * len(REPORT_TITLE))
    display_tickets(tickets)
    print()
    print(f"Total tickets: {summary['total']}")
    print(f"Open tickets: {summary['open']}")
    print(f"High-priority tickets: {summary['high_priority']}")


if __name__ == "__main__":
    main()
