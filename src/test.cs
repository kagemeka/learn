/*
string
*/

Console.WriteLine("Hello World!");

string aFriend = "Bill";
Console.WriteLine(aFriend);

aFriend = "Maira";
Console.WriteLine(aFriend);

Console.WriteLine("Hello " + aFriend);

Console.WriteLine($"Hello {aFriend}");

string firstFriend = "Maira";
string secondFriend = "Sage";
Console.WriteLine($"My friends are {firstFriend} and {secondFriend}");

Console.WriteLine($"The name {firstFriend} has {firstFriend.Length} letters.");
Console.WriteLine($"The name {secondFriend} has {secondFriend.Length} letters.");

string greeting = "     Hello World!     ";
Console.WriteLine($"'{greeting}'");
string trimmedGreeting = greeting.TrimStart();
Console.WriteLine($"'{trimmedGreeting}'");
trimmedGreeting = greeting.TrimEnd();
Console.WriteLine($"'{trimmedGreeting}'");
trimmedGreeting = greeting.Trim();
Console.WriteLine($"'{trimmedGreeting}'");

string sayHello = "Hello World!";
Console.WriteLine(sayHello);
sayHello = sayHello.Replace("Hello", "Greetings");
Console.WriteLine(sayHello);

Console.WriteLine(sayHello.ToUpper());
Console.WriteLine(sayHello.ToLower());

string songLyrics = "You say goodbye, and I say hello";
Console.WriteLine(songLyrics.Contains("goodbye"));
Console.WriteLine(songLyrics.Contains("greetings"));
Console.WriteLine(songLyrics.StartsWith("You"));
Console.WriteLine(songLyrics.StartsWith("goodbye"));
Console.WriteLine(songLyrics.EndsWith("hello"));
Console.WriteLine(songLyrics.EndsWith("goodbye"));

Console.WriteLine(true && false);

/*
number 
*/
int a = 18;
int b = 6; int c = a + b;
Console.WriteLine(c);

c = a - b;
c = a * b;
c = a / b;

a = 5; b = 4; c = 2; int d = a + b*c;
Console.WriteLine(d);

d = (a + b) - 6 * c + (12*4) / 3 + 12;
Console.WriteLine(d);

Console.WriteLine((a + b) / c);
Console.WriteLine((a + b) % c);

Console.WriteLine($"The range of integers is {int.MinValue} to {int.MaxValue}");

Console.WriteLine($"The range of long integers is {long.MinValue} to {long.MaxValue}");

int maxInt = int.MaxValue;
Console.WriteLine($"An example of overflow: {maxInt+2}");


