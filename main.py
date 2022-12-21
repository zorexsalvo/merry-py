from musicpy import *

# We wish you a merry christmas
c = chord("C4")
c_18 = chord("C4", duration=1/8)
f = chord("F4")
f_18 = chord("F4", duration=1/8)
g = chord("G4")
g_18 = chord("G4", duration=1/8)
e = chord("E4")
e_18 = chord("E4", duration=1/8)
d = chord("D4")
a = chord("A4")
a_18 = chord("A4", duration=1/8)
am = chord("A#4")
am_18 = chord("A#4", duration=1/8)

first_line = (c | f | f_18 | g_18 | f_18 | e_18 | d | d)
second_line = (d | g | g_18 | a_18 | g_18 | f_18 | e | e )
third_line = (e | a | a_18 | am_18 | a_18 | g_18 | f | d)
last_line = (c_18)


last_line = (C('C', duration=1/8) |
             C('C', duration=1/8) |
             C('D') |
             C('G') |
             C('Em') |
             C('F'))

play(first_line | second_line | third_line | last_line)
