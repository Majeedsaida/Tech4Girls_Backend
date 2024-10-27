#!/bin/bash
# Script to check logical conditions


numbers=(20 16)

if [[ ${numbers[0]} -gt 10 && ${numbers[1]} -gt 10 ]]; then
  echo "Both numbers are greater than 10."
elif [[ ${numbers[0]} -gt 10 || ${numbers[1]} -gt 10 ]]; then
  echo "At least one number is greater than 10."
else
  echo "Neither number is greater than 10."
fi