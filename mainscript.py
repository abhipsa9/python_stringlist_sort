liststrings = ['mallika_1.jpg','dog005.jpg','grandson_2018_01_01.png','dog008.jpg','mallika_6.jpg','grandson_2018_5_23.png','dog01.png','mallika_11.jpg','mallika2.jpg','grandson_2018_02_5.png','grandson_2019_08_23.jpg', 'dog9.jpg', 'mallika05.jpg']

def sortandprint(list_strings):
  indexlist_strings=[]
  originaldict ={}

  for i in list_strings:
    indx = list_strings.index(i)
    indexlist_strings.append(indx)
  
  originaldict = dict(zip(list_strings,indexlist_strings))

  #fundtion to get keys 
  def keylist(dict):
    listnew =[]
    for key in dict.keys():
      listnew.append(key)
    return listnew
  
  #function to get values
  def valueslist(dict):
    valuenew =[]
    for value in dict.values():
      valuenew.append(value)
    return valuenew
  
  # Create your dictionary class 
  class my_dictionary(dict):
    # __init__ function 
    def __init__(self): 
        self = dict()
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
  
  dict_obj = my_dictionary()
  c=0
  listexceptzero =[]
  for key in originaldict:
    s= ""
    for i in key:
      if i != "0" and i!="_" and i!="-":
        s=s+i
    listexceptzero.append(s)
    dict_obj.add(s,c)
    c+=1
  newlistexceptzero =listexceptzero
  newlistexceptzero.sort()

  import re
  def atoi(text):
    return int(text) if text.isdigit() else text
  def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]
  my_list = newlistexceptzero
  my_list.sort(key=natural_keys)

  listofkeysbeforeone =[]
  for i in my_list:
    listofkeysbeforeone.append(dict_obj[i])
  def get_key(val): 
    for key, value in originaldict.items(): 
      if val == value: 
        return key
  
  listfinal = []
  for i in listofkeysbeforeone:
    listfinal.append(get_key(i))
  print("unsorted list")
  print(keylist(originaldict))
  print("final sorted list")
  print(listfinal)

  print("unsorted list------------------------------")
  for i in keylist(originaldict):
    print(i)
  print("sorted list----------------------------------")
  for i in listfinal:
    print(i)

sortandprint(liststrings)
