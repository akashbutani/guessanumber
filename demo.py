#!/usr/bin/python
import random
randomno = random.randint(0,99)
count = 0

print """Content-type:text/html\r\n\r\n"""
print """<html>"""
print """<head>"""
print """<title>Guess the Number</title>"""
print """</head>"""
print """<body>"""
print """Guess any no between 0 to 99 : <input type="text" name="txtGuess" id="txtGuess" maxlength="3">"""
print """<input type="button" name="btnGuess" value="Get Result" id="btnGuess" onclick="checkGuess()">"""
print """<input type="hidden" name="hdRandomNo" id="hdRandomNo" value="%s">""" % (randomno)
print """<input type="hidden" name="hdGuessCount" id="hdGuessCount" value="%s">""" % (count)
print """<p id="outputSection"></p>"""
print """<script type="text/javascript">
function checkGuess(){
	txtGuess = document.getElementById("txtGuess").value;
	outputSection = document.getElementById("outputSection");
	outputSection.innerHTML = "";
	if(isNaN(txtGuess) || txtGuess == ""){
		//alert("Please enter valid Guess no.");
		outputSection.innerHTML = "Please enter valid Guess no.";
		return false;
	}
	txtGuess = parseInt(document.getElementById("txtGuess").value);
	if(txtGuess < 0 || txtGuess > 99){
		//alert("Guess no should be between 0 to 99");
		outputSection.innerHTML = "Guess no should be between 0 to 99";
		return false;
	}

	hdRandomNo = parseInt(document.getElementById("hdRandomNo").value);
	hdGuessCount = parseInt(document.getElementById("hdGuessCount").value);
	var flagWin = false;
	
	if(hdGuessCount < 3){
		if(hdRandomNo < txtGuess && hdGuessCount < 2){
			outputSection.innerHTML = "You should try below guess";
			//alert("You should try below guess");
		}
		else if(hdRandomNo > txtGuess && hdGuessCount < 2){
			outputSection.innerHTML = "You should try above guess";
			//alert("You should try above guess");
		}
		else if(hdRandomNo == txtGuess){
			outputSection.innerHTML = "Hurray! You guess correct no";
			alert("Hurray! You guess correct no");
			flagWin = true;
			location.href = "";
		}
	}
	hdGuessCount += 1;
	document.getElementById("hdGuessCount").value = hdGuessCount;
	if(hdGuessCount > 2 && !flagWin){
		alert("Sorry! You have tried all options. click ok to play again");
		location.href = "";
	}
}
</script>"""
print """</body>"""
print """</html>"""