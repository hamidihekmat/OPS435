#!/usr/bin/env python3

def function1():
    authorName = 'Andrew 1'
    print(authorName)

def function2():
    global authorName
    authorName = 'Andrew 2'
    print(authorName)

authorName = 'Andrew'
print(authorName)
function1()
print(authorName)
function2()
print(authorName)
