import pandas as pd

def count_books_and_ratings(books, ratings):
    ISBN_s = [row['ISBN'] for index,row in books.iterrows()]
    print('ISBN_s:')
    print(type(ISBN_s[0]))
    i = 0
    print(books['prices'][i])
    for isbn in ISBN_s:
        counts = ratings['ISBN'].value_counts().to_dict()
        print(isbn, '\t' , counts[isbn], '\t', books['prices'][i])
        i+=1
    #counts = [isbn,count for isbn,count in ISBN_s,ratings.groupby(isbn).count()] 

def read_ratings():
    ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';',encoding='unicode_escape')
    print(ratings.head())
    print(ratings.tail())
    return ratings

def read_books():
    books = pd.read_csv('BX-Books.csv', sep=';', nrows=20)
    print(books.head())
    prices = [64.68,2.50,65.73,7.97,8.60,8.90,9.56,4.99,14.95,12.00,9.15,16.00,79.30,4.95,2.00,7.95,75.55,10.91,2.19,21.00]
    books['prices'] = prices
    print('\nFirst book: ')
    print(books.iloc[0])
    return books

def main():
    books = read_books()
    ratings = read_ratings()
    count_books_and_ratings(books, ratings)


if __name__ == '__main__':
    main()
