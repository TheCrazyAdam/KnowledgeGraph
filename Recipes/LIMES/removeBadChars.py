fname = "output-recipes.ttl"
fname2 = "output-recipes2.ttl"

values = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@:<>/#.;,\"-_ ")

def remover(my_string = ""):
  for item in my_string:
    if item not in values:
      my_string = my_string.replace(item, "")
  return my_string


with open(fname, "r") as fp:
    for line in fp:
        line = line.strip()
        line = remover(line)
        with open(fname2, 'a') as the_file:
            the_file.write(line + '\n')
