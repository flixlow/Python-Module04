#! python3

def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        with open("classified_data.txt") as f:
            print("SECURE EXTRACTION:")
            print(f.read())

        with open("security_protocols.txt", "a") as f:
            text = "[CLASSIFIED] New security protocols archived\n"
            print("\nSECURE PRESERVATION:")
            f.write(text)
            print(text.strip())
            print("Vault automatically sealed upon completion")

    except Exception as e:
        print(e)

    else:
        print("\nAll vault operations completed with maximum security.")


def main() -> None:
    ft_vault_security()


if __name__ == "__main__":
    main()
