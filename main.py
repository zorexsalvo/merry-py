from musicpy import *


# We wish you a merry christmas
first_line = (C('C') |
              C('F') |
              C('F', duration=1/8) |
              C('G', duration=1/8) |
              C('F', duration=1/8) |
              C('Em', duration=1/8) |
              C('D') |
              C('D'))

second_line = (C('D') |
               C('G') |
               C('G', duration=1/8) |
               C('Am', duration=1/8) |
               C('G', duration=1/8) |
               C('F', duration=1/8) |
               C('Em') |
               C('Em'))

third_line = (C('Em') |
              C('Am') |
              C('Am', duration=1/8) |
              C('A#m', duration=1/8) |
              C('Am', duration=1/8) |
              C('G', duration=1/8) |
              C('F') |
              C('D'))

last_line = (C('C', duration=1/8) |
             C('C', duration=1/8) |
             C('D') |
             C('G') |
             C('Em') |
             C('F'))

play(first_line | second_line | third_line | last_line)
