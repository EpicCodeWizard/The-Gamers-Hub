def convert_to_human_readable(date):
  parts = date.split("/")
  first = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][int(parts[0].lstrip("0"))-1]
  second = parts[1].lstrip("0")
  third = parts[2]
  return first+" "+second+", "+third
