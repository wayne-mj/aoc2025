def validate(s):
  sstr = str(s)
  return len(sstr) % 2 == 0 and sstr[:len(sstr)//2] == sstr[len(sstr)//2:]

def part1(src):
  valid = 0
  for x in src:
    l,u = x.split('-')
    l = int(l)
    u = int(u)
    for val in range(l,u+1):
      if validate(val):
        valid += val
  return valid

if __name__ == "__main__":
  import sys
  lines = sys.stdin.read().split(",")
  print(lines)
  print(part1(lines))