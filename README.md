# Overview
The core of this project is to test CPU cache locality by creating a large
list of ints, but only multiplying every n'th member. For a much more 
in-depth article about what I'm trying to test, see:    

http://igoro.com/archive/gallery-of-processor-cache-effects/

# mew.py

## How to run:
`./mew.py <amount of data to generate> <number of items to skip> <number to * by>`

For example, if we want to create a list of 128 numbers, and multiply every 
16th number in that list by 3:

`./mew.py 128 16 3`

However, Python is slower than C. There are some pre-compiled binaries
included in the `bin` directory. (compiled for OSX Lion x64, Ubuntu 12.04 x64)
Running those binaries is the same as the Python version, but returns results
about 100x faster.

```
cd bin
./mew_nosum_osx.bin 128 16 3
```

## mew_runner.py
What does this thing do? It runs the mew-c program with several different 
conditions, and then writes the average runtime to a .csv file for each
condition. Running `mew_runner.py` will make your CPU hot, and create a 
file called out.csv each time you run it. 



## plot.py
The plot.py program will read the .csv files that `mew_runner.py` creates 
and will create some nice looking graphs. Run it with any number of csv files 
as args: `python plot.py run1.csv run2.csv`.

# Other Info
## What about the name, mew? 
Short for `Multiplexer`
http://en.wikipedia.org/wiki/Multiplexer

## How much data should I create?
I estimate that a list of 65536 numbers requires about 2097224 bytes of RAM (~2MB).
To get interesting results, try creating data sets that are smaller than your
CPU L2 cache, and larger, and then compare different skip sizes for each.

## CPU Benchmarking in Python? 
The problem with python, is that it can be much slower than C. I decided to
compile my python code down to C-bytecode using the amazing new pypy
translate.py jit compiler.

See this gist for a performance comparison between pure python, and pypy:

https://gist.github.com/2253894

## Pypy
Using the Pypy jit translator allows you to compile your Python code down
to raw, compiled C code as long as you write your python code "C compatible".
See: http://doc.pypy.org/en/latest/coding-guide.html

Watch David Beazley's Pycon 2012 keynote for a really great overview of Pypy
http://pyvideo.org/video/659/keynote-david-beazley

## Building mew.py with pypy
* Download the Pypy source (1.8, as of today) https://bitbucket.org/pypy/pypy/get/release-1.8.tar.bz2
* Expand this somewhere, I put it under ~/bin/pypy
* Run the translate.py app against the mew.py file with:

`python ~/bin/pypy/pypy-pypy-2346207d9946/pypy/translator/goal/translate.py mew_sum.py -Ojit`


