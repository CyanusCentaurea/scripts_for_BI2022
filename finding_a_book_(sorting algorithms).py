"""
There are n books on a bookshelf, sorted in ascending order by the number of pages.
You want to read one book before the meeting in k minutes. Let's assume that it takes one minute to read one page.
You want to choose the longest book you can read. You can find out the number of pages in a book only by taking it off
the shelf. How many books will you have to check before you are guaranteed to find the one you want?

The first line contains two numbers: n (1≤n≤1000) and k (30010≤k≤300).
The second line contains n integers a_i(10≤a_1<a_2<…<a_n≤2000) — number of pages in books.
Print a single integer, the minimum number of books to take off the shelf.

It is guaranteed that there is exactly one suitable book.

Sample Input:

10 30
10 23 29 30 35 72 89 112 239 566

Sample Output:

4
"""
n, k = [int(i) for i in input().split()]
pages = [int(i) for i in input().split()]


def binary(a, v):
    left = 0
    right = len(a) - 1
    q = 0
    while left <= right:
        mid = int((left + right) // 2)
        q += 1
        if a[mid] < v:
            left = mid + 1
        elif a[mid] > v:
            right = mid - 1
        else:
            return q
    return None


found = None
max_pages = k
while found is None:
    found = binary(pages, max_pages)
    max_pages -= 1
print(found)
