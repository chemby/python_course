import sqlite3
from random import randint
from pprint import pprint


with sqlite3.connect("books.sqlite3") as connection:
      cursor = connection.cursor()
      cursor.execute("PRAGMA foreign_keys = ON")

      # query = """
      #       CREATE TABLE IF NOT EXISTS books(
      #             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      #             name TEXT NOT NULL,
      #             pages INTEGER NOT NULL CHECK (pages > 0),
      #             price INTEGER NOT NULL CHECK (price > 0),
      #             author_id INTEGER,
      #             FOREIGN KEY (author_id) REFERENCES authors(id)
      #       );
      #
      #       CREATE TABLE IF NOT EXISTS authors(
      #             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      #             name TEXT NOT NULL,
      #             surname TEXT NOT NULL,
      #             birth_date TEXT NOT NULL,
      #             books_written INTEGER NOT NULL
      #       )
      # """
      # cursor.executescript(query)

      # # add authors
      # values = (
      #       ("Jack", "Yabloko", "20.10.1997", 14),
      #       ("Bob", "Something", "30.06.1985", 3),
      #       ("Thomas", "Surname", "13.03.1990", 100),
      #       ("Katy", "Banana", "01.12.1975", 228),
      #       ("Jennifer", "Doe", "07.09.1999", 54),
      #       ("James", "Ivanov", "23.04.2000", 37),
      #       ("Max", "Unpopular", "13.06.1964", 8),
      #       ("Jane", "Unknown", "25.05.1992", 120)
      # )
      #
      # query = """
      #             INSERT INTO authors(name, surname, birth_date, books_written)
      #             VALUES (?, ?, ?, ?)
      #       """
      #
      # cursor.executemany(query, values)

      # # add books
      # values = (
      #       ("Autobiography", 23, 100, 3),
      #       ("Some book", 3, 15, 1),
      #       ("Spider-man", 123, 230, 2),
      #       ("Spider-man 2", 150, 300, 5),
      #       ("Wizard Story", 83, 55, 4),
      #       ("Sherlock Holmes", 250, 168, 6)
      # )
      #
      # query = """
      #                   INSERT INTO books(name, pages, price, author_id)
      #                   VALUES (?, ?, ?, ?)
      #             """
      #
      # cursor.executemany(query, values)

      # # inner join
      # query = """
      #             SELECT books.name, books.price, authors.name, authors.surname, authors.books_written
      #             FROM books
      #             INNER JOIN authors
      #             ON books.author_id = authors.id
      #       """
      #
      # result = cursor.execute(query)
      # pprint(result.fetchall())

      # # left join
      # query = """
      #                  SELECT *
      #                  FROM books
      #                  LEFT JOIN authors
      #                  ON books.author_id = authors.id
      #            """
      #
      # result = cursor.execute(query)
      # pprint(result.fetchall())

      # full join
      query = """
                             SELECT *
                             FROM books
                             FULL JOIN authors
                             ON books.author_id = authors.id
                       """

      result = cursor.execute(query)
      pprint(result.fetchall())
