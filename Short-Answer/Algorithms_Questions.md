# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n): # O(n)
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n): # O(n^2)
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies): # O(n)
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

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

