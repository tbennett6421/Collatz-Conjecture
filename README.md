# Collatz-Conjecture

## Overview
This program will iterate over `number (n)` in the range `initial (i)` to `stop (s)`. For each number in the range, this will compute whether `n` collapses into the `4-2-1 loop`. Optionally, we can print out the length of the computed chain or the chain itself.

## Background
The Collatz Conjecture is a famous unsolved problem in mathematics. It involves a simple process:
* Start with any positive integer n.
* If n is even, divide it by 2.
* If n is odd, multiply it by 3 and add 1.
* Repeat the process with the new value.

The conjecture states that no matter what positive integer you start with, the sequence will eventually reach 1.
Despite its simplicity, no one has been able to prove this for all integers — or find a counterexample.

f(n) = { n / 2       if n is even
         3n + 1      if n is odd
}

One such chain, starting from n=6:
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
