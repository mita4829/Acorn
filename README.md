![Alt text](https://github.com/mita4829/Acorn/blob/master/AcornHero.jpg "Acorn 1.0")
# Acorn
[![Build Status](https://travis-ci.org/mita4829/Acorn.svg?branch=master)](https://travis-ci.org/mita4829/Acorn)
<br/>A simple interpreted programming language builded upon Python. 

How to run: <i>python3 Driver.py \<acornfile.acorn\> </i> An alias command will be added later in the future to streamline everything. 

#Documentation of Acorn Language (v1.0)
Acorn is an interpreted language which does not depend upon a compiler. Its only dependence is having Python3 installed on the machine of intended coding. Acorn is very similar to Javascript. A more comprehensive tutorial will be written in the future. 

<b>Syntax</b>
<p>All Acorn files must have the extention of <code>.acorn</code> All statements in Acorn must be finished with a semi-colon (including if statements and functions). It should be noted as of v1.0, Acorn does not support string concatenation.</p>

<b>Printing</b>
<p>Printing to the console is simple. <code>print("Hello, World from Acorn!");</code><br>As of Acorn 1.0, Acorn disallows multiple types in call-by-name operations e.g.<code>print("Give me a high "+5);</code> is disallowed. Homogenous-typed values forming an expression are allowed such as <code>print(2.14159+1.0);</code></p> 

<b>Conditionals</b>
<p>If statements have similar syntax as Javascript. <br/><code>if(true){ print("This is true!"); }else{ print("This is false"); };</code><br/>Acorn does not support else if conditions. The boolean expression being evaluated will be casted to be of typed boolean. Expressions to be casted to booleans are <i>Logical Operations and Numbers</i>. Strings are not allowed to be casted directly to boolean e.g. <code>if("string"){ ... }; will not evaluate correctly.</code></p>

<b>Variables and Constants</b>
<p>As of Acorn 1.0, the language is a dynamic-scope langauge. It is recommended to not use the same variable name anywhere in the Acorn code regardless of scope due to dynamic-scoping, otherwise, declaration of the same variable name will result in overwriting the previous value stored in memory bound to that varible name. Declaring variable example <code>var x = 0;</code>varibales can be bounded to values or homogenous-typed expressions. Declaring constant example <code> const e = 2.718; </code></p>

<b>Functions <i>(beta)</i></b>
<p>Functions are limited in v1.0. Function declarion cannot be anonymous and must be bound to a variable name. All functions are required to return at the end of the function body. Functions currently take only one arguments. Function example: <code>
var f = function(x){
  return 1+x;
};
</code> Calling function f: <code>f(1);</code> </p>
<p><b>Scoping:</b> Due to the nature of Acorn being a big-step interpreter, variables and constants defined in the scope of the function will also exist outside of the scope.  <b>Recursion:</b>Acorn v1.0 handles some recursion with the restriction that all return statement in a recursive function cannot contain the function name. Example of a recrusive function: <code> var factorial = function(x){
  if(x == 0){
    return 1;
  };
  var fact = factorial(x-1);
  return x*fact;
};
</code> </p>

<b>Input</b>
<p>Acorn accepts input from the gets() function. <code>var n = gets();</code> gets() automatically infers the type of input. </p>
