#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) # O(n)


b) # O(n^2)


c) # O(n)

## Exercise II

# A binary search would be the most applicable in this situation
# Obtain the floor in the middle of the n-story
# check to see if the egg is broken if dropped 1 floor less than the current floor
  # if the egg is broken
      #(top floor is now current floor - 1)
      #Obtain the floor in the middle of the ground floor and current floor (recursive call)
  # if not broken
    # Drop off floor 1 higher
    # if broken
      # return floor 1 higher
    # else
      # (ground floor is now current floor + 1) 
      # Obtain floor between current floor and topfloor (recursive call)
  
  # Runtime == O(log n)