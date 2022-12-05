
Objective: 
The objective of this lab assignment is to demonstrate your ability in 
 Managing character strings, and 
 Using string compare function. 
Background Info: 
NASDAQ (National Association of Securities Dealers Automated Quotations exchange) is an 
electronic exchange that investors use to buy and sell stocks. Each company that are traded on 
NASDAQ has stock symbol, e.g., APPL is the stock symbol for Apple Computer, Inc. The stocks 
on NASDAQ can be divided into NNM (Nasdaq National Market) or SCM (the Nasdaq SmallCap 
Market).  The following table lists a few companies that are traded on Nasdaq with their stock 
symbol and market type. 
Company Name Stock Symbol NNM or SCM 
Access Anytime Bancorp, Inc. AABC SCM 
Apple Computer, Inc. AAPL NNM 
MSB Financial, Inc. MSBF SCM 
Microsoft Corporation MSFT NNM 
Tangram Enterprise Solutions, 
Inc. 
TESI SCM 
TESSCO Technologies 
Incorporated 
TESS NNM 
Lab Statement: 
You will write a program in LC-3 assembly code that will do the followings: 
1. Display the prompt: “Please enter a stock symbol:” in the console. 
a. Valid inputs are: AABC, AAPL, MSBF, MSFT, TESI, TESS, and Quit. 
b. User can input these strings in upper case, lower case, or a mixture of upper and 
lower cases. 
2. Get user input. 
a. Read the user input from the keyboard and echo the user input to the console 
one character at a time. 
b. Store the user input as a character string in the memory. 
c. User input ends with a newline character with ascii code x0A. 
3. If the user input is valid then do the following: 
a. If the user input is a valid stock symbol, you will display its market type on the 
console then go to step 1. For example, if the user enters “AAPL”, you will display 
“NNM” on the console then go back to step 1. 
b. If the user enters “quit”, then the program ends. 
4. If the user input is not a valid input as specified in 1-a, the program will display “Input 
not valid.” then go back to step 1. 