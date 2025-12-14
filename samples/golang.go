/*
 * Go highlight sample
 */

// Package main
package main

import (
	"fmt"
	alias "fmt"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

//go:generate go tool yacc -o gopher.go -p parser gopher.y

/*
Semantic highlighting:
Generated spectrum to pick colors for local variables and parameters:
 Color#1 SC1.1 SC1.2 SC1.3 SC1.4 Color#2 SC2.1 SC2.2 SC2.3 SC2.4 Color#3
 Color#3 SC3.1 SC3.2 SC3.3 SC3.4 Color#4 SC4.1 SC4.2 SC4.3 SC4.4 Color#5
*/

var x = http.Server{}
var handler http.HandlerFunc

func handl(w http.ResponseWriter, r *http.Request) {}

var hh = http.HandlerFunc(handl)

type handleFunc = http.HandlerFunc
type myInterface = http.Handler

var serve = http.Serve

var y time.Ticker


func do[TypeParameterTyperParameter any]() {
	type Ptr *int
	_ = 1234524123123123123
	_ = "helo\n\n\n\nhelo"
}

type (
	PublicInterface interface {
		PublicFunc() int
		privateFunc() int
	}

	privateInterface interface {
		PublicFunc() int
		privateFunc() int
	}

	PublicStruct struct {
		PublicField  int
		privateField int
		somefunc     func() int
	}

	privateStruct struct {
		PublicField  int
		privateField int
	}

	demoStruct struct {}
	demoError error
	demoInt    int
	demoPointer *int
	demoSlice   []int
	demoMap     map[int]string
	demoFunc   func()
	demoChan    chan int
	demoString string
	demoArr     [5]int
	demoBool   bool

	// T struct {
	// 	FirstName string `json:"first_name" arbitrary text`
	// }
)

const (
	PublicConst  = 1
	privateConst = 2
)

var (
	PublicVar  = 1
	privateVar = 2

	constInt  = demoInt(5)
	constStr  = demoString("hello")
	constStr2 demoString = "hello"
	constBool = demoBool(true)

	constPtr = demoArr{1, 2, 3}
)

// SomeFunc is here
func SomeFunc(param demoBool, param2 demoMap, param3 demoSlice) {
	
}


// PublicFunc does the thing
func PublicFunc() int {
	localVar := PublicVar
	return localVar
}

// privateFunc does the thing
func privateFunc() (int, int) {
	LocalVar := privateVar
	return LocalVar, PublicVar
}

func (ps PublicStruct) PublicFunc() int {
	ps.somefunc()
	return ps.privateField
}

func (ps privateStruct) privateFunc() int {
	return ps.PublicField
}

func tempFunc(f demoFunc) demoFunc {
	f()
	return func() {}
}

func _(pi PublicInterface) {

}

func _(pi privateInterface) {
}

func variableFunc(demo1 int, demo2 demoInt, demo3 demoBool) {
	demo1 = 3
	a := PublicStruct{}
	a.PublicFunc()
	b := privateStruct{}
	b.privateFunc()
	demo2 = 4
	if demo1, demo2 := privateFunc(); demo1 != 3 {
		_ = demo1
		_ = demo2
		return
	}
demoLabel:
	for demo1 := range []int{1, 2, 3, 4} {
		_ = demo1
		continue demoLabel
	}

	switch {
	case 1 == 2:
		demo1, demo2 := privateFunc()
		_ = demo1
		_ = demo2
	default:
		_ = demo1
	}

	f := func() int {
		return 1
	}
	f()
	PublicFunc()
	variableFunc(1, 2)
	_ = demo1
	_ = demo2
	println("builtin function")
}

func main() {
	const LocalConst = 1
	const localConst = 2
	fmt.Println("demo\n\xA")
	alias.Println("demo")
	variableFunc(1, 2, true)
	var d, c *int = nil, nil
	_, _ = c, d
	_, _ = true, false

	_ = "\n\n\n\n\n\n\n\n\n"
	_ = 123456324123123
}

var ExportedVariableFunction = func() {}
var packageLocalVariableFunction = func() {}

type typeWithCall struct {
	PublicFieldCall  func()
	privateFieldCall func()
}

func calls(t typeWithCall) {
	var localVariableFunction = func() {}

	ExportedVariableFunction()
	packageLocalVariableFunction()
	localVariableFunction()
	t.PublicFieldCall()
	t.privateFieldCall()
}

func _() {
	var demoErr demoError
	demoErr = nil
	_ = demoErr
	var err error
	a, err := 1, nil
	println(a, err)

	for a := 0; a < 10; a++ {
		println(a)
	}
}

func withFuncParam(param func() int) func(func() int) int {
	fmt.Println(param)
	param()

	return func(f func() int) int { return 4 }
}
