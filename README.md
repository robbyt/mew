# Overview
The core of this project is to test CPU cache locality by creating a large
list of ints, but only multiplying every n'th member. For a much more 
in-depth article about what I'm trying to test, see:    

http://igoro.com/archive/gallery-of-processor-cache-effects/

# mew.py
I first started this experiment with C, a programming language that is not
my strongest. Writing in C failed because I could not get dynamically sized
lists to work. Some friends said "just use linked lists" or "use glib", but
I decided to write the test in python instead. However, running this test in
pure python was very slow. So I compiled mew.py with the pypy jit translator.
(read below for more information about pypy)

# mew_runner.py
So what does this thing do? It runs the mew-c program with several different 
conditions, and then writes the average runtime to a .csv file for each
condition. Running `mew_runner.py` will make your CPU hot, and create a 
file called out.csv each time you run it. 

# plot.py
The plot.py program will read the .csv files that `mew_runner.py` creates 
and will create some nice looking graphs. Run it with any number of csv files 
as args: `python plot.py run1.csv run2.csv`.

## So what about the name, mew? 
Short for `Multiplexer`
http://en.wikipedia.org/wiki/Multiplexer

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

## Building mew.py
* Download the Pypy source (1.8, as of today) https://bitbucket.org/pypy/pypy/get/release-1.8.tar.bz2
* Expand this somewhere, I put it under ~/bin/pypy
* Run the translate.py app against the mew.py file with -Ojit
`~/bin/pypy/pypy-pypy-2346207d9946/pypy/translator/goal/translate.py mew_sum.py`


