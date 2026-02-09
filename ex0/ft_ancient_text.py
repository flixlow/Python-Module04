# python3

def ft_ancient_text() -> None:
    print("Accessing Storage Vault: ancient_fragment.txt\n")
    try:
        f = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
    except Exception:
        print("ERROR: Storage vault not found.")
    else:
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")


def main():
    ft_ancient_text()


if __name__ == "__main__":
    main()
