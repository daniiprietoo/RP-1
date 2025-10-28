% dim(n) -> size of the grid
% position(t_id, step, row, col) -> position of each part of the thermometer
% row_restriction(row, count) -> number of filled cells in the row
% col_restriction(col, count) -> number of filled cells in the column

% dim with one value
% fill with two values 

% choice rule for saying a part can be filled or not
{ thermo_segment_filled(T,P) : position(T,P,_,_) }.

% can only fill a segment if the previous ones are filled
% cannot be the case p2 is filled if p1 is not filled
:- not thermo_segment_filled(T,P1), thermo_segment_filled(T,P2), P1 < P2, position(T,P2,_,_), position(T,P1,_,_).

% A position is filled if a segment is filled and it exists
fill(R,C) :- thermo_segment_filled(T,P), position(T,P,R,C).

% Rows and columns restriction count
:- row_restriction(R,K), K != #count {C : fill(R,C)}. % count the filled cells in row R by counting the columns C where filled(R,C) holds
:- col_restriction(C,K), K != #count {R : fill(R,C)}. % count the filled cells in column C by counting the rows R where filled(R,C) holds

#show fill/2.
