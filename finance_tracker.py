import json
from datetime import date

DATA_FILE = "data.json"
transactions = []


def load_from_file():

    global transactions
    try:
        with open(DATA_FILE, "r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        transactions = []
    except json.JSONDecodeError:
        transactions = []


def save_to_file():
   
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, ensure_ascii=False, indent=2)


def add_transaction(amount, category, description, date_str=None):

    if date_str is None:
        date_str = str(date.today())

    transaction = {
        "datum": date_str,
        "betrag": amount,
        "kategorie": category,
        "beschreibung": description
    }
    transactions.append(transaction)


def show_transactions():

    if not transactions:
        print("Keine Transaktionen vorhanden.")
        return

    print("{:<12} {:>10} {:<15} {}".format("Datum", "Betrag", "Kategorie", "Beschreibung"))
    print("-" * 60)
    for t in transactions:
        print("{:<12} {:>10.2f} {:<15} {}".format(
            t["datum"], t["betrag"], t["kategorie"], t["beschreibung"]
        ))


def filter_by_category(category):
    filtered = [t for t in transactions if t["kategorie"].lower() == category.lower()]

    if not filtered:
        print("Keine Transaktionen in dieser Kategorie.")
        return

    print("{:<12} {:>10} {:<15} {}".format("Datum", "Betrag", "Kategorie", "Beschreibung"))
    print("-" * 60)
    for t in filtered:
        print("{:<12} {:>10.2f} {:<15} {}".format(
            t["datum"], t["betrag"], t["kategorie"], t["beschreibung"]
        ))


def calculate_balance():
    balance = sum(t["betrag"] for t in transactions)
    print(f"Gesamtsaldo: {balance:.2f} €")
    return balance


def show_menu():
    print()
    print("Wähle eine Option:")
    print("1. Einnahme hinzufügen")
    print("2. Ausgabe hinzufügen")
    print("3. Alle Transaktionen anzeigen")
    print("4. Nach Kategorie filtern")
    print("5. Kontostand anzeigen")
    print("6. Speichern & Beenden")


def main():
    load_from_file()
    print("Willkommen beim Personal Finance Tracker!")

    while True:
        show_menu()
        choice = input("Deine Auswahl: ")

        if choice == "1":
            try:
                amount = float(input("Betrag (positiv): "))
            except ValueError:
                print("Ungültiger Betrag.")
                continue
            category = input("Kategorie: ")
            description = input("Beschreibung: ")
            add_transaction(amount, category, description)

        elif choice == "2":
            try:
                amount = float(input("Betrag (positiv): "))
            except ValueError:
                print("Ungültiger Betrag.")
                continue
            category = input("Kategorie: ")
            description = input("Beschreibung: ")
            add_transaction(-amount, category, description)

        elif choice == "3":
            show_transactions()

        elif choice == "4":
            category = input("Kategorie zum Filtern: ")
            filter_by_category(category)

        elif choice == "5":
            calculate_balance()

        elif choice == "6":
            save_to_file()
            print("Daten gespeichert. Programm wird beendet.")
            break

        else:
            print("Ungültige Auswahl.")


if __name__ == "__main__":
    main()
