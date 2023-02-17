# Python - Everything is object

Project done during my **Software Engineering studies** at **Holberton School**. It aims to study about object instantiation in **Python**, delving into variable aliasing and object identifiers, types, and mutability. This project involved a series of quiz-like questions, the answers were provided in single-line `.txt` files.

## Tasks

* [`0-answer.txt`](./0-answer.txt): What function would you use to print the type of an object? 

* [`1-answer.txt`](./1-answer.txt): How do you get a variable's identifier (which is the memory address in the CPython implementation)? 

*  [`2-answer.txt`](./2-answer.txt): In the following code, do `a` and `b` point to the same object? 
    ```
    >>> a = 89
    >>> b = 100
    ```
*  [`3-answer.txt`](./3-answer.txt): In the following code, do `a` and `b` point to the same object?
    ```
    >>> a = 89
    >>> b = 89
    ```
*  [`4-answer.txt`](./4-answer.txt): In the following code, do `a` and `b` point to the same object?
    ```
    >>> a = 89
    >>> b = a
    ```
*  [`5-answer.txt`](./5-answer.txt): In the following code, do `a` and `b` point to the same object?
    ```
    >>> a = 89
    >>> b = a + 1
    ```
*  [`6-answer.txt`](./6-answer.txt): What do these 3 lines print?
    ```
    >>> s1 = "Holberton"
    >>> s2 = s1
    >>> print(s1 == s2)
    ```
*  [`7-answer.txt`](./7-answer.txt): What do these 3 lines print?
    ```
    >>> s1 = "Holberton"
    >>> s2 = s1
    >>> print(s1 is s2)
    ```
*  [`8-answer.txt`](./8-answer.txt): What do these 3 lines print?
    ```
    >>> s1 = "Holberton"
    >>> s2 = "Holberton"
    >>> print(s1 == s2)
    ```
*  [`9-answer.txt`](./9-answer.txt): What do these 3 lines print?
    ```
    >>> s1 = "Holberton"
    >>> s2 = "Holberton"
    >>> print(s1 is s2)
    ```
*  [`10-answer.txt`](./10-answer.txt): What do these 3 lines print?
    ```
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3]
    >>> print(l1 == l2)
    ```
*  [`11-answer.txt`](./11-answer.txt): What do these 3 lines print?
    ```
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3]
    >>> print(l1 is l2)
    ```
*  [`12-answer.txt`](./12-answer.txt): What do these 3 lines print?
    ```
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 == l2)
    ```
*  [`13-answer.txt`](./13-answer.txt): What do these 3 lines print?
    ```
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 is l2)
    ```
*  [`14-answer.txt`](./14-answer.txt): What does this script print?
    ```
    l1 = [1, 2, 3]
    l2 = l1
    l1.append(4)
    print(l2)
    ```
*  [`15-answer.txt`](./15-answer.txt): What does this script print?
    ```
    l1 = [1, 2, 3]
    l2 = l1
    l1 = l1 + [4]
    print(l2)
    ```
*  [`16-answer.txt`](./16-answer.txt): What does this script print?
    ```
    def increment(n):
        n += 1

    a = 1
    increment(a)
    print(a)
    ```
*  [`17-answer.txt`](./17-answer.txt): What does this script print?
    ```
    def increment(n):
        n.append(4)

    l = [1, 2, 3]
    increment(l)
    print(l)
    ```
*  [`18-answer.txt`](./18-answer.txt): What does this script print?
    ```
    def assign_value(n, v):
        n = v

    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    assign_value(l1, l2)
    print(l1)
    ```
*  [`19-answer.py`](./19-answer.py): Python function `def copy_list(l):` that returns
a copy of a list.

*  [`20-answer.txt`](./20-answer.txt): Is `a` a tuple?
    ```
    a = ()
    ```
*  [`21-answer.txt`](./21-answer.txt): Is `a` a tuple?
    ```
    a = (1, 2)
    ```
*  [`22-answer.txt`](./22-answer.txt): Is `a` a tuple?
    ```
    a = (1)
    ```
*  [`23-answer.txt`](./23-answer.txt): Is `a` a tuple?
    ```
    a = (1, )
    ```
*  [`24-answer.txt`](./24-answer.txt): What does this script print?
    ```
    a = (1)
    b = (1)
    a is b
    ```
*  [`25-answer.txt`](./25-answer.txt): What does this script print?
    ```
    a = (1, 2)
    b = (1, 2)
    a is b
    ```
*  [`26-answer.txt`](./26-answer.txt): What does this script print?
    ```
    a = ()
    b = ()
    a is b
    ```
*  [`27-answer.txt`](./27-answer.txt): Will the last line of this script print `139926795932424`?
    ```
    >>> id(a)
    139926795932424
    >>> a
    [1, 2, 3, 4]
    >>> a = a + [5]
    >>> id(a)
    ```
*  [`28-answer.txt`](./28-answer.txt): Will the last line of this script print `139926795932424`?
    ```
    >>> a
    [1, 2, 3]
    >>> id (a)
    139926795932424
    >>> a += [4]
    >>> id(a)
    ```

## Authors

* Juan Esteban Duque <a href="https://github.com/Juanesduque1" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>
