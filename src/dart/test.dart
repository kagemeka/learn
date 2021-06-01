import 'dart:io';
import 'package:characters/characters.dart';
import "package:meta/meta.dart";

// import 'dart:convert';

int a() {
  return 1;
}

void printInterger(int aNumber) {
  print('The number is $aNumber.');
}

void main(List<String> args) {
  print(args);
  for (int i = 0; i < 5; i++) {
    print('hello ${i + 1}');
  }
  print(a());

  // var name = stdin.readLineSync();
  // print(name);

  var number = 42;
  printInterger(number);

  String name = "Bob";
  Object b = 2;
  print(b);

  int lineCount;
  assert(lineCount == null);
  print(lineCount == null);

  final na = 'Alice';
  // na = 'Alicia';
  print('na: $na');

  const int bar = 1 * 9;
  print(bar);
  double d = 1;
  print(d);

  const Object i = 3;
  const list = [i as int];
  const map = {if (i is int) i: 'int'};
  const s = {if (list is List<int>) ...list};
  print(s);
  print(list);
  print(map);

  var hex = 0xDEADBEEF;
  print(hex);

  var exponents = 1.42e5;
  print(exponents);

  double z = 1;
  print(z);

  var one = int.parse('1');
  print(one);

  var onePointZero = double.parse('1');
  print(onePointZero);

  print(1.toString());

  print(3.141592.toStringAsFixed(2));

  print(1 << 5);
  print(1 & 0);
  print(3 ^ 5);

  var multiLineString = '''
  block comments.
  aaaa
  bbbb
  ''';
  print(multiLineString);

  var s1 = 'aaaa' 'bbbb' 'cccc';
  var s2 = 'aaaabbbbcccc';
  assert(s1 == s2);

  var rawString = r'In a raw string, not even \n gets special treatment.';
  print(rawString);

  print(''.isEmpty);
  print('' == null);
  print((0 / 0).isNaN);
  print(0.isNaN);

  var ls = [1, 2, 3];
  print(ls.length);
  ls[0] = 4;
  print(ls);
  var ls2 = ls;
  ls2[0] = 5;
  print(ls2);
  print(ls);

  var ls3 = [100, ...ls];
  print(ls3);
  print([...ls]);
  print([0, ...?ls]);

  var ls4 = [
    for (var i = 0; i < 10; i++)
      for (var j = 0; j < 2; j++) i * 2 + j
  ];
  print(ls4);
  for (var i = 1; i < 2; i++) for (var j = 2; j < 4; j++) print(4);

  Set<String> ss = {};
  ss.addAll(['sdf', 'sadf']);
  print(ss);

  var ss2 = <String>{"asd", 'asdf'};
  print(ss2);

  var mp = Map<String, int>();
  mp['aaa'] = 1;
  print(mp);

  print(mp['bbb']);

  var unicodeString = '\u{1f606}';
  print(unicodeString);
  var hi = 'Hi 🇩🇰';
  print(hi);
  print('The end of the string: ${hi.substring(hi.length - 1)}');
  print('The last character: ${hi.characters.last}\n');

  print(returnTrue());
  print(returnFalse());

  optionalPositional(1, 2, 3, 4);

  ls = [1, 2];
  ls.forEach(print);

  var isEven = (int x) => x&1==1 ? false : true;
  print(isEven(2));
  ls.forEach((x) => x*=2);
  print(ls);

  int j = 1;
  print(j++);
  print(i==j);
  // print(i.==(j));
  print((i as int).bitLength);
  // print((i as double).isNaN);
  j ??= i;
  print(j);

  var p = Point.viceVersa(1, 2);
  print(p.x + p.y);
}

bool returnTrue() {
  return true;
}

bool returnFalse() => false;

// void needNamedParameter(
//     {String s, @required int a}) {
//   print(a);
// }

void optionalPositional(int a, int b, [int c=1, int d]) { 
}


class Point {
  int x, y;
  Point(this.x, this.y);
  Point.viceVersa(this.y, this.x);
}

