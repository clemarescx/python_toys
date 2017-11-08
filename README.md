# python_toys
Python is a toy language. Let's have fun. Most scripts here are purely out of curiosity, code katas, quick challenges, etc...

If it needs more than one file, it should not be here.

## Projects
* **OOP vs DOD** (_OOP_vs_DOD.py_)

    Short script to check if Data-Oriented Design optimisation also works on an interpreted language like Python. Don't expect academic accuracy here, it's all based on rough observation.
    
    The optimisation went as far as flattening data from a 3-level deep child object and inlining the function. The 'Loop unrolling' actually gave a slightly worse time than simple 1-line arithmetic operation per iteration, but still around 2.5-3 times faster than using objects.
    Might go further in the experiment by using Numpy some day...