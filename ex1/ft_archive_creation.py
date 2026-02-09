#!python3

def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")
    text: str = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee\n"""

    try:
        f = open("new_discovery.txt", "a")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        f.write(text)
        print(text)

    except Exception as e:
        print(e)
    else:
        f.close()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")


def main() -> None:
    ft_archive_creation()


if __name__ == "__main__":
    main()
