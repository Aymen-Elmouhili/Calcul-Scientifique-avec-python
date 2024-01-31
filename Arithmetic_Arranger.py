def arithmetic_arranger(problems, answer=False):
  #if (len(problems) > 5):
  #  print("Error: Too many problems.")
  #for elt in problems:
  #  if '+' not in elt and '-' not in elt:
  #    print("Error: Operator must be '+' or '-'.")
  #  else:
  #    parties = elt.split('+' if '+' in elt else '-')
  #    is_digit = all(part.isdigit() for part in parties)
  #    if (is_digit is False):
  #      print("Error: Numbers must only contain digits.")
  #    is_valid = all(len(part) <= 4 for part in parties)
  #    if (is_valid is False):
  #      print("Error: Numbers cannot be more than four digits.")
  #arranged_problems = ""
  #table = []
  #tab_oper = []
  #for elt in problems:
  #  table.append(elt.split('+' if '+' in elt else '-'))
  #  tab_oper.append('+' if '+' in elt else '-')
  #for i in range(0, len(table), 2):
  #  print("  ", table[i], "    ")
  #print("\n")
  #j = 0
  #for i in range(1, len(table), 2):
  #  print(tab_oper[j], " ", table[i], "    ")
  #print("\n")
  #tab_max_size = []
  #for i in range(len(table) - 1):
  #  tab_max_size.append(max(table[i], table[i + 1]))
  #for i in range(len(tab_max_size)):
  #  print(tab_max_size[i] * '-', end="    ")
  #for i in range(0, len(table) - 1, 2):
  #  print(table[i] + table[i + 1], "    ")

  #####################################################

  #if len(problems) > 5:
  #  return "Error: Too many problems."

  #arranged_problems = []
  #for problem in problems:
  #  operand1, operator, operand2 = problem.split()

  #  if operator not in ('+', '-'):
  #    return "Error: Operator must be '+' or '-'."

  #    if not operand1.isdigit() or not operand2.isdigit():
  #      return "Error: Numbers must only contain digits."

  #    if len(operand1) > 4 or len(operand2) > 4:
  #      return "Error: Numbers cannot be more than four digits."

  #   width = max(len(operand1), len(operand2)) + 2  # Add 2 for spacing

  #  arranged_problems.append(f"{operand1.rjust(width)}    ")
  #  arranged_problems.append(f"{operator} {operand2.rjust(width - 2)}    ")
  #  arranged_problems.append("-" * width + "    ")

  #arranged_problems.pop()
  #"".join(arranged_problems)

  # Check the number of problems

  # Check the number of problems
  if len(problems) > 5:
    return "Error: Too many problems."

  first_operand = []
  second_operand = []
  operator = []

  for problem in problems:
    pieces = problem.split()
    first_operand.append(pieces[0])
    operator.append(pieces[1])
    second_operand.append(pieces[2])

  # Check for * or /
  if "*" in operator or "/" in operator:
    return "Error: Operator must be '+' or '-'."

  # Check the digits
  for i in range(len(first_operand)):
    if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
      return "Error: Numbers must only contain digits."

  # Check the length
  for i in range(len(first_operand)):
    if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
      return "Error: Numbers cannot be more than four digits."

  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  for i in range(len(first_operand)):
    if len(first_operand[i]) > len(second_operand[i]):
      first_line.append(" " * 2 + first_operand[i])
    else:
      first_line.append(" " *
                        (len(second_operand[i]) - len(first_operand[i]) + 2) +
                        first_operand[i])

  for i in range(len(second_operand)):
    if len(second_operand[i]) > len(first_operand[i]):
      second_line.append(operator[i] + " " + second_operand[i])
    else:
      second_line.append(operator[i] + " " *
                         (len(first_operand[i]) - len(second_operand[i]) + 1) +
                         second_operand[i])

  for i in range(len(first_operand)):
    third_line.append("-" *
                      (max(len(first_operand[i]), len(second_operand[i])) + 2))

  if answer:
    for i in range(len(first_operand)):
      if operator[i] == "+":
        ans = str(int(first_operand[i]) + int(second_operand[i]))
      else:
        ans = str(int(first_operand[i]) - int(second_operand[i]))

      if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
        fourth_line.append(" " + ans)
      else:
        fourth_line.append(
            " " * (max(len(first_operand[i]), len(second_operand[i])) -
                   len(ans) + 2) + ans)
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(
        second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(
            fourth_line)
  else:
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(
        second_line) + "\n" + "    ".join(third_line)
  return arranged_problems


#---------------------------------------------------------------------------------------------------


#Test
# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
main(['-vv'])

