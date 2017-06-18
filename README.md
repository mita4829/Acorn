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
<li>Integers are represented as 64-bits</li>
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
<li>Cocoa offers full-featured for loops with index variable, condition, and counter, delegate to the responsibility of the code</li>
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
</ul>

How to run: <i>python3 Driver.py \<acornfile.acorn\> </i> An alias command will be added later in the future to streamline everything. 

<b>Documentation of Acorn Language (v2.0)</b>
Acorn is an interpreted language which does not depend upon a compiler. Its only dependence is having Python3 (working up to 3.6) installed on the machine of intended coding. Acorn is very similar to Javascript. A more comprehensive tutorial will be written in the future. 

<b>Syntax</b>
<p>All Acorn files must have the extention of <code>.acorn</code> All statements in Acorn must be finished with a semi-colon (including if statements and functions).</p>

<b>Printing</b>
<p>Printing to the console is simple. <code>print("Hello, World from Acorn!");</code><br>As of Acorn 1.1, Acorn disallows multiple types in call-by-name operations e.g.<code>print("Give me a high "+5);</code> is disallowed. Homogenous-typed values forming an expression are allowed such as <code>print(2.14159+1.0);</code></p> 
<p>Cocoa infers the type of printed values and no longer assumes integers to be floats when printed.</p>
<p>Printing with newline</p>
<code>println("Hi newline");</code>

<b>Conditionals</b>
<p>If statements have similar syntax as Javascript. <br/><code>if(true){ print("This is true!"); }else{ print("This is false"); };</code><br/>The boolean expression being evaluated will be casted to be of type boolean. Expressions to be casted to booleans are <i>Logical Operations and Numbers</i>.</p>

<b>Variables</b>
<p>Declaring variable example <code>var x = 0;</code>variables can be bounded to values or homogenous-typed expressions. Constants have been deprecated from Cocoa</p>
<p>Assigning variables <code>var pi = 3.15; pi = 3.14159;</code></p>

<b>Arrays</b>
<p><code>var fib = [0,1,1,2,3,5,8]; var nthFib = fib[n];</code></p>
<b>Functions</b>
<p>Function declaration cannot be anonymous, and they must be bound to a variable name. All functions are required to return at the end of the function body. Function example: <code>
var f = function(x){
  return 1+x;
};
</code> Calling function f: <code>f(1);</code></p>

<b>Input</b>
<p>Acorn accepts input from the stdin() function. <code>var n = stdin();</code> stdin() automatically infers the type of input. </p>

<b>For Loop</b>
<p>For loops:
<code>for(var i = 0; i<10; i=i+1){ ... }</code>

<b>Casting</b>
<p>Expressions when called with the cast operator <code>~></code> will attempt to cast to the desired type. Upon sucess, the expression will be the new type. Upon failure, a run time error will be thrown</p>
<p>Cocoa supports casting to types: <code>(Int)</code>, <code>(Float)</code>, <code>(Bool)</code>, <code>(String)</code>. 
</p>
<p>Example casting an integer to a string.</p>
<code>var str = "I have "+3~>(String)+" apples."</code> 
<p>Will evaulate to the string being, <code>I have 3.0 apples</code>.</p>

<b>For Each</b>
<p>For loops in Acorn 1.1.1 has be demoted to <code>foreach</code> loops. Foreach loops should be taken advantage for speed when simple iterations are needed.</p>
<code>foreach( <i>var</i> = <i>start</i> <i>closure</i> <i>end</i> ){ ... }</code>
<p><code>var</code> is a local variable only available within the scope of the loop and then destroyed once the loop is finished. <code> start, end</code> are integers that compose the range of the loop. <code>closure</code> can be <code>&lt; or &lt;=</code> in the range.
Example: <br><code> for(i = 0&lt;=9){ print(i); };</code> prints 0 to 9. 
</p>

<b>Bug Fixes</b>
<i>Individuals who find bugs with Acorn will recieve recognition below</i>
<ul>
<li>1.1 Fix string comparison giving false negatives during conditional checks.</li>
<li>1.1.1 Fix strings being handled incorrectly when interpreted which led to negatives during conditional checks.</li>
<li>1.1.1 Fix forloop bodies which did not handle more than one statement.</li>
<li>1.1.1 Fix binary logicial operators which gave incorrect results due to evaluation phase of interpretation.</li>
</ul>
