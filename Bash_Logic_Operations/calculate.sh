#!/bin/bash
 
  numbers=(2 3 4) 
  sum=$(( numbers[0] + numbers[1] ))
  product=$(( sum * numbers[2] ))

  echo "The sum of ${numbers[0]} and ${numbers[1]} is: $sum"
echo "Multiplying the sum by ${numbers[2]} gives: $product"