package main



type Ints []int 


func (
	a Ints,
) Clone() interface{} {
	n := len(a)
	b := make(Ints, n)
	copy(b, a)
	return b
}


func (
	a Ints,
) Get(i int) interface{} {
	return a[i]
}


func (
	a Ints,
) Len() int {
	return len(a)
}


func (
	a Ints,
) Set(
	i int,
	x interface{},
) { 
	a[i] = x.(int)
}



type AccumulateIF interface {
	Get(int) interface{}
	Len() int
	Set(int, interface{})
}


func Accumulate(
	a AccumulateIF,
	f func(
		x, y interface{},
	) interface{},
) {
	n := a.Len()
	for i := 0; i < n - 1; i++ {
		x := a.Get(i)
		y := a.Get(i + 1)
		a.Set(i + 1, f(x, y))
	}
}


type CumuSum struct {


func main() {
	n := 10 
	a := Ints{1, 2, 3}

}