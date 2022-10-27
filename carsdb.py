import sqlite3

DB_PATH = "cars.db"

OWNERS_QRY = "select first, last, phone from owners where id = ?"
CARS_QRY = (
    "select c.id, c.make, c.model, c.year "
    "from cars c inner join carownership co on c.id = co.carid "
    "where co.ownerid = ?"
)


def main():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    id = int(input("Enter an owner id? "))
    while id > 0:
        # Query DB for owners
        cur.execute(OWNERS_QRY, (id,))
        row = cur.fetchone()
        if row:
            # there is an owner
            print(f"Owner's name = {row[0]} {row[1]} / Phone Number = {row[2]}")
            cur.execute(CARS_QRY, (id,))
            print("Cars owned: ")
            for row in cur.fetchall():
                print(f"Make = {row[1]} / Model = {row[2]} / Year = {row[3]}")
        else:
            print(f"No owners found with id = {id}")

        id = int(input("Enter an owner id? "))


if __name__ == "__main__":
    main()
