"""Tests for the CPS 310 DevOps Fundamentals starter project."""

from release_audit import (
    build_summary,
    count_high_priority_tickets,
    count_open_tickets,
    load_tickets,
)


def test_count_open_tickets_counts_only_open_status():
    # Arrange
    tickets = [
        {"id": "T-101", "status": "open", "priority": 5},
        {"id": "T-102", "status": "closed", "priority": 2},
        {"id": "T-103", "status": "open", "priority": 3},
    ]

    # Act
    result = count_open_tickets(tickets)

    # Assert
    assert result == 2


def test_count_high_priority_tickets_uses_threshold():
    # Arrange
    tickets = [
        {"id": "T-101", "status": "open", "priority": 5},
        {"id": "T-102", "status": "closed", "priority": 2},
        {"id": "T-103", "status": "open", "priority": 4},
    ]

    # Act
    result = count_high_priority_tickets(tickets, 4)

    # Assert
    assert result == 2


def test_build_summary_reports_all_counts():
    # Arrange
    tickets = [
        {"id": "T-101", "status": "open", "priority": 5},
        {"id": "T-102", "status": "closed", "priority": 2},
        {"id": "T-103", "status": "open", "priority": 4},
    ]

    # Act
    result = build_summary(tickets, 4)

    # Assert
    assert result == {
        "total": 3,
        "open": 2,
        "high_priority": 2,
    }


def test_load_tickets_reads_valid_file(tmp_path):
    # Arrange
    test_file = tmp_path / "tickets.txt"
    test_file.write_text(
        "T-201|open|3\nT-202|closed|1\n",
        encoding="utf-8",
    )

    # Act
    result = load_tickets(test_file)

    # Assert
    assert result == [
        {"id": "T-201", "status": "open", "priority": 3},
        {"id": "T-202", "status": "closed", "priority": 1},
    ]


def test_load_tickets_missing_file_returns_empty_list(tmp_path):
    # Arrange
    missing_file = tmp_path / "missing.txt"

    # Act
    result = load_tickets(missing_file)

    # Assert
    assert result == []
