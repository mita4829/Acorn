![Alt text](https://github.com/mita4829/Acorn/blob/master/AcornHero.jpg "Acorn 1.1")
# Acorn
[![Build Status](https://travis-ci.org/mita4829/Acorn.svg?branch=master)](https://travis-ci.org/mita4829/Acorn)
<br/>A simple interpreted programming language built upon Python. 

How to run: <i>python3 Driver.py \<acornfile.acorn\> </i> An alias command will be added later in the future to streamline everything. 

<b>Documentation of Acorn Language (v1.1.1)</b>
Acorn is an interpreted language which does not depend upon a compiler. Its only dependence is having Python3 (working up to 3.6) installed on the machine of intended coding. Acorn is very similar to Javascript. A more comprehensive tutorial will be written in the future. 

<b>Syntax</b>
<p>All Acorn files must have the extention of <code>.acorn</code> All statements in Acorn must be finished with a semi-colon (including if statements and functions). It should be noted as of v1.1, Acorn does not support string concatenation.</p>

<b>Printing</b>
<p>Printing to the console is simple. <code>print("Hello, World from Acorn!");</code><br>As of Acorn 1.1, Acorn disallows multiple types in call-by-name operations e.g.<code>print("Give me a high "+5);</code> is disallowed. Homogenous-typed values forming an expression are allowed such as <code>print(2.14159+1.0);</code></p> 
<p>Acorn 1.1 now infers the type of printed values and no longer assumes integers to be floats when printed.</p>

<b>Conditionals</b>
<p>If statements have similar syntax as Javascript. <br/><code>if(true){ print("This is true!"); }else{ print("This is false"); };</code><br/>Acorn does not support else if conditions. The boolean expression being evaluated will be casted to be of type boolean. Expressions to be casted to booleans are <i>Logical Operations and Numbers</i>. Strings are not allowed to be casted directly to boolean e.g. <code>if("string"){ ... }; will not evaluate correctly.</code></p>

<b>Variables and Constants</b>
<p>As of Acorn 1.1, the language is a dynamic-scope langauge. It is recommended to not use the same variable name anywhere in the Acorn code regardless of scope due to dynamic-scoping; otherwise, declaration of the same variable name will result in overwriting the previous value stored in memory bound to that variable name. Declaring variable example <code>var x = 0;</code>variables can be bounded to values or homogenous-typed expressions. Declaring constant example <code> const e = 2.718; </code></p>
<p>Assigning variables <code>var pi = 3.15; pi = 3.14159;</code></p>

<b>Arrays <i>(beta)</i></b>
<p>Acorn 1.1.1 now provides semi-mutable arrays. Example: <code>var fib = [0,1,1,2,3,5,8]; var nthFib = fib[n];</code></p>
<b>Functions <i>(beta)</i></b>
<p>Functions are limited in v1.1. Function declaration cannot be anonymous, and they must be bound to a variable name. All functions are required to return at the end of the function body. Functions currently take only one arguments. Function example: <code>
var f = function(x){
  return 1+x;
};
</code> Calling function f: <code>f(1);</code></p>
<p>If a function does not take any argument, then it must be supplemented with a <code>Void</code> argument and parameter. Example: <code>var pi = function(Void){ return 3.14159; }; pi(Void);</code></p>
<p><b>Scoping:</b> Due to the nature of Acorn being a big-step interpreter, variables and constants defined in the scope of the function will also exist outside of the scope.  <b>Recursion:</b>Acorn v1.1 handles some recursion with the restriction that all return statement in a recursive function cannot contain the function name. Example of a recrusive function: <code> var factorial = function(x){
  if(x == 0){
    return 1;
  };
  var fact = factorial(x-1);
  return x*fact;
};
</code> </p>

<b>Input</b>
<p>Acorn accepts input from the stdin() function. <code>var n = stdin();</code> stdin() automatically infers the type of input. </p>

<b>For Loop</b>
<p>Acorn 1.1 now can preform basic for loop. Nested for loops are currently not available. For loops have simple syntax.
<code>for(<i>var</i> = <i>start</i> <i>closure</i> <i>end</i>){ ... }</code>
<p><code>var</code> is a local variable only available within the scope of the loop and then destroyed once the loop is finished. <code> start, end</code> are integers that compose the range of the loop. <code>closure</code> can be <code>&lt; or &lt;=</code> in the range.
Example: <br><code> for(i = 0&lt;=9){ print(i); };</code> prints 0 to 9. 
</p>

<b>Misc Error</b>
<i>Anyone who finds these errors, please report your code to me for acknowledgment.</i>
<p>Error 0x00000001: Parser most likely handled an unexpected raw value.</p>
<p>Error 0xdeadbeef: Parser received something it could not handle. (rare)</p>

<b>Bug Fixes</b>
<i>Individuals who find bugs with Acorn will recieve recognition below</i>
<ul>
<li>1.1 Fix string comparison giving false negatives during conditional checks.</li>
<li>1.1.1 Fix strings being handled incorrectly when interpreted which led to negatives during conditional checks.</li>
<li>1.1.1 Fix forloop bodies which did not handle more than one statement.</li>
<li>1.1.1 Fix binary logicial operators which gave incorrect results due to evaluation phase of interpretation.</li>
</ul>
