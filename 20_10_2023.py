import sqlite3
from random import randint

def generate_barcode():
      barcode = f"{randint(0,9)}-"
      for i in range(5):
         barcode += str(randint(0,9))
      return barcode

with sqlite3.connect("books.sqlite3") as connection:
      cursor = connection.cursor()
      connection.create_function("generate_barcode", 0, generate_barcode)
      # query = """
      #       CREATE TABLE IF NOT EXISTS books(
      #             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      #             name TEXT NOT NULL,
      #             pages INTEGER NOT NULL CHECK (length(pages) > 0),
      #             price INTEGER NOT NULL CHECK (length(price) > 0),
      #       )
      # """
      # cursor.execute(query)

      # # create single book
      # name = "гра престолів"
      # pages = 149
      # price = 100
      # values = [name, pages, price]
      #
      # query = """
      #       INSERT INTO books(name, pages, price)
      #       VALUES(?, ?, ?)
      # """
      #
      # cursor.execute(query, values)

      # # create multiple books
      # values = (
      #       ("історія хвороби", 200, 345),
      #       ("Гаррі Поттер", 123, 47),
      #       ("історія 7 клас", 498, 233),
      #       ("чарівник з країни Оз", 25, 100),
      #       ("чарівна історія", 228, 305)
      # )
      #
      # query = """
      #             INSERT INTO books(name, pages, price)
      #             VALUES (?, ?, ?)
      #       """
      #
      # cursor.executemany(query, values)

      # # select books where price > 100
      # query = """
      #       SELECT *
      #       FROM books
      #       WHERE price > 100
      # """
      #
      # result = cursor.execute(query)
      # print(result.fetchall())

      # # select 3 cheapest books
      # query = """
      #       SELECT *
      #       FROM books
      #       ORDER BY price ASC
      #       LIMIT 3
      # """
      #
      # result = cursor.execute(query)
      # print(result.fetchall())

      # # select 2 history books
      # query = """
      #             SELECT *
      #             FROM books
      #             WHERE name LIKE '%історія%'
      #             LIMIT 2
      #       """
      #
      # result = cursor.execute(query)
      # print(result.fetchall())

      # # add barcode column
      # query = """
      #       ALTER TABLE books ADD barcode TEXT
      # """
      # cursor.execute(query)

      # # set barcode to books with pages > 200
      # query = """
      #
      #       UPDATE books
      #       SET barcode = generate_barcode()
      #       WHERE pages > 200
      # """
      # result = cursor.execute(query)

      # delete books with price 100

      query = """
            DELETE FROM books
            WHERE price == 100
      """
      cursor.execute(query)
