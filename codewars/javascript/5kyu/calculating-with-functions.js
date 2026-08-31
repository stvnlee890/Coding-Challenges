/*
 * This time we want to write calculations using functions and get the results. Let's have a look at some examples:
 *
 * seven(times(five()));   //  must return 35
 * four(plus(nine()));     //  must return 13
 * eight(minus(three()));  //  must return 5
 * six(dividedBy(two()));  //  must return 3
 * 
 * There must be a function for each number from 0 ("zero") to 9 ("nine")
 * There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
 * Each calculation consist of exactly one operation and two numbers
 * The most outer function represents the left operand, the most inner function represents the right operand
 * Division should be integer division. For example, this should return 2, not 2.666666...:
 * */

// HELPER
function parseAndOperate(left, right) {
  const parse = right.split(" ")
  const operation = parse[0]
  const rightVal = parse[1]
  const rightNum = parseInt(rightVal)

  if (operation === '-') {
    return left - rightNum
  }
  if (operation === '+') {
    return left + rightNum
  }
  if (operation === '*') {
    return left * rightNum
  }
  if (operation === '/') {
    return Math.trunc(left / rightNum)
  }
}

// OPERATIONS
function times(rightVal) {
  return `* ${rightVal}`
}

function plus(rightVal) {
  return `+ ${rightVal}`
}

function minus(rightVal) {
  return `- ${rightVal}`
}

function dividedBy(rightVal) {
  return `/ ${rightVal}`
}

function zero(arg = null) {
  if (!arg) return 0
  else {
    return parseAndOperate(0, arg)
  }
}

function one(arg = null) {
  if (!arg) return 1
  else {
    return parseAndOperate(1, arg)
  }
}

function two(arg = null) {
  if (!arg) return 2
  else {
    return parseAndOperate(2, arg)
  }
}

function three(arg = null) {
  if (!arg) return 3
  else {
    return parseAndOperate(3, arg)
  }
}

function four(arg = null) {
  if (!arg) return 4
  else {
    return parseAndOperate(4, arg)
  }
}

function five(arg = null) {
  if (!arg) return 5
  else {
    return parseAndOperate(5, arg)
  }
}

function six(arg = null) {
  if (!arg) return 6
  else {
    return parseAndOperate(6, arg)
  }
}

function seven(arg = null) {
  if (!arg) return 7
  else {
    return parseAndOperate(7, arg)
  }
}

function eight(arg = null) {
  if (!arg) return 8
  else {
    return parseAndOperate(8, arg)
  }
}

function nine(arg = null) {
  if (!arg) return 9
  else {
    return parseAndOperate(9, arg)
  }
}

console.log(zero(times(one())))
console.log(zero(plus(one())))
console.log()

