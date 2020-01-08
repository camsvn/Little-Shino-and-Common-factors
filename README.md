# 1) Little Shino and Common factors
Little Shino loves maths. Today her teacher gave her two intergers.  Shino is now wondering how many integers can divide both the numbers. She is busy with her assignments. Help her to solve the problem. 

## Output Format:
Print the **number of common factors** of *a* and *b*.

## Input Constraints:
<img src="https://latex.codecogs.com/gif.latex?1\leq&space;a,b&space;\leq&space;10^{12}" title="1\leq a,b \leq 10^{12}" />

## Sample:
> Input : <img src="https://latex.codecogs.com/gif.latex?$10&space;$15" title="$10 $15" /><br><br>
> Output : <img src="https://latex.codecogs.com/gif.latex?2" title="2" />

## Explanation:
The common factors of <img src="https://latex.codecogs.com/gif.latex?10" title="10" /> and <img src="https://latex.codecogs.com/gif.latex?15" title="15" /> are *1* and *5* thus the output *2*

# 2) Fredo and Array Update
Fredo is assigned a new task today. He is given an *array A* containing *N integers*. His task is to *update* all elements of array to *some minimum value x* , that is, <img src="https://latex.codecogs.com/gif.latex?A[i]=x&space;;&space;1\leq&space;i\leq&space;N" title="A[i]=x ; 1\leq i\leq N" /> such that sum of this new array is strictly greater than the sum of the initial array. Note that x should be as minimum as possible such that sum of the new array is greater than the sum of the initial array.

## Output Format:
The only line of output consists of the value of x.

## Input Constraints:
<img src="https://latex.codecogs.com/gif.latex?1\leq&space;i\leq&space;10^5" title="1\leq i\leq 10^5" /> <br>
<img src="https://latex.codecogs.com/gif.latex?1\leq&space;A[i]\leq&space;1000" title="1\leq A[i]\leq 1000" />

## Sample:
> Input : <img src="https://latex.codecogs.com/gif.latex?$1&space;$2&space;$&space;$3&space;$&space;$4&space;$&space;$5" title="$1 $2 $ $3 $ $4 $ $5" /> <br><br>
> Output : <img src="https://latex.codecogs.com/gif.latex?4" title="4" />

## Explanation:
Initial sum of array <img src="https://latex.codecogs.com/gif.latex?=1&plus;2&plus;3&plus;4&plus;5=15" title="=1+2+3+4+5=15" /> <br>
When we update all elements to *4*, sum of array <img src="https://latex.codecogs.com/gif.latex?=4&plus;4&plus;4&plus;4&plus;4=20" title="=4+4+4+4+4=20" /> which is greater than <img src="https://latex.codecogs.com/gif.latex?15" title="15" />.<br>
Note that if we had updated the array elements to *3*,  which is not greater than <img src="https://latex.codecogs.com/gif.latex?sum=15" title="sum=15" />. So, *4* is the minimum value to which array elements need to be updated.
