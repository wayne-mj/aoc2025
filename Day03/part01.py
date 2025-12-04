def part1(lines):
  sum = 0
  for line in lines:
    bank = [int(l) for l in line]
    ub = max(bank[:-1])
    lb = max(bank[bank.index(ub)+1:])
    
    # l = len(line)
    # count = 0
    # pos = 0
    # ub = 0
    
    # while count < l - 1:
    #   if int(line[count]) > ub:
    #     ub = int(line[count])
    #     pos = count
    #     # print(line[count])
    #   count += 1
    
    # count = pos + 1
    # lb = 0
    # while count < l:
    #   if int(line[count]) > lb:
    #     lb = int(line[count])
    #     pos = count
    #   count += 1

    sum = sum + (ub * 10) + lb
    print (f"{ub}{lb} {sum}")
    
  return sum

if __name__ == "__main__":
  import sys
  lines = []
  lines = sys.stdin.read().splitlines()
  # print(lines)
  print(part1(lines))