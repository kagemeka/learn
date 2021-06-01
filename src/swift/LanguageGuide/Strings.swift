let someString = "Some string literal value"



var multiLineString = """
This is multi line
string.
"""

print(
  multiLineString
)


multiLineString = """

aaa

---
"""

print(multiLineString)

multiLineString = """
\
aaa\
bbb
"""

print(multiLineString)

func genMultiLineStr(  
) -> String {
  let s = """
  \
  aaa\
  bbb
  """
  return s 
}

print(genMultiLineStr())

/* special characters */

let wiseWords = """
\"Imagination is more \
important than knowledge\" \
- Einstein
"""
print(wiseWords)
let dollarSign = "\u{24}"
let blackHeart = "\u{2665}"
let sparklingHeart = "\u{1F496}"

print(
  dollarSign,
  blackHeart,
  sparklingHeart
)

multiLineString = """
Escaping the first quotation mark ""\"
Escaping all three quotation marks ""\"
"""


print(multiLineString)

multiLineString = #"""
\n """ \\ \r \u{24}
"""#
print(multiLineString)



// partialy don't escape
let s = #"\n \r \#u{24} \\"#
print(s)

print(s.isEmpty)

let exclamationMark: (
  Character
) = "!"
print(
  type(of: exclamationMark)
)

let catCharacters: [
  Character
] = [
  "C",
  "a",
  "t",
  "!",
  "🐱",
]

print(catCharacters)
var catString = String(
  catCharacters
)
print(catString)

catString.append(
  exclamationMark
)
print(catString)




// Grapheme Cluster


// compile error 
// print(catString[0])

// ok 
print(
  catString[catString.index(
    catString.startIndex,
    offsetBy: 4
  )]
)


for i in catString.indices {
  print(
    "\(i): \(catString[i])"
  )
}


