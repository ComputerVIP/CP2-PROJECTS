#Vincent Johnson, Degubbing notes
import sys
import trace

def tracecls(frame, event, arg):
    if event == 'call':
        print(f'Call to {frame.f_code.co_name} on line {frame.f_lineno} of {frame.f_code.co_filename}')
    return tracecls

sys.settrace(tracecls)
tracer = trace.Trace(count=False, trace=True)

'''
What is tracing?
    Following how the code runs and what it does.

    python -m trace --^^^^^ (path to file)

    --trace (displays lines as called)
    --count (displays how many times a line is called)
    --listfuncs (displays functions as they are called)
    --trackcalls (displays functions and their arguments and relationships between functions)

What are some ways we can debug by tracing?
    Seeing what it does, where it goes, and what it runs
How do you access the debugger in VS Code?
    F5, or run with debug
What is testing?
    Running the code and inputting different values to see if it works
What are boundary conditions?
    Conditions at the endge of the allowed inputs, (e.g. if the allowed inputs are 1 and 100, boundary conditions would be 1 and 100)
How do you handle when users give strange inputs?
    Use try and except blocks
'''

def subtract(a, b):
    return a - b

def add(a, b):
    print(subtract(a, b))
    return a + b

print(add(1, 2))