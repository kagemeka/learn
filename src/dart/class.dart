class Spacecraft {
  String name;
  DateTime? launchDate;


  Spacecraft(
    this.name,
    this.launchDate,
  ) {
  }

  Spacecraft.unlaunced(
    String name,
  ) : this(name, null);

  int? get launchYear => (
    launchDate?.year
  );


  void describe() {
    var launchDate = (
      this.launchDate
    );
    
    if (launchDate != null) {
      int years = (
        DateTime.now()
        .difference(launchDate)
        .inDays
      ) ~/ 365;
      print(years);
    } else {
      print('unlaunched');
    }
  }

}


// inheritance
class Orbiter
extends Spacecraft {
  double altitude;

  Orbiter(
    String name,
    DateTime launchDate,
    this.altitude,
  ) : super(name, launchDate);
}


void main() {
  var voyager = Spacecraft(
    'Voyager I',
    DateTime(1977, 9, 5),
  );
  voyager.describe();

  voyager = Spacecraft.unlaunced('Voyager II');
  voyager.describe();


  var orbiter = Orbiter(
    'aaa',
    DateTime(2000, 1, 1),
    200.1,
  );
  orbiter.describe();
}