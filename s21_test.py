def remove_list_item(*, the_list, the_item):
  ''' create new list containing all items, except the_item 
  to be deleted.'''

  new_list = [item for item in the_list if item != the_item]
  return new_list
  
