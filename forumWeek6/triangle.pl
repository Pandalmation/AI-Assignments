
itsRightTriangle(A, B, C) :-
    % All angles are positive.
    A > 0, B > 0, C > 0,
    
    % Check if one of the angles is 90 degrees.
    (A =:= 90, B + C =:= 90) ;
    (B =:= 90, A + C =:= 90) ;
    (C =:= 90, A + B =:= 90).

