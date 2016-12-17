# Acorn
[![Build Status](https://travis-ci.org/mita4829/Acorn.svg?branch=master)](https://travis-ci.org/mita4829/Acorn)
<br/>A simple interpreted programming language builded upon Python. 

How to run: <i>python3 Driver.py \<acornfile.acorn\> </i> An alias command will be added later in the futre to streamline everything. 

#Documentation of Acorn Language (v1.0)
Acorn is an interpreted language which does not depend upon a compiler. Its only dependence is having Python3 installed on the machine of intended coding. Acorn is very similar to Javascript. A more comprehensive tutorial will be written in the future. 

<b>Syntax</b>
<p>All Acorn files must have the extention of <code>.acorn</code>. All statements in Acorn must be finished with a semi-colon (including if statements and functions)</p>

<b>Printing</b>
<p>Printing to the console is simple. <code>print("Hello, World from Acorn!");</code><br>As of Acorn 1.0, Acorn disallows multiple types in call-by-name operations e.g.<code>print("Give me a high "+5);</code> is disallowed. Homogenous typed values forming an expression are allowed such as <code>print(2.14159+1.0);</code></p> 

<b>Conditionals</b>
<p>If statements have similar syntax. <code>if(true){ print("This is true!");<br/>}else{<br/>print("This is false");<br/>};</code><br/>Acorn does not support else if condition. The boolean expression being evaluated must be a boolean value.</p> 
