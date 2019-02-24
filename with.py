class Sample:
  def __enter__(self):
    print("In __enter__()")
    return "Foo"
 
  def __exit__(self, type, value, trace):
    print(f"In __exit__()")
 
def get_sample():
  return Sample()

class Sample_2:
  def __enter__(self):
    return self
    
  def __exit__(self, type, value, trace):
    print(f"In __exit__(), type:{type}, value:{value}, trace:{trace}")
 
  def do_something(self):
    bar = 1/0
    return bar + 10
 
with Sample_2() as sample:
  sample.do_something()
  # In __exit__(), type:<class 'ZeroDivisionError'>, value:division by zero, trace:<traceback object at 0x10ca6fa88>

with get_sample():
  print("sample is end")
# In __enter__()
# sample is end
# In __exit__()

with get_sample() as sample:
    print("sample:", sample)
# In __enter__()
# sample: Foo
# In __exit__()

