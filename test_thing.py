import stuff

def inc(x):
  return x+1

def test_answer():
  assert inc(3) == 5

def test_stuff():
  assert stuff.plusOne(3) == 4
  assert stuff.summation(1,1) == 3