import math

# parenthesis, also called round brackets like "()"
# ==================================================

# can be used to control order of operations
assert (1+2)*3 == 9
assert 1+(2*3) == 7
assert 1+2*3 == 7

# can be used to call functions
assert math.sqrt(81) == 9
assert math.cos(0) == 1
assert math.sin(0) == 0
x = math.sqrt  # no bracket here so function is not called
assert x(9) == 3

# can be used to define functions


def backward_string(val: str) -> str:
    return val[::-1]


# square brackets like "[]"
# =========================

# can be used for defining lists
x = list(range(20))

# can be used to index into lists and strings
assert x[0] == 0
assert x[1] == 1
assert x[2] == 2
assert x[3] == 3
assert x[-1] == 19
assert x[-2] == 18
assert x[-3] == 17
assert x[-4] == 16

assert x[0:3] == [0, 1, 2]
assert x[1:3] == [1, 2]
assert x[2:3] == [2]
assert x[2:6] == [2, 3, 4, 5]

assert x[:4] == [0, 1, 2, 3]  # missing first number means the start
assert x[:1] == [0]

assert x[4:] == [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19]  # missing end number means the end
assert x[1:] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

assert x[:] == x  # [:] means all the list
assert x[::] == x  # [::] means all the list

# the third number when indexing is the number to skip/jump
assert x[::1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] == x
assert x[::2] == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
assert x[::3] == [0, 3, 6, 9, 12, 15, 18]
assert x[::4] == [0, 4, 8, 12, 16]
assert x[::-1] == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert x[::-2] == [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
assert x[::-3] == [19, 16, 13, 10, 7, 4, 1]
assert x[::-4] == [19, 15, 11, 7, 3]

# it is possible to combine these.
# The first number is the start position,
#     when empty it means the start, this is the same as 0
#     when negative it means from the end
# The second number is the end position
#     when empty it means the end, this is the same as -1
#     when negative it means from the end
# The third number is the step size
#     when empty it means 1
#     when negative it means we count backwards
# a good explanation can be found at:
# https://stackoverflow.com/questions/509211/understanding-slice-notation
assert x[0:7:2] == [0, 2, 4, 6]
assert x[:8:2] == [0, 2, 4, 6]
assert x[1:7:2] == [1, 3, 5]
assert x[1:3:1] == [1, 2]
assert x[1:7:2] == [1, 3, 5]
assert x[2:7:2] == [2, 4, 6]


y = ['saya', 'suka', 'apel', 'jeruk', 'mangga', 'anggur', 'strawberry',
     'dan', 'masih', 'banyak', 'lagi']

# can be used to index into lists and strings
assert y[0] == 'saya'
assert y[1] == 'suka'
assert y[2] == 'apel'
assert y[3] == 'jeruk'
assert y[-1] == 'lagi'
assert y[-2] == 'banyak'
assert y[-3] == 'masih'
assert y[-4] == 'dan'

assert y[0:3] == ['saya', 'suka', 'apel']
assert y[1:3] == ['suka', 'apel']
assert y[2:3] == ['apel']
assert y[2:6] == ['apel', 'jeruk', 'mangga', 'anggur']

assert y[:4] == ['saya', 'suka', 'apel', 'jeruk']  # missing first number means the start
assert y[:1] == ['saya']

assert y[4:] == ['mangga', 'anggur', 'strawberry', 'dan', 'masih', 'banyak', 'lagi']  # missing end number means the end
assert y[1:] == ['suka', 'apel', 'jeruk', 'mangga', 'anggur', 'strawberry', 'dan', 'masih', 'banyak', 'lagi']

assert y[:] == y  # [:] means all the list
assert y[::] == y  # [::] means all the list

# the third number when indexing is the number to skip/jump
assert y[::1] == ['saya', 'suka', 'apel', 'jeruk', 'mangga', 'anggur', 'strawberry', 'dan', 'masih', 'banyak', 'lagi'] == y
assert y[::2] == ['saya', 'apel', 'mangga', 'strawberry', 'masih', 'lagi']
assert y[::3] == ['saya', 'jeruk', 'strawberry', 'banyak']
assert y[::4] == ['saya', 'mangga', 'masih']
assert y[::-1] == ['lagi', 'banyak', 'masih', 'dan', 'strawberry', 'anggur', 'mangga', 'jeruk', 'apel', 'suka', 'saya']
assert y[::-2] == ['lagi', 'masih', 'strawberry', 'mangga', 'apel', 'saya']
assert y[::-3] == ['lagi', 'dan', 'mangga', 'suka']
assert y[::-4] == ['lagi', 'strawberry', 'apel']

assert y[0:6:2] == ['saya', 'apel', 'mangga']
assert y[:8:2] == ['saya', 'apel', 'mangga', 'strawberry']
assert y[1:7:2] == ['suka', 'jeruk', 'anggur']
assert y[1:7:1] == ['suka', 'apel', 'jeruk', 'mangga', 'anggur', 'strawberry']
assert y[1:7:3] == ['suka', 'mangga']

z = "Understanding is more important than solving the problem"

# can be used to index into lists and strings
assert z[0] == 'U'
assert z[1] == 'n'
assert z[2] == 'd'
assert z[3] == 'e'
assert z[-1] == 'm'
assert z[-2] == 'e'
assert z[-3] == 'l'
assert z[-4] == 'b'

assert z[0:3] == 'Und'
assert z[1:3] == 'nd'
assert z[2:3] == 'd'
assert z[2:6] == 'ders'

assert z[:4] == 'Unde'    # missing first number means the start
assert z[:1] == 'U'

assert z[4:] == 'rstanding is more important than solving the problem'  # missing end number means the end
assert z[1:] == 'nderstanding is more important than solving the problem'

assert z[:] == z  # [:] means all the list
assert z[::] == z  # [::] means all the list

# the third number when indexing is the number to skip/jump
assert z[::1] == 'Understanding is more important than solving the problem' == z
assert z[::2] == 'Udrtnigi oeipratta ovn h rbe'
assert z[::3] == 'Uetdgso ptth lnt oe'
assert z[::4] == 'Urng epat v  b'
assert z[::-1] == 'melborp eht gnivlos naht tnatropmi erom si gnidnatsrednU'
assert z[::-2] == 'mlopetgilsnh ntom rms ndasen'

assert z[0:6:2] == 'Udr'
assert z[:8:2] == 'Udrt'
assert z[1:7:2] == 'nes'
assert z[1:7:1] == 'nderst'
assert z[:7:3] == 'Uet'
assert z[1::3] == 'nrai  rioa asvghpbm'
assert z[1:7:] == 'nderst'
assert z[2:10:3] == 'dsn'
assert z[3:12:1] == 'erstandin'
assert z[3:12:2] == 'esadn'
assert z[3:12:3] == 'etd'
assert z[3:12:4] == 'ean'
assert z[3:12:5] == 'en'
assert z[::1] == 'Understanding is more important than solving the problem'
assert z[::2] == 'Udrtnigi oeipratta ovn h rbe'
assert z[::3] == 'Uetdgso ptth lnt oe'
assert z[::4] == 'Urng epat v  b'
assert z[::5] == 'Usiseotnvtrm'
assert z[0::5] == 'Usiseotnvtrm'
assert z[1::5] == 'ntn  r  iho'

# curly brackets like "{}"
# ========================
