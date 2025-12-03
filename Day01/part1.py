def part1(src):
  dial = 100
  pos = 50
  zeros = 0

  for turn in src:
    tpos = int(turn[1:])
    if turn[0] == "L":
      pos = ((pos - tpos) + dial) % dial
    else:
      pos = (pos + tpos) % dial

    if pos == 0:
      zeros += 1
  
  # print(zeros)
  return zeros


if __name__ == "__main__":
  import sys
  lines = sys.stdin.read().splitlines()
  # print(lines)
  print(part1(lines))