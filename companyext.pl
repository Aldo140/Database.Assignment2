%-------------------------------------------------------------
% Facts:
employee(john).
employee(franklin).
employee(alicia).
employee(jennifer).
employee(ramesh).
employee(joyce).
employee(ahmad).
employee(james).


salary(john, 30000).
salary(franklin, 40001).
salary(alicia, 25000).
salary(jennifer, 43000).
salary(ramesh, 38000).
salary(joyce, 25000).
salary(ahmad, 25000).
salary(james, 55000).


department(john, research).
department(franklin, research).
department(alicia, administration).
department(jennifer, administration).
department(ramesh, research).
department(joyce, research).
department(ahmad, administration).
department(james, headquarters).


supervise(franklin, john).
supervise(franklin, ramesh).
supervise(franklin, joyce).
supervise(jennifer, alicia).
supervise(jennifer, ahmad).
supervise(james, franklin).
supervise(james, jennifer).


female(alicia).
female(jennifer).
female(joyce).
female(jayne).

male(john).
male(franklin).
male(ramesh).
male(ahmad).
male(james).


project(productx).
project(producty).
project(productz).
project(computerization).
project(reorganization).
project(newbenefits).

works_on(john, productx, 32).
works_on(john, producty, 8).
works_on(ramesh, productz, 40).
works_on(joyce, productx, 20).
works_on(joyce, producty, 20).
works_on(franklin, producty, 10).
works_on(franklin, productz, 10).
works_on(franklin, computerization, 10).
works_on(franklin, reorganization, 10).
works_on(alicia, newbenefits, 30).
works_on(alicia, computerization, 10).
works_on(ahmad, computerization, 35).
works_on(ahmad, newbenefits, 5).
works_on(jennifer, newbenefits, 20).
works_on(jennifer, reorganization, 15).
works_on(james, reorganization, 10).


%-------------------------------------------------------------
% Rules
superior(X,Y) :- supervise(X,Y).

subordinate(X,Y) :- superior(Y,X).

% Should you need to write new rules, please enter them here.

supreme_chief(SupremeChief) :- supervise(SupremeChief, _), supervise(_, SupremeChief).

%-------------------------------------------------------------
% Queries
% Q1: female, computerization with an effort of 10 hours per week, and that have jennifer as a supervisor? If so, list them.
% A: result is Alicia
?- female(Employee), works_on(Employee, computerization, 10), supervise(jennifer, Employee). 

% Q2: Who is the employee who makes over 40000 dollars a year and works at the research department?
% A: The Employee is Franklin

?- salary(Employee, Amount), Amount > 40000, department(Employee, research). 

% Q3: Who is the supreme chief of this fictional company (aka the President)
% A: Franklin is the Supreme Chief

?- supreme_chief(SupremeChief). 


% Q4: Who are the individuals that work on project productx with an *effort* of 20 or more hours a week?
% A: John works on productx more than 20 hours a week

?- works_on(Individual, productx, Hours), Hours >= 20. 



