## Brainfuck interpreter in one line

According to [this comment on reddit](https://www.reddit.com/r/Python/comments/3cu6ej/what_are_some_wtf_things_about_python/csz3lwa/), it's possible to write every Python program (that doesn't throw exceptions) in just one line without using any semicolons.

Here's a photo of me shortly after reading that comment:

![](https://stayhipp.com/wp-content/uploads/2019/07/New.jpg)

So I wrote a Brainfuck interpreter in just one line, with no semicolons. Tested with hello-world and rot13  in brainfuck. Use like this: `python3 b.py some_bf_code.bf`

Here's the thing in a more "readable" format:

```python
with type("Com", (), {  # create a new type Com
    # define __enter__ and __exit__ methods to make the type available for
    # the with .. as .. syntax
    "__enter__": lambda  s: s,
    "__exit__":lambda s,e,v,t: 1,
    # import some modules and save them as class members
    "sys": __import__("sys"),
    "re": __import__("re"),
    "it": __import__("itertools"),
    "__init__": lambda s: [
        None,
        # initialize memory tape
        setattr(s, "mem", [0 for i in range(30000)]),
        # initialize pointer
        setattr(s, "ptr", 0),
        # initialize index (where are we in the code)
        setattr(s, "i", -1)
        # return the 0th element of this list (None), since __init__ must return None
        ][0],
    # this is the method that does all the work, it takes the code as input
    "do": lambda com,code: [ # first, create a list (to loop over code, see below)
        # this lambda gets called on every step
        # first, increase the index by 1
        (lambda: setattr(com, "i" ,com.i+1) or\
            # if the current symbol is '>' or '<', change the pointer accordingly
            (setattr(com, "ptr", com.ptr+1) if code[com.i]==">"\
            else setattr(com, "ptr", com.ptr-1) if code[com.i]=="<"\
            # if the current symbol is '+' or '-', change the memory at the pointer accordingly
            else com.mem.__setitem__(com.ptr, com.mem[com.ptr]+1) if code[com.i]=="+"\
            else com.mem.__setitem__(com.ptr, com.mem[com.ptr]-1) if code[com.i]=="-"\
            # input and output, using sys module
            else com.sys.stdout.write(chr(com.mem[com.ptr])) if code[com.i]=="."\
            else com.mem.__setitem__(com.ptr,ord(com.sys.stdin.read(1))) if code[com.i]==","\
            # move index forward to matching ]
            else setattr(com, "i", com.i +
                # here comes my fancy matching bracket finder
                (lambda string: [i for i in zip([m.start() for m in com.re.finditer('\[',string)][1:]+[len(string)],
                                                [m.start() for m in com.re.finditer(']',string)])\
                    if i[0]>i[1]][0][1])\
                # call the fancy matching bracket finder with the rest of the code if the
                # current symbol is '[' and the pointer points to a 0
                (code[com.i:])) if code[com.i]=="[" and com.mem[com.ptr]==0\
            # move index back to matching [
            else setattr(com, "i", len(code[:(com.i+1)]) -
                # fancy matching bracket finder pt. 2
                (lambda string:[i for i in zip([m.start() for m in com.re.finditer(']',string)][1:]+[len(string)],
                                               [m.start() for m in com.re.finditer('\[',string)])\
                    if i[0]>i[1]][0][1])\
                # call the fancy matching bracket finder with the code until here if the
                # current symbol is ']' and the pointer doesn't point to a 0
                (code[:(com.i+1)][::-1])-2) if code[com.i]=="]" and not com.mem[com.ptr]==0\
            else 1) # dummy else
        # call the outer lambda if there's still code left
        )() if com.i+1<len(code)\
        # exit otherwise
        else com.sys.exit()\
        # endless for loop, imitating a while loop
        for _ in com.it.repeat(0)]
# call the newly created type to make an instance
})()\
# assign that instance to com
as com:\
# call the do method with the code
com.do("".join(
    # only care about the relevant characters
    filter(lambda x:x in "+-[]><.,",
           # open the file that was given as an argument on the command line
           list(open(com.sys.argv[1]).read()))
))
```
