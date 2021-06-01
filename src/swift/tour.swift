print("Hello, world!")


var myVariable = 42 
myVariable = 50 
let myConstant = 42

let implicitInterger = 70 
let implicitDouble = 70.0 
let explicitDouble: Double = 
  70

print(explicitDouble)

let explicitFloat: Float = 4.0

print(explicitFloat)



let label = "The width is "
let width = 94

let widthLabel = 
  label + String(width)

let apples = 3 
let oranges = 5 
let appleSummary =
  "I have \(apples) apples."

let fruitSummary =
  "I have \(apples + oranges) pieces of fruit."


print(fruitSummary)



let name = "ellipsis"
let greet = 
  "Hello \(name)! \(0.3 + 5)"

print(greet)


let quatation = """
I said "I have \(apples + oranges) pieces of fruit."
"""

print(quatation)


var shoppingList = [
  "catfish",
  "water",
  "tulips",
]

print(shoppingList)

shoppingList[1] =
  "bottle of water"


var occupations = [
  "Malcolm": "Captain",
  "Kaylee": "Mechanic",
]

occupations["Jayne"] = 
  "Public Relations"


shoppingList.append(
  "blue paint"
)

print(shoppingList)
print(occupations)


// way to initialize
let emptyAarray = [String]()
let emptyDictionary = [
  String: Float
]()

/* another initialization */
shoppingList = []
occupations = [:]




/* Control Flow */

let individualScores = [
  75, 43, 103, 87, 12,
]

var teamScore = 0 
for s in individualScores {
  if s > 50 {
    teamScore += 3
  } else {
    teamScore += 1
  }
}

print(teamScore)


var optionalString: String? = 
  "Hello"

print(optionalString == nil)

var optionalName: String? = 
  "John Appleseed"

var greeting = "Hello!"

if let name = optionalName {
  greeting = "Hello, \(name)"
}


var nickname: String? = nil 
var fullName: String = 
  "John Applessed"

var informalGreeting = 
  "Hi \(nickname ?? fullName)"

print(informalGreeting)



let vegetable = "red pepper"
switch vegetable {
case "celery":
  print("Add some raisins and make ants on a log.")

case "cucumber", "watercress":
  print("That would make a good tea sandwich.")

case let x where x.hasSuffix(
  "pepper"
):
  print("Is it a spicy \(x)?")

default:
  print("Everything tastes good in soup.")
}


let interestingNumbers = [
  "Prime": [
    2, 3, 5, 7, 11, 13,
  ],
  "Fibbonacci": [
    1, 1, 2, 3, 5, 8,
  ],
  "Square": [
    1, 4, 9, 16, 25,
  ],
]

var largest = 0 
for (kind, a) in 
  interestingNumbers {
  for n in a {
    if n > largest {
      largest = n
    }
  }
}

print(largest)


var n = 2 
while n < 100 {
  n *= 2 
}
print(n)

var m = 2 
repeat {
  m *= 2
} while m < 100

print(m)


var total = 0
for i in 0..<4 {
  total += 1
}
print(total)


for i in 0...4 {
  total += 1
}
print(total)





/* Functions / Closures */

func greet(
  person: String,
  day: String
) -> String {
  return "Hello \(person), today is \(day)."
}

greet(
  person: "Bob", 
  day: "Monday"
)


func greet(
  _ person: String,
  on day: String
) -> String {
  return "Hello \(person), today is \(day)."
}

greet("John", on: "Wednesday")


func calculatesStatistics(
  scores: [Int]
) -> (
  min: Int, 
  max: Int,
  sum: Int
) {
  var min = scores[0]
  var max = scores[0]
  var sum = 0
  for score in scores {
    if score > max {
      max = score
    } else if score < min {
      min = score
    }
    sum += score 
  }
  return (min, max, sum)
}


let scores = [
  5, 3, 100, 4, 7,
]
let s = calculatesStatistics(
  scores: scores
)
print(s.sum)
print(s.2)




// nested functions
func returnFifteen() -> Int {
  var y = 10
  func add() {
    y += 5
  }
  add()
  return y 
}


func makeIncrementer() -> (
  (Int) -> Int
) {
  func addOne(
    number: Int
  ) -> Int {
    return 1 + number
  }
  return addOne
}

var increment = makeIncrementer() 
print(increment(7))


// function as argument
func hasAnyMatches(
  list: [Int], 
  condition: (Int) -> Bool
) -> Bool {
  for item in list {
    if condition(item) {
      return true
    }
  }
  return false
}

func lessThanTen(
  number: Int 
) -> Bool {
  return number < 10 
}

var numbers = [29, 19, 7, 12]
hasAnyMatches(
  list: numbers,
  condition: lessThanTen
)

numbers = numbers.map({
  (n: Int) -> Int in 3 * n 
})

print(numbers)

numbers = numbers.sorted{
  $0 > $1
}

print(numbers)



class Shape {
  var numberOfSides = 0
  func simpleDescription(
  ) -> String {
    return "A shape with \(numberOfSides) sides."
  }
}

let shape = Shape()
shape.numberOfSides = 10
print(
  shape.simpleDescription())



class NamedShape {
  var numberOfSides: Int = 0
  var name: String 

  init(name: String) {
    self.name = name
  }

  func simpleDescription(
  ) -> String {
    return "A shape with \(numberOfSides) sides."
  }
}

let nShape = NamedShape(
  name: "aaa"
)

print(
  nShape.simpleDescription()
)



class Square: NamedShape {
  var sideLength: Double 
  
  init(
    sideLength: Double,
    name: String
  ) {
    self.sideLength = 
      sideLength
    super.init(name: name)
    numberOfSides = 4 
  }

  func area() -> Double {
    return 
      sideLength * sideLength 
  }

  override func 
    simpleDescription(
  ) -> String {
    return "A square with sides of length \(sideLength)."
  }
}


let test = Square(
  sideLength: 5.2,
  name: "my tset square"
)

print(test.area())

print(test.simpleDescription())



// experiment 
import Glibc 

class Circle: NamedShape {
  var radius: Double

  init(
    radius: Double,
    name: String
  ) {
    self.radius = radius
    super.init(name: name)
    numberOfSides = 1
  }

  func area() -> Double {
    return Double.pi *
      radius * radius
  }
}

let circle = Circle(
  radius: 4,
  name: "my test circle"
)

print(circle.area())




class EquilateralTriangle:
NamedShape {
  var sideLength: Double = 0.0 

  init(
    sideLength: Double,
    name: String
  ) {
    self.sideLength = 
      sideLength 
    super.init(name: name)
    numberOfSides = 3
  }

  var perimeter: Double {
    get {
      return 3.0 * sideLength
    }
    set {
      sideLength = 
        newValue / 3.0
      // newValue is implicit 
    }
  }

  override func
  simpleDescription(
  ) -> String {
    return "An equilateral triangle with sides of length \(sideLength)."
  }
}

var triangle = 
  EquilateralTriangle(
    sideLength: 3.1,
    name: "a triangle"
  )

print(triangle.perimeter)
triangle.perimeter = 9.9 
print(triangle.sideLength)


class TriangleAndSquare {
  var triangle:
    EquilateralTriangle {
    willSet {
      square.sideLength = 
        newValue.sideLength
    }
  }
  var square: Square {
    willSet {
      triangle.sideLength = 
        newValue.sideLength
    }
  }

  init(
    size: Double, 
    name: String
  ) {
    square = Square(
      sideLength: size,
      name: name 
    )
    triangle = 
        EquilateralTriangle(
      sideLength: size,
      name: name  
    )
  }
}


var tas = TriangleAndSquare(
  size: 10,
  name: "another test shape"
)

print(tas.square.sideLength)
print(tas.triangle.sideLength)
tas.square = Square(
  sideLength: 50,
  name: "larger square"
)

print(
  tas.triangle.sideLength
)



// Optional Value 
let optionalSquare: Square? = 
  Square(
    sideLength: 2.5,
    name: "optional Square"
  )

let sideLength = 
  optionalSquare?.sideLength 



print(sideLength)




// Enumerations and structures

enum Rank: Int {
  case ace = 1
  case two, three, four, five,
    six, seven, eight, nine,
    ten
  case jack, queen, king

  func simpleDescription(

  ) -> String {
    switch self {
    case .ace:
      return "ace"
    case .jack:
      return "jack"
    case .queen:
      return "queen"
    case .king:
      return "king"
    default:
      return String(
        self.rawValue)
    }
  }
}

let ace = Rank.ace 
let aceRawValue = ace.rawValue
print(aceRawValue)


if let convertedRank = Rank(
  rawValue: 3
) {
  let threeDescription =
    convertedRank
    .simpleDescription()
}

enum Suit {
  case 
    spades, 
    hearts,
    diamonds, 
    clubs

  func simpleDescription(
  ) -> String {
    switch self {
    case .spades:
      return "spades"
    case .hearts:
      return "hearts"
    case .diamonds:
      return "diamonds"
    case .clubs:
      return "clubs"
    }
  }

  func color() -> String {
    switch self {
    case .spades, .clubs:
      return "black"
    default:
      return "white"
    }
  }
}

var suit = Suit.spades
print(suit.color())
print(suit.simpleDescription())

suit = Suit.diamonds
print(suit.color())

suit = Suit.clubs
print(suit.color())




enum ServerResponse{
  case result(String, String)
  case failure(String)
}

let success = ServerResponse.result(
  "6:00 am",
  "8:00 pm"
)

let failure = ServerResponse
.failure(
  "Out of cheese."
)

switch success {
case let .result(
  sunrise,
  sunset
):
  print(
    "Sunrise is at \(sunrise) and sunset is at \(sunset)."
  )
case let .failure(msg):
  print("Failure... \(msg)")
}




// Struct 

struct Card {
  var rank: Rank 
  var suit: Suit
  func simpleDescription(
  ) -> String {
    return "The \(rank.simpleDescription()) of \(suit.simpleDescription())"
  }
}

let threeOfSpades = Card(
  rank: .three,
  suit: .spades
)

let threeOfSpadesDescription = 
  threeOfSpades
  .simpleDescription()

print(threeOfSpadesDescription)


/* Rrotocols and Extensions */

protocol ExampleProtocol {
  var simpleDescription:
      String {
    get
  }
  mutating func adjust()
}


class SimpleClass:
ExampleProtocol {
  var simpleDescription:
  String = "A very simple class."
  var anotherProperty:
  Int = 69105
  func adjust() {
    simpleDescription += " Now 100% adjusted."
  }


}

var a = SimpleClass()
a.adjust()
let aDescription = 
  a.simpleDescription

struct SimpleStructure:
ExampleProtocol {
  var simpleDescription:
  String = "A simple structure"
  mutating func adjust() {
    simpleDescription += 
    " (adjusted)"
  }
}

var b = SimpleStructure()
b.adjust() 
let bDescription = 
  b.simpleDescription


print(bDescription) 

extension Int: ExampleProtocol {
  var simpleDescription: 
  String {
    return "The number \(self)"
  }

  mutating func adjust() {
    self += 42
  }
}

print(7.simpleDescription)

// able to use the protocol name like any other named type
let protocolValue: ExampleProtocol = a

print(protocolValue.simpleDescription)

// but cannot access methods outside the protocol definition 

// so this would occur an error
// print(protocolValue.anotherProperty)





/* Errord Handling */



enum PrinterError: Error {
  case outOfPaper 
  case noToner 
  case onFire 
}


func send(
  job: Int,
  toPrinter printerName: String
) throws -> String {
  if (
    printerName == 
      "Never Has Toner"
  ) {
    throw PrinterError.noToner
  }
  return "Job sent"
}



do {
  let printerResponse = 
    try send(
      job: 1040,
      toPrinter: "Bi Sheng"
    )
    print(printerResponse)
} catch {
  print(error)
}


do {
  let printerResponse = 
   try send(
     job: 1040,
     toPrinter: "Never Has Toner"
   )
   print(printerResponse)
} catch {
  print(error)
}



// mutliple catch blocks 
do {
  let printerResponse = 
    try send(
    job: 1440,
    toPrinter: "Gutenberg"
  )
  throw PrinterError.onFire
  print(printerResponse)
} catch PrinterError.onFire {
  print(
    "I'll just put this over here, with the rest of the fire."
  )
} catch let printerError 
  as PrinterError {
  print(
    "Printer Error: \(printerError)."
  )
} catch {
  print(error)
}



let printerSuccesss = 
  try? send(
  job: 1884,
  toPrinter: "Mergethaler"
)

let printerFailure = 
  try? send(
  job: 1885,
  toPrinter: "Never Has Toner"
)



// print(printerSuccess)
print(printerFailure)




var fridgeIsOpen = false
let fridgeContent = [
  "milk",
  "eggs",
  "leftovers"
]

func fridgeContains(
  _ food: String
) -> Bool {
  fridgeIsOpen = true 
  defer {
    fridgeIsOpen = false
  }

  let result = fridgeContent
    .contains(
    food
  )
  return result
}

fridgeContains("banana")
print(fridgeIsOpen)



// Generic
func makeArray<Item>(
  repeating item: Item,
  numberOfTimes: Int
) -> [Item] {
  var result = [Item]()
  for _ in 0..<numberOfTimes {
    result.append(item)
  }
  return result 
}


print(makeArray(
  repeating: "knock",
  numberOfTimes: 5
))



enum OptionalValue<T> {
  case none
  case some(T)
}

var possibleInteger:
  OptionalValue<Int> = .none 

possibleInteger = .some(100)

print(possibleInteger)


func anyCommonElements<
  T: Sequence,
  U: Sequence
>(
  _ lhs: T,
  _ rhs: U
) -> (
  Bool
) where 
  T.Element: Equatable,
  T.Element == U.Element
{
  for l in lhs {
    for r in rhs {
      if l != r {continue}
      return true
    }
  }
  return false
}

print(anyCommonElements(
  [1, 2, 3],
  [4]
))

nickname = "kagemeka"
fullName = "John Appleseed"
informalGreeting = "Hi \(nickname ?? fullName)"

print(informalGreeting)



print(Rank(rawValue: 1))