% crime.pl

% Sample suspects
person( ).
person(susan).
person(alice).
person(bob).

% Facts: crime(CrimeType, Location, Time, Person)
crime(murder, warehouse, night, john).
crime(theft, market, afternoon, susan).
crime(arson, office, morning, alice).
crime(fraud, old_factory, night, bob).

% Motives
motive(john, murder).
motive(susan, theft).
motive(alice, arson).
motive(bob, fraud).

% Presence (crime scene attendance)
presence(john, warehouse, night).
presence(john, old_factory, morning).
presence(susan, market, afternoon).
presence(alice, office, afternoon).
presence(bob, warehouse, night).

% Weapon possession
weapon(john).

% Alibi - no alibi facts
no_alibi(john).
no_alibi(bob).

% Points for each factor
points(motive, 35).
points(presence, 30).
points(weapon, 20).
points(no_alibi, 15).

% Calculate score and justifications
score(Person, CrimeType, Location, Time, TotalScore, Justifications) :-
    findall(Justification-Points, justification(Person, CrimeType, Location, Time, Justification, Points), List),
    sum_points(List, TotalScore),
    findall(Justification, member(Justification-_, List), Justifications).

sum_points([], 0).
sum_points([_-P|T], Sum) :-
    sum_points(T, Rest),
    Sum is P + Rest.

% Justification rules returning text and points
justification(Person, CrimeType, _, _, 'Had motive (+35 points)', 35) :-
    motive(Person, CrimeType).

justification(Person, _, Location, Time, Factor, 30) :-
    presence(Person, Location, Time),
    format(atom(Factor), 'Was at crime scene (~w, ~w) (+30 points)', [Location, Time]).

justification(Person, _, _, _, 'Had relevant weapon/item (+20 points)', 20) :-
    weapon(Person).

justification(Person, _, _, _, 'No specific alibi (+15 points)', 15) :-
    no_alibi(Person).
