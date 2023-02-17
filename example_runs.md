# Example run

Sample input and result of these inputs

## Test case 1:
`9 4 (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)`

* 9 queens with a reach of 4 each
* Initial positions: (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7,2), (8,3)

### Result:
* Starting state:
  * Positions = (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)
  * Conflict count = 4
* Next neighbor states:
  * 1st neighbor:
    * Positions = (1, 7), (2, 4), (3, 8), (4, 1), (4, 6), (5, 5), (6, 2), **(1 2)**, (8, 3)
    * Conflict count = 2
  * 2nd neighbor:
    * Positions = (1, 7), (2, 4), (3, 8), (4, 1), **(7, 6)**, (5, 5), (6, 2), (1 2), (8, 3)
    * Conflict count = 0

* Solution - SOLUTION FOUND
  * Positions: (1, 7), (2, 4), (3, 8), (4, 1), **(7, 6)**, (5, 5), (6, 2), (1 2), (8, 3)
  * Conflict count = 0

* Total number of state transition: **2**

* Total number of state examined: **241**

## Test case 2:
`9 5 (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)`

* 9 queens with a reach of 5 each
* Initial positions: (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7,2), (8,3)

### Result:
* Starting state:
  * Positions = (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)
  * Conflict count = 7
* Next neighbor states:
  * 1st neighbor:
    * Positions = (1, 7), (2, 4), (3, 8), (4, 1), **(4, 8)**, (5, 5), (6, 2), (7, 2), (8, 3)
    * Conflict count = 5
  * 2nd neighbor:
    * Positions = (1, 7), (2, 4), (3, 8), (4, 1), (4, 8), (5, 5), (6, 2), (7, 2), **(8, 6)**
    * Conflict count = 3
  * 3rd neighbor:
    * Positions = (1, 7), (2, 4), (3, 8), (4, 1), (4, 8), (5, 5), **(1, 2)**, (7, 2), (8, 6)
    * Conflict count = 2

* Solution - SOLUTION FOUND
  * Positions: (1, 8), (2, 4), (7, 8), (3, 1), (4, 3), (5, 5), (1, 2), (7 2), (8, 4)
  * Conflict count = 0

* Total number of state transition: **8**

* Total number of state examined: **947**

## Test case 3:
`9 6 (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)`

* 9 queens with a reach of 6 each
* Initial positions: (1, 7), (2, 4), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)

### Result:
* Starting state:
  * Positions = (1, 7), (2, 4), (3, 8), (4, 1), (4, 6), (5, 5), (6, 2), (7, 2), (8, 3)
  * Conflict count = 7
* Next neighbor states:
  * 1st neighbor:
    * Positions = (1, 7), (2, 4), (3, 8), (4, 1), **(7, 6)**, (5, 5), (6, 2), (7, 2), (8, 3)
    * Conflict count = 5
  * 2nd neighbor:
    * Positions = (1, 7), (2, 4), **(4, 8)**, (4, 1), (7, 6), (5, 5), (6, 2), (7, 2), (8, 3)
    * Conflict count = 4
  * 3rd neighbor:
    * Positions = (1, 7), (2, 4), (4, 8), (4, 1), (7, 6), (5, 5), (6, 2), **(1, 2)**, (8, 3)
    * Conflict count = 3
  * 4th neighbor:
    * Positions = **(2, 7)**, (2, 4), (4, 8), (4, 1), (7, 6), (5, 5), (6, 2), (1, 2), (8, 3)
    * Conflict count = 2

* Solution - SOLUTION FOUND
  * Positions: (2, 7), (3, 4), (4, 8), (4, 1), (7, 6), (5, 5), (6, 2), (1, 3), (8, 3)
  * Conflict count = 0

* Total number of state transition: **6**

* Total number of state examined: **721**

## Test case 4:
`10 3 (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7,2),(8,3)`

* 10 queens with a reach of 3 each
* Initial positions: (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)

### Result:
* Starting state:
  * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)
  * Conflict count = 6
* Next neighbor states:
  * 1st neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 6), (5, 5), (6, 2), **(1, 2)**, (8, 3)
    * Conflict count = 4
  * 2nd neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), **(7, 6)**, (5, 5), (6, 2), (1, 2), (8, 3)
    * Conflict count = 2
  * 3rd neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), **(7, 8)**, (5, 5), (6, 2), (1, 2), (8, 3)
    * Conflict count = 2
  * 4th neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (7, 8), (5, 5), (6, 2), (1, 2), **(8, 1)**
    * Conflict count = 2

* Solution - SOLUTION FOUND
  * Positions: (1, 7), (6, 6), (2, 5), (3, 8), (4, 1), (7, 8), (8, 5), (6, 2), (1, 2) (8, 1)
  * Conflict count = 0

* Total number of state transition: **7**

* Total number of state examined: **898**

## Test case 5:
`10 4 (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2),(8, 3)`

* 10 queens with a reach of 4 each
* Initial positions: (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)

### Result:
* Starting state:
  * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)
  * Conflict count = 6
* Next neighbor states:
  * 1st neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), **(1, 2)**, (8, 3)
    * Conflict count = 4
  * 2nd neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 6), **(7, 5)**, (6, 2), (1, 2), (8, 3)
    * Conflict count = 2
  * 3rd neighbor:
    * Positions = (1, 7), **(5, 4)**, (2, 5), (3, 8), (4, 1), (4, 6), (7, 5), (6, 2), (1, 2), (8, 3)
    * Conflict count = 0

* Solution - SOLUTION FOUND
  * Positions: (1, 7), (5, 4), (2, 5), (3, 8), (4, 1), (4, 6), (7, 5), (6, 2), (1, 2), (8, 3)
  * Conflict count = 0

* Total number of state transition: **3**

* Total number of state examined: **390**

## Test case 6:
`10 5 (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 6), (5, 5), (6, 2), (7, 2), (8,3)`

* 10 queens with a reach of 5 each
* Initial positions: (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 6), (5, 5), (6, 2), (7, 2), (8, 3)

### Result:
* Starting state:
  * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 6), (5, 5), (6, 2), (7, 2), (8, 3)
  * Conflict count = 9
* Next neighbor states:
  * 1st neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 6), (5, 5), (6, 2), (7, 2), **(8, 7)**
    * Conflict count = 7
  * 2nd neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), **(8, 6)**, (5, 5), (6, 2), (7, 2), (8, 7)
    * Conflict count = 5
  * 3rd neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (8, 6), (5, 5), **(1, 2)**, (7, 2), (8, 7)
    * Conflict count = 4
  * 4th neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), **(6, 6)**, (5, 5), (1, 2), (7, 2), (8, 7)
    * Conflict count = 3

* Solution - SOLUTION FOUND
  * Positions: (1, 8), (2, 4), (8, 5), (7, 8), (3, 1), (6, 6), (4, 3), (1, 2), (7, 2) (3, 7)
  * Conflict count = 0

* Total number of state transition: **14**

* Total number of state examined: **1809**

## Test case 7:
`10 6 (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7,2),(8,3)`

* 10 queens with a reach of 6 each
* Initial positions: (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7,2),(8,3)

### Result:
* Starting state:
  * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4,6), (5, 5), (6, 2), (7, 2), (8, 3)
  * Conflict count = 9
* Next 4 neighbor states:
  * 1st neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), **(4, 8)**, (5, 5), (6, 2), (7, 2), (8, 3)
    * Conflict count = 7
  * 2nd neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 8), (5, 5), (6, 2), (7, 2), **(8, 6)**
    * Conflict count = 5
  * 3rd neighbor:
    * Positions = (1, 7), (2, 4), (2, 5), (3, 8), (4, 1), (4, 8), (5, 5), **(6, 7)**, (7, 2), (8, 6)
    * Conflict count = 4
  * 4th neighbor:
    * Positions = (1, 7), (2, 4), **(2, 1)**, (3, 8), (4, 1), (4, 8), (5, 5), (6, 7), (7, 2), (8, 6)
    * Conflict count = 4

* Solution - SOLUTION FOUND
  * Positions: (8, 8), (6, 4), (1, 8), (3, 5), (1, 1), (4, 7), (2, 3), (5, 2), (8, 1), (7, 6)
  * Conflict count = 0

* Total number of state transition: **43**

* Total number of state examined: **5456**