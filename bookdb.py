import mysql.connector
from ibookdb import IBOOKDB
from queryresult import QueryResult

class BOOKDB(IBOOKDB):

    def __init__(self,user,password,host,database,port):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port
        self.connection = None

    def initialize(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database,
            port=self.port
        )

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()


    def createTables(self):
        mycursor = self.connection.cursor()
        mycursor.execute("CREATE TABLE author (author_id INT PRIMARY KEY, author_name VARCHAR(60))")
        mycursor.execute("CREATE TABLE publisher (publisher_id INT PRIMARY KEY, publisher_name VARCHAR(50))")
        mycursor.execute("CREATE TABLE book (isbn char(13) PRIMARY KEY, book_name VARCHAR(120), publisher_id INT, first_publish_year CHAR(4), page_count INT, category VARCHAR(25), rating FLOAT, FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id))")
        mycursor.execute("CREATE TABLE author_of (isbn CHAR(13), author_id INT, PRIMARY KEY(isbn, author_id), FOREIGN KEY (isbn) REFERENCES book(isbn), FOREIGN KEY (author_id) REFERENCES author(author_id))")
        mycursor.execute("CREATE TABLE phw1 (isbn CHAR(13), book_name VARCHAR(120), rating FLOAT, PRIMARY KEY(isbn))")
        return 5

    def dropTables(self):
        mycursor = self.connection.cursor()
        mycursor.execute("DROP TABLE author_of")
        mycursor.execute("DROP TABLE author")
        mycursor.execute("DROP TABLE book")
        mycursor.execute("DROP TABLE publisher")
        mycursor.execute("DROP TABLE phw1")
        return 5


    def insertAuthor(self,authors):
        mycursor = self.connection.cursor()
        for author in authors:
            mycursor.execute("INSERT INTO author (author_id, author_name) VALUES (%s, %s)", (author.author_id,author.author_name))
        self.connection.commit()
        return len(authors)


    def insertBook(self,books):
        mycursor = self.connection.cursor()
        for book in books:
            mycursor.execute("INSERT INTO book (isbn, book_name, publisher_id, first_publish_year, page_count, category, rating) VALUES (%s, %s, %s, %s, %s, %s, %s)", (book.isbn, book.book_name, book.publisher_id, book.first_publish_year, book.page_count, book.category, book.rating))
        self.connection.commit()
        return len(books)
    
    def insertPublisher(self,publishers):
        mycursor = self.connection.cursor()
        for publisher in publishers:
            mycursor.execute("INSERT INTO publisher (publisher_id, publisher_name) VALUES (%s, %s)", (publisher.publisher_id, publisher.publisher_name))
        self.connection.commit()
        return len(publishers)
    
    def insertAuthor_of(self,author_ofs):
        mycursor = self.connection.cursor()
        for author_of in author_ofs:
            mycursor.execute("INSERT INTO author_of (isbn, author_id) VALUES (%s, %s)", (author_of.isbn, author_of.author_id))
        self.connection.commit()
        return len(author_ofs)
    
    def functionQ1(self):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT b.isbn, b.first_publish_year, b.page_count, p.publisher_name FROM book b JOIN publisher p ON b.publisher_id = p.publisher_id WHERE b.page_count = (SELECT page_count FROM book ORDER BY page_count DESC LIMIT 1)")
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ1(row[0], row[1], row[2], row[3]))
        return query_result
    
    def functionQ2(self,author_id1, author_id2):
        mycursor = self.connection.cursor()
        mycursor.execute("WITH ortak_kitaplar AS (SELECT isbn FROM author_of WHERE author_id IN (%s, %s)GROUP BY isbn) SELECT p.publisher_id,AVG(b2.page_count) AS ortalama_sayfa_sayisi FROM ortak_kitaplar ok JOIN book b ON ok.isbn = b.isbn JOIN publisher p ON b.publisher_id = p.publisher_id LEFT JOIN book b2 ON b2.publisher_id = p.publisher_id GROUP BY p.publisher_id ORDER BY p.publisher_id ASC;", (author_id1, author_id2))
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ2(row[0], row[1]))
        return query_result

    
    def functionQ3(self,author_name):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT book.book_name, book.category, book.first_publish_year FROM book JOIN author_of ON book.isbn = author_of.isbn JOIN author ON author_of.author_id = author.author_id WHERE author.author_name = %s ORDER BY book.book_name, book.category, book.first_publish_year", (author_name,))
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ3(row[0], row[1], row[2]))
        return query_result
    
    def functionQ4(self):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT DISTINCT book.publisher_id, book.category FROM book JOIN publisher ON book.publisher_id = publisher.publisher_id WHERE publisher.publisher_id IN (SELECT publisher_id FROM book GROUP BY publisher_id HAVING COUNT(DISTINCT category) >= 3 AND AVG(rating) > 3) ORDER BY book.publisher_id, book.category")
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ4(row[0], row[1]))
        return query_result
    
    def functionQ5(self,author_id):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT a.author_id, a.author_name FROM author a JOIN author_of ao ON a.author_id = ao.author_id JOIN book b ON ao.isbn = b.isbn JOIN publisher p ON b.publisher_id = p.publisher_id WHERE p.publisher_id IN (SELECT DISTINCT p.publisher_id FROM author a JOIN author_of ao ON a.author_id = ao.author_id JOIN book b ON ao.isbn = b.isbn JOIN publisher p ON b.publisher_id = p.publisher_id WHERE a.author_id = %s) GROUP BY a.author_id, a.author_name",(author_id,))
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ5(row[0], row[1]))
        return query_result
    
    def functionQ6(self):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT ao.author_id, ao.isbn FROM author_of ao JOIN book b ON ao.isbn = b.isbn WHERE b.publisher_id IN (SELECT publisher_id FROM (SELECT b.publisher_id, COUNT(DISTINCT ao.author_id) as author_count FROM book b JOIN author_of ao ON b.isbn = ao.isbn GROUP BY b.publisher_id) as subquery WHERE author_count = 1) AND ao.author_id NOT IN (SELECT ao.author_id FROM author_of ao JOIN book b ON ao.isbn = b.isbn WHERE b.publisher_id IN (SELECT publisher_id FROM (SELECT b.publisher_id, COUNT(DISTINCT ao.author_id) as author_count FROM book b JOIN author_of ao ON b.isbn = ao.isbn GROUP BY b.publisher_id) as subquery WHERE author_count > 1));")
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ6(row[0], row[1]))
        return query_result
    
    def functionQ7(self,rating):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT publisher.publisher_id, publisher.publisher_name FROM publisher JOIN book ON publisher.publisher_id = book.publisher_id WHERE book.category = 'Roman' GROUP BY publisher.publisher_id HAVING COUNT(book.isbn) >= 2 AND AVG(book.rating) > %s ORDER BY publisher.publisher_id", (rating,))
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ7(row[0], row[1]))
        return query_result
    
    def functionQ8(self):
        mycursor = self.connection.cursor()
        mycursor.execute("INSERT INTO phw1 (isbn, book_name, rating)SELECT isbn, book_name, rating FROM (SELECT b.isbn, b.book_name, b.rating FROM book b WHERE b.book_name IN (SELECT b2.book_name FROM book b2 GROUP BY b2.book_name HAVING COUNT(DISTINCT b2.isbn) > 1) AND b.rating = (SELECT MIN(b3.rating) FROM book b3 WHERE b3.book_name = b.book_name)) AS subquery;")
        self.connection.commit()
        mycursor.execute("SELECT isbn, book_name, rating FROM phw1 ORDER BY isbn")
        result = mycursor.fetchall()
        query_result = []
        for row in result:
            query_result.append(QueryResult.ResultQ8(row[0], row[1], row[2]))
        return query_result

    
    def functionQ9(self,keyword):
        mycursor = self.connection.cursor()
        mycursor.execute("UPDATE book SET rating = rating+1 WHERE book_name LIKE %s AND rating <= 4", ('%'+keyword+'%',))
        self.connection.commit()
        mycursor.execute("SELECT SUM(rating) FROM book")
        result = mycursor.fetchall()
        return result[0][0]
    
    def function10(self):
        mycursor = self.connection.cursor()
        mycursor.execute("DELETE FROM publisher WHERE publisher_id NOT IN (SELECT publisher_id FROM book)")
        self.connection.commit()
        mycursor.execute("SELECT COUNT(publisher_id) FROM publisher")
        result = mycursor.fetchall()
        return result[0][0]
