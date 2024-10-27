#!/bin/bash


number=20


if (( number % 2 == 0 )); then
  echo "The number $number is even."
else
  echo "The number $number is odd."
fi
