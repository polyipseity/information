---
aliases:
  - HKUST COMP 1029P exercise for lesson 3
tags:
  - date/2024/01/16
  - language/in/English
---

# exercise for lesson 3

- HKUST COMP 1029P

<!-- list separator -->

- due: 2024-01-16T23:59:59+08:00
- points: 100
- submitting: a file upload
- file types: py
- available: until 2024-01-16T23:59:59+08:00

## The Game of Life

Now, we are ready to finalize our game of Life.

Your task is to write a function called life\(array, generations\) that takes as input these two parameters:

- a 2-dimensional array \(a list of lists\) representing the first generation of the Life game
- a positive integer indicating the number of future generations that you would like to see.

Then, the function should ___print___ the initial array followed by the arrays of the given number of subsequent generations. Each generation should be printed nicely as shown in the example sequence and videos below. Between each generation, there is a 1 second delay. The screen is cleared before the printing of each generation. Be sure to use the functions that you wrote in the previous sections, i.e.

- neighbors\(\) in [Review Questions 3.1](review%20questions%20-%20lesson%203.1.md), and
- nextgen\(\) in [Review Questions 3.2](review%20questions%20-%20lesson%203.2.md).

## Example Sequence

Here is an example of using life\(\):

```Python
>>> start = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

>>> life(start, 3)

(clear the screen)

Initial generation:


 ###



(delay for 1 second and then clear the screen)

Generation 1:

  #
  #
  #


(delay for 1 second and then clear the screen)

Generation 2:


 ###



(delay for 1 second and then clear the screen)

Generation 3:

  #
  #
  #
```

Here is a video showing the execution of life\(start, 3\) \(recorded in the IDLE environment\):

[game\_of\_life\_start.mp4](attachments/game_of_life_start.mp4.webm) <br/>
![game\_of\_life\_start.mp4](attachments/game_of_life_start.mp4.webm)

And here is a video showing the execution of life\(start, 50\) \(recorded in the IDLE environment\):

[game\_of\_life\_start\_50.mp4](attachments/game_of_life_start_50.mp4.webm) <br/>
![game\_of\_life\_start\_50.mp4](attachments/game_of_life_start_50.mp4.webm)

\(You may find that the speed of execution in the videos are different from the speed of running the function in your machines. Don't worry too much because these videos are just for simple demonstrations. You may also see videos with the same issue in the coming lessons and exercises.\)

You can see that for this particular starting array, the result is a repeating two stage pattern. However, other starting arrays will give very different results, as you will see later.

As you can see in the example above, the arrays are printed using '\#' and ' ' \(space\) instead of 1 and 0. In the starting code below, there is a new function, print\_life\(\), which takes a 2D array as input and prints a '\#' if the cell is a 1 and prints a space otherwise. You do not need to change it. It is already working.

## Starting Code

You may download the code below as your starting code:

[life.py](template/life.py)

## Some Interesting Examples

There are some interesting initial 2D array values that you can try with your life\(\) function:

- tumbler - looks like a moving circus performer
- face - constantly changing eyes, nose and mouth
- glider\_gun - shoots bullets

They are already included in the starting code shown above.

Below we have included videos which shows the results you should get.

As you can see in some of the videos, if we use a delay of only 1 second between each generation, it is sometimes not easy to see how the generations grow and any interesting patterns that appear. For this reasons it helps if we use a shorter delay, so that the changes in the generations are quickly shown. However, please note that a delay shorter than 0.5 second in the IDLE environment usually doesn't work because the 'clear screen by printing 100 empty lines' method typically takes more than 0.5 seconds to work.

Here are links to the example videos.

### Tumbler

- Here is a video showing the result of life\(tumbler, 30\) \(recorded in the IDLE environment, using 1 second delay between each generation\):

  [game\_of\_life\_tumbler\_30.mp4](attachments/game_of_life_tumbler_30.mp4.webm) <br/>
  ![game\_of\_life\_tumbler\_30.mp4](attachments/game_of_life_tumbler_30.mp4.webm)
- Here is a video showing the result of life\(tumbler, 120\) \(recorded in the IDLE environment, using 1/8 second delay between each generation\):

  [game\_of\_life\_tumbler\_120.mp4](attachments/game_of_life_tumbler_120.mp4.webm) <br/>
  ![game\_of\_life\_tumbler\_120.mp4](attachments/game_of_life_tumbler_120.mp4.webm)

### Face

- Here is a video showing the result of life\(face, 30\) \(recorded in the IDLE environment, using 1 second delay between each generation\):

  [game\_of\_life\_face\_30.mp4](attachments/game_of_life_face_30.mp4.webm) <br/>
  ![game\_of\_life\_face\_30.mp4](attachments/game_of_life_face_30.mp4.webm)

- Here is a video showing the result of life\(face, 60\) \(recorded in the IDLE environment, using 1/8 second delay between each generation\):

  [game\_of\_life\_face\_60.mp4](attachments/game_of_life_face_60.mp4.webm) <br/>
  ![game\_of\_life\_face\_60.mp4](attachments/game_of_life_face_60.mp4.webm)

### Glider Gun

- Here is a video showing the result of life\(glider\_gun, 100\) \(recorded in the IDLE environment, using 1 second delay between each generation\)

  [game\_of\_life\_glider\_gun\_100.mp4](attachments/game_of_life_glider_gun_100.mp4.md) <br/>
  ![game\_of\_life\_glider\_gun\_100.mp4](attachments/game_of_life_glider_gun_100.mp4.md)

- Here is a video showing the result of life\(glider\_gun, 500\) \(recorded in the IDLE environment, using 1/8 second delay between each generation\). In this video we used a much bigger glider\_gun arrary with a size of __50x35__ \(the given array has a dimension of 38x11 only\) so that the 'shooting' effect can be demonstrated in the video.

  [game\_of\_life\_glider\_gun\_500.mp4](attachments/game_of_life_glider_gun_500.mp4.md) <br/>
  ![game\_of\_life\_glider\_gun\_500.mp4](attachments/game_of_life_glider_gun_500.mp4.md)

## Testing Your life\(\) Function

To test your life\(\) function, you can open your ___life.py___ file in the IDLE environment. Then execute 'Run Module' by hitting 'F5'. \(In the event that you are using a different environment than IDLE, you can use from life import \* instead, which does the same thing.\)

After that, in the shell, you can use your life\(\) function with the initial 2D array values given to you in the starting code.

For example, you can type in this command:

```Python
>>> life(start, 3)
```

and it should show exactly the 4 generations shown in the example sequence at the very top of this page, with a delay between each generation.

## Submission

You need to write the function life\(\), and the functions it calls in a file called ___life.py___.

In your life.py, include these:

- the neighbors\(\) function, which counts the number of neighbors of a cell
- the nextgen\(\) function, which gives the next generation of the input array
- the print\_life\(\) function, which print one generation in a nice way. You do not need to change this function.
- the life\(\) function
- set up the 2D array start, tumbler, face and glider\_gun as shown in the example sequence above

After you have finished your work, upload your file and then submit by clicking the "Submit Assignment", and then choosing your file to submit.

## submission

- file: [life.py](submission/life.py)
