# Overview

As somebody who wants to be able to do full stack development it is vital for me to understand how sockets work and how computers communicate from 
one machine to the next. I decided to make my own API framework that uses the Python Socket library to abstract away things and give other programmers an easy 
interface to write an API while hiding away the lower level details.

I wrote a simple HTTP server and am working on the user interface so that programmers can write the handler and their own application specific logic and use 
my library to hide away the lower level socket details.

My purpose for writing this software was to better understand client-server communication and how HTTP works at a lower level.

[Client Server DEMO](https://youtu.be/zSwY4bwLgko)

# Network Communication

I used the client server architecture for this project. I wanted to simulate something similar 
to how a browser would actually call a server from the client side.

I used TCP because reliability mattered to me and I just used port 5000 to test things out.

I used HTTP version 1 to communicate between the client and server so they would each be able to understand 
what is being sent and when to stop accepting the stream of bytes.

# Development Environment

Python 3.12
Python Socket Module
Python JSON library

# Useful Websites

* [Beej's Guide to Network Programming](http://url.link.goes.here](https://beej.us/guide/bgnet/)
* [Python Socket Module](http://url.link.goes.here](https://docs.python.org/3/library/socket.html)

# Future Work

* Improve Programmer Interface to easily make the handler
* Improve parser to accept more types
* Add Error handling
