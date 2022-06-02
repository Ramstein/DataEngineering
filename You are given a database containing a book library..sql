/*
You started to organize your library in your smartphone, and even started to read books right there. After some time the list of books became disorganized, and you even don't know which book to continue reading. So you decided to organize it, and here's what you've got:

You are given a database containing a book library.

The book_library table contains the following columns:

id - a unique ID of the book;
author - the author of the book;
book - the title of the book;
pages_read - the number of pages of the book that you've already read;
total_number_of_pages - the total number of pages in the book;
speed - the number of pages of the book you read per day.
Your task is to write a select query to sort books in the library in a specific order, and then leave only two columns in the result: author and book. The book records should be sorted as follows:

First, order by the authors that have the max number of books in library;
In case of ties, order by the min number of days that you need to read all the books by a particular author;
Then, order by the min number of days that you need to read a particular book;
Finally, order by the title of the books (book column).
Example

For given table book_library

id	author	book	pages_read	total_number_of_pages	speed
1	Chuck Palahniuk	Fight Club	100	200	20
2	Chuck Palahniuk	Survivor	100	300	15
3	Chuck Palahniuk	Haunted	150	400	25
4	Stephen King	Carrie	50	150	10
5	Stephen King	It	100	250	15
6	Stephen King	Mysery	50	350	20
7	Stephen King	Cujo	100	450	25
8	Ken Kesey	Sailor Song	50	125	20
9	Ken Kesey	Demon Box	100	225	25
10	Ken Kesey	Last Go Round	150	235	15
the output should be

author	book
Stephen King	Carrie
Stephen King	It
Stephen King	Cujo
Stephen King	Mysery
Ken Kesey	Sailor Song
Ken Kesey	Demon Box
Ken Kesey	Last Go Round
Chuck Palahniuk	Fight Club
Chuck Palahniuk	Haunted
Chuck Palahniuk	Survivor
Explanation:

There are 4 books of Stephen King, whereas the other authors have 3 books each, so all books by Stephen are placed at the top.
Since it is required 14.4167 days to read all the books by Ken Kesey and 28.3333 days to read all the books by Chuck Palahniuk, books by Ken Kesey are placed above the books by Chuck Palahniuk.
Books by Stephen King are sorted in the way: Both "Carrie" and "It" could be read in 10 days, sorted alphabetically. At the same time, "Cujo" could be read in 14 days, and "Mysery" in 15 days.
[execution time limit] 10 seconds (mysql)


Input:
book_library
id	author	book	pages_read	total_number_of_pages	speed
1	Chuck Palahniuk	Fight Club	100	200	20
2	Chuck Palahniuk	Survivor	100	300	15
3	Chuck Palahniuk	Haunted	150	400	25
4	Stephen King	Carrie	50	150	10
5	Chuck Palahniuk	Choke	100	400	10
6	Stephen King	It	100	250	15
7	Stephen King	Mysery	50	350	20
8	Stephen King	Cujo	100	450	25
9	Ken Kesey	Sailor Song	50	125	20
10	Ken Kesey	Demon Box	100	225	25
11	Ken Kesey	Last Go Round	150	235	15
Output:
author	book
Stephen King	Carrie
Stephen King	It
Stephen King	Cujo
Stephen King	Mysery
Ken Kesey	Sailor Song
Ken Kesey	Demon Box
Ken Kesey	Last Go Round
Chuck Palahniuk	Fight Club
Chuck Palahniuk	Haunted
Chuck Palahniuk	Survivor
Chuck Palahniuk	Choke
Expected Output:
author	book
Stephen King	Carrie
Stephen King	It
Stephen King	Cujo
Stephen King	Mysery
Chuck Palahniuk	Fight Club
Chuck Palahniuk	Haunted
Chuck Palahniuk	Survivor
Chuck Palahniuk	Choke
Ken Kesey	Sailor Song
Ken Kesey	Demon Box
Ken Kesey	Last Go Round


Input:
book_library
id	author	book	pages_read	total_number_of_pages	speed
1	Chuck Palahniuk	Fight Club	100	200	20
2	Chuck Palahniuk	Survivor	100	300	15
3	Chuck Palahniuk	Haunted	150	400	25
4	Stephen King	Carrie	50	150	10
5	Stephen King	It	100	250	15
6	Stephen King	Mysery	50	350	20
7	Stephen King	Cujo	100	450	25
8	Ken Kesey	Sailor Song	50	125	20
9	Ken Kesey	Demon Box	100	225	25
10	Ken Kesey	Last Go Round	150	235	15
11	Emily Bronte	Wuthering Heights	63	109	5
12	Bernard Werber	Les Fourmis	266	269	29
13	Bernard Werber	Le Jour des fourmis	129	183	10
14	Bernard Werber	Les Thanatonautes	81	465	9
15	Ray Bradbury	Fahrenheit 451	172	172	48
16	Ray Bradbury	Dandelion Wine	102	202	23
17	Albert Camus	The Stranger	0	239	24
18	Albert Camus	The Plague	197	428	29
19	Albert Camus	The Fall	28	255	21
20	Albert Camus	The First Man	144	246	44
Output:
author	book
Stephen King	Carrie
Stephen King	It
Stephen King	Cujo
Stephen King	Mysery
Ray Bradbury	Fahrenheit 451
Ray Bradbury	Dandelion Wine
Ken Kesey	Sailor Song
Ken Kesey	Demon Box
Ken Kesey	Last Go Round
Emily Bronte	Wuthering Heights
Chuck Palahniuk	Fight Club
Chuck Palahniuk	Haunted
Chuck Palahniuk	Survivor
Bernard Werber	Les Fourmis
Bernard Werber	Le Jour des fourmis
Bernard Werber	Les Thanatonautes
Albert Camus	The First Man
Albert Camus	The Plague
Albert Camus	The Stranger
Albert Camus	The Fall
Expected Output:
author	book
Albert Camus	The First Man
Albert Camus	The Plague
Albert Camus	The Stranger
Albert Camus	The Fall
Stephen King	Carrie
Stephen King	It
Stephen King	Cujo
Stephen King	Mysery
Ken Kesey	Sailor Song
Ken Kesey	Demon Box
Ken Kesey	Last Go Round
Chuck Palahniuk	Fight Club
Chuck Palahniuk	Haunted
Chuck Palahniuk	Survivor
Bernard Werber	Les Fourmis
Bernard Werber	Le Jour des fourmis
Bernard Werber	Les Thanatonautes
Ray Bradbury	Fahrenheit 451
Ray Bradbury	Dandelion Wine
Emily Bronte	Wuthering Heights

*/


CREATE PROCEDURE solution()
BEGIN
    /*
    1. First, order by the authors that have the max number of books in library;
    2. In case of ties, order by the min number of days that you need to read all the books by a particular author;
    3. Then, order by the min number of days that you need to read a particular book;
    4. Finally, order by the title of the books (book column).
    */
    SELECT author, book
    FROM book_library
    ORDER BY author DESC,
    (SELECT COUNT(*) FROM book_library WHERE author = book_library.author) ASC, 
    (SELECT MIN(speed) FROM book_library WHERE author = book_library.author) ASC,
    (SELECT MIN(speed) FROM book_library WHERE author = book_library.author AND book = book_library.book) ASC,
    book ASC;


END