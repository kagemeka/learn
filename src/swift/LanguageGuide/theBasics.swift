var
  x = 1,
  y = 2

print(x)

print(abs(x))

let input = readLine(
  strippingNewline: true
)
print(input!)




let constInt: Int
constInt = 1

print(constInt)



var red, gree, blue: Double

let あ: String = "a"
print(あ) 



let `import` = "reserved"
print(`import`)
// avoid as possible



print(x, terminator: " ")
print("terminator")


print(Int.max)



/* Floating Point Numbers
Double: 64bit 
Float: 32bit 

Double is preferred.
 */




let decimalSevenTeen = 17
let binarySevenTeen = 0b10001
let octalSevenTeen = 0o21 
let hexadecimalSevenTeen = 0x11
print(
  decimalSevenTeen,
  binarySevenTeen,
  octalSevenTeen,
  hexadecimalSevenTeen
)



let decimalExp = 121.875e-1
// 121.875 * 10^(-1)
let haxadecimalExp = 0xC.3p0 
// 12.1875 * 2^0
print(
  decimalExp,
  haxadecimalExp,
  separator: "\n"
)


// formatting Numeric literals
let paddedDouble = 000123.456
let oneMillion = 1_000_000
let justOverOneMillion = (
  1_000_000.000_000_1
)





typealias AudioSample = UInt16
print(AudioSample.max)

let floatNumber = Float(3)
print(type(of: floatNumber))




// tuples 

let http404Error = (
  404, 
  "Not Found"
)

let (
  statusCode,
  statusMessage
) = http404Error 
// decompose 

print(statusCode)

let (
  justTheStatusCode,
  _ 
) = http404Error


print(
  http404Error.0,
  http404Error.1
)

// print(http404Error[0])
// compile error 



// named tuple 
let http200Status = (
  statusCode: 200,
  description: "OK"
)

print(
  http200Status.statusCode,
  http200Status.description
)


/* Optionals */


let strNum = "123"
let optNum = Int(strNum)
print(optNum)
// this type is not "Int" but "Int?"

var serverResponseCode: Int? = 
  404 

serverResponseCode = nil 
// nil is not a pointer to a nonexsistent object, but is the absense of a value.

print(serverResponseCode)

var surveyAnswer: String? 
print(surveyAnswer)


if (optNum != nil) {
  print(
    "some integer: ",
    optNum!
  )
}

if let n = Int(strNum) {
  print(n)
} else {
  "\(strNum) cannot be converted to an integer"
}



if 
let first = Int("4"),
let second = Int("42"),
(
  first < second
  && second < 100
) {
  print(
    "\(first) < \(second) < 100"
  )
}



// Implicitly Unwrapped Optionals 


let assumedString: String! = (
  "An implicitly unwrapped optional string."
)


print(assumedString + " no ")
let implicitString: String = (
  assumedString
)
// no ! needed 

print(type(of: implicitString))

let optionalString = (
  assumedString
)
print(type(of: optionalString))



/* Error Handling */

var age = -3 
// assert(
//   age >= 0,
//   "A person's age can't be less than zero."  
// )
// only at debug


precondition(
  age >= 0
)
// at both debug and release