I save a list of books that I want to read on goodreads (https://www.goodreads.com/) and 
I run a script to search if the books are available at the Sunnyvale Library 
(https://sunnyvale.ca.gov/community/library/default.htm)

The first problem I had was the library won't give me a key to access their official APIs since I don't work for any library. 
I worked around the problem by searching using their regular URL. It's ugly but it works.

Then on 12/8/2020, goodreads decided to unsupport thier APIs and invalidate my API key without any warning.
So I needed to find a new way to get to the list of books I stored on goodreads.
Looks like they still support RSS and that seems to be the easiest and cleaniest way to get to the list of my books.

This python script will get the list of books from goodreads via RSS and then search the Sunnyvale Library.
If a book is available, a URL to the entry at the library is displayed.

If you want to use this script, you will need to customize it by using your own RSS link.
You will also need to use a different library serach link if you use a different library. 
