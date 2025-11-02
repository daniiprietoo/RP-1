Lab Assignment #1: Thermometers Puzzle

Student Names:
- Alejandro Silva Durán
- Daniel Prieto Diaz

Files Submitted:

- encoder.py: encodes the ASCII puzzles into facts
- thermo.lp: logic program with the rules to solve the problems
- decoder.py (provided)
- drawthermo.py (provided)
- pics/ (provided)

How to run it:

1.  Encode a puzzle:
    python3 encoder.py dom01.txt dom01.lp

2. Solve the puzzle:
    python3 decode.py thermo.lp dom01.lp

    Optionally to save the solution to a file:
    python3 decode.py thermo.lp dom01.lp > sol01.txt

3. Visualize the solution
    python3 drawthermo.py dom01.txt sol01.txt
    
