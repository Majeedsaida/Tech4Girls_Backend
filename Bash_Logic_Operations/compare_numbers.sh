#!/bin/bash
# Script to compare two numbers
 numbers=(6 8)
if (( $[0] > $[1] )); then
  echo "${numbers[0]} is greater than {numbers[1]}."
elif (( $[0] < $[1] )); then
  echo "$[1] is greater than $[0]."
else
  echo "Both numbers are equal."
fi
#!/bin/bash
# Script to compare two numbers
numbers=(6 8)

if (( ${numbers[0]} > ${numbers[1]} )); then
  echo "${numbers[0]} is greater than ${numbers[1]}."
elif (( ${numbers[0]} < ${numbers[1]} )); then
  echo "${numbers[1]} is greater than ${numbers[0]}."
else
  echo "Both numbers are equal."
fi