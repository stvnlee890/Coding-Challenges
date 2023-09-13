/*
986. Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [start, end] and secondList[j] = [start, end]. Each list of intervals is pariwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a,b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1,3] and [2,4] is [2,3]

EXAMPLE 1:

input:
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

EXAMPLE 2:
input:
firstList = [[1,3],[5,9]]
secondList = []
Output: []
*/

const firstList = [
  [0, 2],
  [5, 10],
  [13, 23],
  [24, 25],
];
const secondList = [
  [1, 5],
  [8, 12],
  [15, 24],
  [25, 26],
];
// [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

/*
    Initial Questions
    // Is the size of the firstList always going to be the same size as the second other than when secondList is = []

    TIME COMPLEXITY: O(N)
      Iterates through both arrays simultaneously and once
    Space Complexity: O(N)
      Create a new array of N size of input
*/
const intervalIntersection = function(firstList, secondList) {
  if (!firstList.length || !secondList.length) return [];

  const result = []
  let p1 = 0
  let p2 = 0

  while (p1 < firstList.length && p2 < secondList.length) {
    const [start1, end1] = firstList[p1]
    const [start2, end2] = secondList[p2]
    
    if (end1 < start2) {
      p1 ++
    } else if (end2 < start1) {
      p2 ++
    } else {
      const maxVal = Math.max(start1, start2)
      const minVal = Math.min(end1, end2)
      result.push([maxVal, minVal])
      if (end1 < end2) {
        p1 ++
      } else {
        p2 ++
      }
    }
  }
  return result
};


intervalIntersection(firstList, secondList);
