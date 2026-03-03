Nogard is a simple dargon fractal curve generator that uses two separate approaches drawn with turtle.

The top block is iterative and maintains an explicit list of 'f' / 'r' / 'l' symbols. Each step it
reverses the list, flips all turns, then concatenates. It build the same fold sequence and replays it with the turtle.

The recursive block [dragoncurve] uses two manually recursive functions (controlled with "# of iterations") that encode the dragon curve as an L-system:

    X(n) = X(n−1) rightY(n−1) forward
    Y(n) = forward X(n−1) left Y(n−1)

with the base case X(0) = Y(0) = ∅. The curve is initiated with one forward step followed by X(n).
Each level or recursion doubles the number of segments, which produces the self-similar fractal structure directly from the call stack rather than an explicit sequence.

Nogard opens its own graphic interface, you can type in the wanted iterations in the command line.
