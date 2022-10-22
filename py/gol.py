# Game Of Life
# CSCI 77800
# consulted: ThinkPython
import random as r
import time


# board
def buildBoard(numRows, numCols):
  board = []
  for x in range(numRows):
    row = []
    for y in range(numCols):
      row.append(randomState())
    board.append(row)

  return board


def randomState():
  v = r.random()
  prob = 0.8

  if (v > prob):
    return 1
  else:
    return 0


# print the board
def printBoard(board):
  alive = "X"
  dead = "O"
  for row in board:
    rowString = ""
    for col in row:
      if col == 0:
        rowString += dead
      else:
        rowString += alive

    print(rowString)
  print()
  print("----------")
  print()


# set each cell
def setCell(b, r, c, v):
  b[r][c] = v


# check neighboring cells
def countNeighbors(b, r, c):
  count = 0

  for i in range(r - 1, r + 2, 1):
    for j in range(c - 1, c + 2, 1):

      # only check valid indeces and don't count cell being checked
      if validIndex(b, i, j) and not (i == r and j == c):

        count += b[i][j]

  return count


# check if index is valid
def validIndex(l, r, c):
  if 0 <= r < len(l) and 0 <= c < len(l[r]):
    try:
      l[r][c]
      return True
    except IndexError:
      return False
  else:
    return False


def getNextCell(l, r, c):
  nextValue = l[r][c]
  count = countNeighbors(l, r, c)

  if nextValue:
    if count < 2 or count > 3:
      nextValue = 0
  else:
    if count == 3:
      nextValue = 1

  return nextValue


def getNextBoard(l):
  nextBoard = [x[:] for x in l]

  for r in range(len(l)):
    for c in range(len(l[r])):
      nextBoard[r][c] = getNextCell(l, r, c)

  return nextBoard


board = buildBoard(10, 10)

while True:
  printBoard(board)
  board = getNextBoard(board)
  time.sleep(1)
