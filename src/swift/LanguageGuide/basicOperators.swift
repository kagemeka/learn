/* Assignment */

let a = 10 
var b = 5 
b = a 
print(a)


let (x, y) = (1, 2)

print(x, y, separator: "\n")



/* Arithmetic Operators */
1 + 2 
5 - 3 
2 * 3


print(10.0 / 2)
print(9 / 2)

"Hello, " + "world!"
1 &+ 5 // Overflow Operator

print(-5 % 3)
print(-5 % -3)
print(5 % -3)
// the sign of the remainder is always same as the devidend.


// tuple comparison
print(
  (1, "a") < (1, "b")  
)

// can't compare tuples with seven or more elements.


// ternary coonditional 


var ternaryNum = true ? 1 : 2
print(ternaryNum)


// nil coalescing 


let optNum: Int? = 3

// two below are same.
print(
  optNum != nil ? optNum! : 2 
)

print(
  optNum ?? 2
)


// Range Operators 

for i in 1...5 {
  print(i)
}

for i in 1..<5 {
  print(i)
}


var names = [
  "Anna",
  "kagemeka",
  "Ellipsis",
  "Ugoku chan"
]


for name in names[1...] {
  print(name)
}

let c = names.count
for name in (
  names[..<(c-1)]
) {
  print(name)
}

for name in (
  names[...(c-1)]
) {
  print(name)
}


let range = ...5 

print(
  range.contains(-100),
  range.contains(100)
)


print(
  !true,
  false && true,
  false || true
)


