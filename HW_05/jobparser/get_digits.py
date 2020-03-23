def get_digits(input):
  output = ''
  for i in filter(str.isdigit, input) : output = output + i
  return output if output else None