#!/bin/bash
# Script to determine age category

read -p "Please enter your age: " age

if (( age < 18 )); then
  echo "You are a minor."
elif (( age >= 18 && age < 65 )); then
  echo "You are an adult."
else
  echo "You are a senior."
fi