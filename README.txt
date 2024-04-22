SCHEMA
author(author id:int, author name:varchar(60))
publisher(publisher id:int, publisher name:varchar(50))
book(isbn:char(13), book name:varchar(120), publisher id:int, first publish year:char(4), page count:int, category:varchar(25), rating:float) REFERENCES publisher(publisher id)
author of(isbn:char(13),author id:int) REFERENCES book(isbn) author(author id)
phw1(isbn:char(13), book name:varchar(120), rating:float)

1. createTables(self): Create all tables according to the schema defined above
2. Data has been added to the appropriate tables. In this task, no data has been added to table phw1.
3. Query 1, The book(s) with the most pages should be listed with isbn, first publish year, page count and publisher name. yYou must sort the results in ascending order by isbn. 
4. Query 2, You will list the publisher ids of the publishing houses that published the books co-authored by the given two authors, and the average page count of all books published by these publishing houses. You must sort the results in ascending order according to the publisher id. 
5. Query 3, You will list the book name, category and first publish year of the earliest published book(s) of the author(s) with the given author name. You must sort the results in ascending order by book name, category and first publish year. 
6. Query 4, You will list the publisher ids of publishing houses with names containing at least 3 words (¨ornek: "Koc Universitesi Yayinlari"), that have published at least 3 books and have an average rating higher than 3 for all their books, and the different categories they publish in. Note: you can assume that each word in publisher name is separated by a space. You must sort the results in ascending order by publisher id and category.
7. Query 5, You will list the author id and author name of all authors who have worked with all publishers with the given author id. You must sort the results in ascending order by author id.
8. Query 6, List author id, isbn(s) of 'selective' authors. "Selective" authors are "authors who have only dealt with publishers who have published their own books (i.e. they have not published books by other authors). You must sort the results in ascending order by author id and ISBN number.
9. Query 7, You will list the publisher id and publisher name of publishers who have published at least 2 books in the 'Novel' category and whose average rating is higher than the given value. You must sort the results in ascending order according to the publisher id.
10. Query 8, Some books in the store may have been published more than once: they may have the same title (book name) but different ISBNs. For each of these books, find the isbn, book name and rating of the one with the lowest rating and save them in table phw1 using a single BULK insert query. If there is more than one book with the lowest rating, then save them all. After the bulk insert, list the isbn, book name and rating of all rows in table phw1. You must sort them in ascending order by isbn.
11. Query 9, Increase the rating by one (1) for books with the given keyword in the book name. The maximum rating cannot be more than 5, so do not update the rating of a book if the rating before the change was greater than 4. After the update, return the sum of the ratings of all books.
12. Query 10, Delete publishers that have never published a book from the publisher table. After deletion, return the number of records in the publisher table.


In Turkish;

1. Yukarıda tanımlanan semaya gore tum tabloları olusturacaksınız (create).
2. Uygun tablolara veri ekleyeceksiniz.Bu fonksiyon basarıyla eklenen satır sayısını dondurur. Bu gorevde, lutfen phw1 tablosuna herhangi bir veri eklemeyin.
3. Query 1,En fazla sayfaya sahip olan kitabın(kitapların) isbn, first publish year, page count ve publisher name bilgilerini listeleyeceksinz. Sonucları isbn’ye gore artan sırada sıralamalısınız.
4. Query 2,Verilen iki yazarın birlikte yazdıgı kitapları yayımlayan yayınevlerinin; publisher id’lerini ve bu yayınevlerinin yayımladıgı tum kitapların ortalama sayfa sayısını (page count) listeleyeceksiniz. Sonucları publisher id’ye gore artan sırada sıralamalısınız.
5. Query 3, Verilen author name’e sahip yazar(lar)ın en erken yayımlanan kitabının(kitaplarının) book name, category ve first publish year bilgilerini listeleyeceksiniz. Sonucları book name, category ve first publish year’a gore artan sırada sıralamalısınız.
6. Query 4,En az 3 kelime iceren (¨ornek: "Koc Universitesi Yayinlari") isimlere sahip, en az 3 kitap yayımlamıs olan ve tum kitaplarının ortalama rating’i 3’ten buyuk olan yayınevlerinin publisher id’lerini ve yayınladıkları farklı kategorileri (category) listeleyeceksiniz. Not: publisher name icindeki her kelimenin bir boslukla ayrıldıgını varsayabilirsiniz. Sonucları publisher id ve category’e gore artan sırada sıralamalısınız
7. Query 5, Verilen author id’nin calıstıgı tum yayınevleriyle calısmıs yazarların author id ve author name bilgilerini listeleyeceksiniz.Sonucları author id’ye gore artan sırada sıralamalısınız.
8. Query 6, Secici’ yazarların author id, isbn(ler)ini listeleyin. ”Secici” yazarlar;” yalnızca kendi kitaplarını yayımlayan yayınevleriyle ¸calısmıs olan yazarlardır. (yani, farklı yazarların kitaplarını yayınlamamıslardır). Sonucları author id ve ISBN numarasına gore artan sırada sıralamalısınız.
9. Query 7, ’Roman’ kategorisinde en az 2 kitap yayımlamıs olan ve kitaplarının ortalama rating’i verilen degerden buyuk olan yayınevlerinin publisher id ve publisher namelerini listeleyeceksiniz. Sonucları publisher id’ye gore artan sırada sıralamalısınız.
10. Query 8, Magazadaki bazı kitaplar birden fazla kez yayımlanmıs olabilir: aynı isimlere (book name) sahip olmalarına ragmen, farklı isbn’lerle yayımlanmıs olabilirler. Bu kitapların her biri icin, en kucuk rating’e sahip olanlarının isbn, book name ve rating’lerini bulun ve bunları tek bir BULK insert sorgusu kullanarak phw1 tablosuna
kaydedin. Eger en dusuk puanlı birden fazla kitap varsa, o zaman hepsini kaydedin. Toplu ekleme isleminden sonra, phw1 tablosundaki tum satırların isbn, book name ve rating’lerini listeleyiniz. Isbn’e gore artan sırada sıralamalısınız.
11. Query 9, ˙Isimlerinin (book name) icerisinde verilen anahtar kelime(keyword) olan kitapların rating’lerini bir (1)artırın. Maksimum rating 5’ten fazla olamaz, bu nedenle degistirmeden onceki rating 4’ten buyukse, o kitabın rating’ini guncellemeyiniz. Guncelleme isleminden sonra, tum kitapların rating’lerinin toplamını dondurunuz.
12. Query 10, Henuz hic kitap yayımlamamıs yayınevlerini publisher tablosundan siliniz. Silme isleminden sonra, yayınevleri tablosundaki kayıtların sayısını dondurunuz.


