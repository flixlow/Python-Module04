#! python3

import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().strip()
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    report = sys.stdin.readline().strip()
    print()
    sys.stdout.write(
        f"[STANDARD] Archive status from {archivist_id}: {report}\n")
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


def main() -> None:
    ft_stream_management()


if __name__ == "__main__":
    main()
