def hello_name(name):
  return "Hello"+ " " + name + "!"

def make_abba(a, b):
  return a + b +b+a

def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

def make_out_word(out, word):
    return out[:2] + word + out[2:]
  
def extra_end(str):
      return str[len(str)-2:] +str[len(str)-2:]+str[len(str)-2:]
  
def first_two(str):
    return str[:2]
  
def first_half(str):
    if len(str) % 2 ==0:
      return  str[:len(str)/2]
    else:
        return str

def without_end(str):
  return str[1:len(str)-1]
  

def combo_string(a, b):
    if len(a) > len(b):
        return b+a+b
    elif len(b) > len(a):
        return a+b+a
      
def non_start(a, b):
    return a[1:len(a)]+b[1:len(b)]

def left2(str):
  return str[2:] + str[:2]
