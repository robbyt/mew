# Overview
The core of this project is to test CPU cache locality by creating a large
list of ints, but only multiplying every n'th member. For a much more 
in-depth article about what I'm trying to test, see:    

http://igoro.com/archive/gallery-of-processor-cache-effects/

# mew.py
I first started this experiment with C, a programming language that is not
my strongest. Writing in C failed because I could not get dynamically sized
lists to work. Some friends said "just use linked lists" or "use glib", but
I decided to write the test in python instead.

## CPU Benchmarking in Python? 
The problem with python, is that it can be much slower than C. So I decided to
compile my python code down to C-bytecode using the amazing new pypy
translate.py jit compiler.

See this gist for a performance comparison between pure python, and pypy:

https://gist.github.com/2253894

## Pypy
So the cool thing about Pypy, is that you can compile your Python code with
the pypy translator, as long as you write your python code "C compatible".

Watch David Beazley's Pycon 2012 keynote for a really great overview of Pypy

http://pyvideo.org/video/659/keynote-david-beazley

# mew runner.py
So what does this thing do? It runs the mew-c program with several different 
conditions, and then writes the average runtime to a .csv file for each
condition. Load this up in Excel, and you can make some nice graphs that show 
some pretty interesting things about the speed of your processor, and the size
of it's cache. 

# So what about the name, mew? 
Short for `Multiplexer`

http://en.wikipedia.org/wiki/Multiplexer


