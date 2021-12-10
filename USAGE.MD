I was wondering: if I usually aim to 20, but sometimes miss, and usually I miss for the neighbours of 20 - five and one.

Hence, what is the best cell to aim if you miss a lot but want to get a better result in average.

The answer is - try to hit "the average zone" where cells are not the highest, but the sum of three is the largest 
at the board.

If you run the program you'll get:

[5, 20, 1] | 26 

[20, 1, 18] | 39

[1, 18, 4] | 23

[18, 4, 13] | 35

[4, 13, 6] | 23

[13, 6, 10] | 29

[6, 10, 15] | 31

[10, 15, 2] | 27

[15, 2, 17] | 34

[2, 17, 3] | 22

[17, 3, 19] | 39

[3, 19, 7] | 29

[19, 7, 16] | 42

[7, 16, 8] | 31

[16, 8, 11] | 35

[8, 11, 14] | 33

[11, 14, 9] | 34

[14, 9, 12] | 35

[9, 12, 5] | 26

[12, 5, 20] | 37

Where first column is a set of three. The middle one is your aim cell, left and right cells - the cells you hit if you miss.

The second column is an average result you get, if you try to hit the middle cell.


For instance:

If you always try to hit 20, it looks like [5, 20, 1], because if you miss right - you'll get 1, left - 5. The avg result is 26.

Thus, the least profitable cell to hit is 17 ([2, 17, 3] | 22) because the avg result you may get is 22.

The most profitable is 7! Because if you try to hit 7, you may miss to 19 or 16 and the avg result will be 42.

Of course the representation of the least/most profitable cells are theoretical and will work if you hit each cell with a chance of 33.3%, but anyway, it may work if you are just an amateur in darts and want to have fun with better results.