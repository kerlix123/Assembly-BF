def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "whl:": temp_bracestack.append(position)
    if command == "end":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap

f = open("test.abf", "r")

code = f.read().split("\n")

print(code)
cells, codeptr, cellptr = [0], 0, 0
bracemap = buildbracemap(code)

while codeptr < len(code):
  spl = code[codeptr].replace("    ", "").split(" ")
  if spl[0] == "mov":
      if spl[1] == ">":
          cellptr += int(spl[2])
          if cellptr >= len(cells):
              for _ in range(0, cellptr):
                  cells.append(0)

      if spl[1] == "<":
          cellptr = 0 if cellptr <= 0 else cellptr - int(spl[2])

  if spl[0] == "inc":
    cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

  if spl[0] == "dec":
    cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

  if spl[0] == "out":
      print(chr(cells[cellptr]))

  if spl[0] == "inp":
      cells[cellptr] = ord(input())
  if spl[0] == "whl:" and cells[cellptr] == 0: codeptr = bracemap[codeptr]

  if spl[0] == "end" and cells[cellptr] != 0: codeptr = bracemap[codeptr]

  codeptr += 1
