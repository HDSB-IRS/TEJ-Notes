/*-----------------------------------------------------------------------------
 Name:        Some Basics
 Purpose:     To provide a sample program about the basics of Processing

 Author:      Mr. Seidel, C. Brooks-Prenger
 Created:     14-Aug-2018
 Updated:     30-Oct-2025 (Converted to Processing)
-----------------------------------------------------------------------------*/

// Printing the addition of two integers
println(1 + 2);

// Printing of the subtraction of two floats
println(4.3 - 2.1);

// Boolean values
boolean right = true;
boolean wrong = false;
println(right);
println(wrong);

// Two integers to be used for the rest of the program.
int integerOne = 1;
int integerTwo = 2;

// Two float values to be used for the rest of the program.
float floatOne = 3.14;
float floatTwo = 5.3;

// Multiplying two float values.
float productOfFloats = floatOne * floatTwo;
println(productOfFloats);

// Division of two float values.
float quotientOfFloats = floatTwo / floatOne;
println(quotientOfFloats);

// Using integer division on two floats (truncating the decimal)
// Note: Python's 5.3 // 3.14 results in 1.0. 
// int(5.3 / 3.14) in Processing results in 1.
int integerDivisionOfFloats = int(floatTwo / floatOne);
println(integerDivisionOfFloats);

// Using the modulo operator
int moduloOfIntegers = 5 % 2;
println(moduloOfIntegers);

// Converting between floats and integers
println(int(floatOne));     // Prints 3
println(float(integerOne)); // Prints 1.0

// Equation
println((4 * 2) / 8); // Prints 1

//-----------------------------------------------------------------------------
// Receiving input from the user
//-----------------------------------------------------------------------------
// In Processing, user input is not handled with a simple console
// function like Python's.  See later notes about user input.
