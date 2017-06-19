![Alt text](https://github.com/mita4829/Acorn/blob/master/CocoaHero.jpg "Cocoa: Acorn 2.0")
# Cocoa : Acorn 2.0
[![Build Status](https://travis-ci.org/mita4829/Acorn.svg?branch=master)](https://travis-ci.org/mita4829/Acorn)
<br/>A simple interpreted programming language built upon Python. 

# What's new in Cocoa
<b>Strings</b>
<ul>
<li>String concatenation</li>
<li>Fix issue in 1.1.1 were strings may become truncated</li>
</ul>
<b>Numbers</b>
<ul>
<li>Integers are represented as 64-bits and can be expanded to 1024-bit</li>
<li>Cocoa can recognize hexidecimal numbers</li>
<li>Fix issue in 1.1.1 were expressions may fail during order of operations</li>
</ul>
<b>Operators</b>
<ul>
<li>Modulo operator</li>
<li>Logical And & Or</li>
<li>Bit And & Or</li>
<li>Bit left & right shift</li>
<li>Bit invert</li>
<li>Fix issue in 1.1.1 were banged and negated expression/value fail to work</li>
<li>Operation order of precdence from lowest to highest: ||, &&, {<,<=,==,>=,>,<<,>>}, {+,-}, {*,/,%,~>}, |, &, {-, !, ~},  (expression)</li>
</ul>
<b>Function</b>
<ul>
<li>Functions may take more than one argument now</li>
<li>Recursive functions can be called within the return statement now</li>
<li>Functions return Null on void return type functions</li>
</ul>
<b>If statements</b>
<ul>
<li>Else if statement are now available in Cocoa</li>
</ul>
<b>For loops</b>
<ul>
<li>Cocoa offers full-featured for loops with index variable, condition, and counter, delegated to the responsibility of the coder</li>
<li>For loops can be nested now</li>
<li>Basic for loops in 1.1.1 have been demoted to foreach loop</li>
</ul>
<b>While loops</b>
<ul>
<li>Cocoa offers while loops</li>
</ul>
<b>Casting</b>
<ul>
Cocoa offers basic casting of variables to other primative types
</ul>
<b>Behavior</b>
<ul>
<li>Acorn is no longer a global-scope language. Lexical scope is now implement in Cocoa.</li>
<li>Boolean are represented as 1s and 0s and no longer true or false respectively. </li>
<li>Integer overflow through any arithmetic will result in INT_MAX 64-bit unsigned to be returned </li>
</ul>
<b>Cocoa</b>
<ul>
<li>Rewritten tokenizer </li>
<li>Rewritten parser</li>
<li>Strict token parsing, prevent dangling lexem</li>
<li>Safer parsing by no longer exposing parser to raw non-foundation values</li>
<li>Parser no longer accesses Cocoa's stack or heap. An environment stack has replaced it for the implementation of lexical scoping</li>
<li>Previoius recursive implementation of Acorn have been rewritten in Cocoa to be loops, reducing the weight on Python</li>
<li>Cocoa takes advantage of improved dictionaries in Python 3.6 as for its implementation of lexical scoping</li>
<li>Cocoa improves the speed of certain tasks. Recursive functions are <code>19%</code> more efficent in Cocoa. Nested for loops were implemented in Acorn 1.1.1 under its environment and tested again Cocoa. Cocoa showed a <code>7%</code> speed improvement.
</ul>

# Documentation of Acorn Language (v2.0)
Acorn is an interpreted language which does not depend upon a compiler. Its only dependence is having Python3 (working up to 3.6) installed on the machine of intended coding. Acorn is very similar to Javascript. A more comprehensive tutorial will be written in the future. 

# How to run

To start coding in Acorn on MacOS, clone or download the Acorn directory onto your desktop. Inside the Acorn folder, run the <code>setup</code> executable, and it should set up an Acorn environment. To test if it's working, create a file on your desktop called <code>Hello.acorn</code> and write a simple 'Hello World' program described below. Navigate through terminal to the file's location and run

```
cocoa Hello.acorn
```

If sucessful, your 'Hello World' program should output:

```
Hello, World from Acorn!
```


<b>Syntax</b>
<p>All Acorn files must have the extention of <code>.acorn</code> All statements in Acorn must be finished with a semi-colon (including if statements and functions).</p>

<b>Printing</b>
<p>Printing to the console is simple. 

```
print("Hello, World from Acorn!");
```

<br>As of Acorn 1.1, Acorn disallows multiple types in call-by-name operations e.g.

```
print("Give me a high "+5);
```

is disallowed. Values in a call-by-name operation must be casted first. Homogenous-typed values forming an expression are allowed such as 

```
print(2.14159+1.0);
```

</p> 
<p>Cocoa infers the type of printed values and no longer assumes integers to be floats when printed.</p>
<p>Printing with newline</p>

```
println("Hi newline");
```

<b>Conditionals</b>
<p>If statements<br/>

```
if(0){ 
  print("This should not be true."); 
}else if(42){ 
  print("The answer to everything?"); 
}else{
  print("Some sort of number that will pass in a multi-dimensional universe...");
};
```

<p>The clause binded to the first If statement will execute if the condition evaulates to true. The condition will first be casted as a boolean. Expression/Values that evualate to true are: booleans that are true, non-zero numbers, non-empty string, logical conditions evaluating to true, and bitwise conditions evaluating to true</p>


<b>Variables</b>
<p>Declaring variable example:

```
var x = 0;
```

variables can be bounded to values or homogenous-typed expressions. Constants have been deprecated from Cocoa</p>
<p>Assigning variables 

```
var pi = 3.15; pi = 3.14159;
```

</p>

<b>Arrays</b>
<p>

```
var fib = [0,1,1,2,3,5,8]; var nthFib = fib[n];
```
Arrays in Cocoa may handle non-homogenous type expressions. An array's size is fix upon declaration. An array may be indexed as given in the example above; array start at index 0. 
</p>
<b>Functions</b>
<p>Function declaration cannot be anonymous; they must be bound to a variable name. All functions are required to return at the end of the function body. Functions may take zero to multiple arugments. Functions return Null on void return-type functions. Function example: 

```
var f = function(x){
  return 1+x;
};
```
Calling function f: 

```
f(1);
```

</p>

<b>Input</b>
<p>Acorn accepts input from the stdin() function. 

```
var n = stdin();
```

stdin() automatically infers the type of input. </p>

<b>For Loop</b>
For loops in Cocoa require the following syntax. It must be given an initial value, followed by a condition, followed by an incrementer. Upon each call to the body, the incrermenter will be re-evalutated, and the condition will be check to determine if the body of the loop will execute again. 
<p>For loops:

```
for(var i = 0; i<10; i=i+1){
  ... 
};
```


<b>Casting</b>
<p>Expressions when called with the cast operator <code>~></code> will attempt to cast to the desired type. Upon sucess, the expression will be the new type. Upon failure, a run time error will be thrown</p>
<p>Cocoa supports casting to types: <code>(Int)</code>, <code>(Float)</code>, <code>(Bool)</code>, <code>(String)</code>. 
</p>
<p>Example casting an integer to a string.</p>

```
var str = "I have "+3~>(String)+" apples."
```

<p>Will evaulate to the string being, <code>I have 3.0 apples</code>.</p>

<b>For Each</b>
<p>For loops in Acorn 1.1.1 has be demoted to <code>foreach</code> loops. Foreach loops should be taken advantage for speed when simple iterations are needed.</p>

```
foreach( i = 0 < 10 ){
  ... 
};
```
<p>A foreach loop initiates a local variable with the given name and accepts a given range composed of integers. Foreach loops may only handle < and <= conditions. </p>

<b>Bug Fixes</b>
<i>Individuals who find bugs with Acorn will recieve recognition below</i>
<ul>
<li>1.1 Fix string comparison giving false negatives during conditional checks.</li>
<li>1.1.1 Fix strings being handled incorrectly when interpreted, which led to negatives during conditional checks.</li>
<li>1.1.1 Fix foreach loop bodies which did not handle more than one statement.</li>
<li>1.1.1 Fix binary logicial operators which gave incorrect results due to the evaluation phase of interpretation.</li>
</ul>
