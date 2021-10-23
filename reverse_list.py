listn = [1,2,3,4,5]

def reverse_list (list_):
  for index in range(len(list_) - 1, -1, -1):
    print list_[index]

reverse_list(listn)