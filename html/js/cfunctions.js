var allIDS=[];
var qAnswers=[];
//COMMON FUNCTIONS
function idToNumber(id, lastID) {
  //variable declration
  var output = null;
  var qNum, qPart, qRNumeral = "";
  var idArray = [];
  var returnVal = "";
  var qNum = "";
  var qPart = "";
  var qRNumeral = "";
  var space = " ";
  var oldIDArray = [];
  var tab = "&nbsp";
  lastID = lastID.toString();
  //makes sure value is string to bypass errors
  if ($.type(id) === "string") {
    //makes sure code can run
    try {
      //makes sure id format is correct
      if (id.length == 3) {

        //splits the ids into arrays of strings for ease of access
        idArray = strSplt(id, idArray)
        oldIDArray = strSplt(lastID, oldIDArray);

        //sets the qNum qPart and qRNumeral respectivly
        //Main Question Identifier
        qNum = idArray[0];

        //Secondary Identifier
        qPart = idArray[1];

        //final identifier
        qRNumeral = idArray[2];

        //debug logs the variables
        console.debug(idArray.join(""));
        console.debug(lastID);



        //Check if is the same base question as not to repeat numbers (primarily for neatness)
        //checks if the id is the same as the old one
        if (idArray[0] != oldIDArray[0]) {
          returnVal += char = '0ABCDEFGHIJK'[qNum] + space;
        }
        else {
          returnVal += tab + tab + tab + tab;
        }
        //checks if the id is the same as the old one
        if (idArray[1] != oldIDArray[1]) {
          returnVal += char = '01234567'[qPart] + space;
        }
        else {
          returnVal += tab + tab + tab;
        }
        //Appends I, II etc to question
        returnVal += ["invalid ID", "i", "ii", "iii", "iv", "v", "vi", "vii", "vii"][qRNumeral];
        //formats the ) onto the string and adds a space for a flusher design.
        returnVal += ")" + space;

        //Sets the global variable for easy access to IDS
        
        //returns the value of the function to the caller

        return (returnVal);


      }
      else {
        console.log("String is too long or too short.")
      }
    }
    catch (err) {
      console.log("ID is inputed as an int, or as an invalid type")
    }
  }
  else {
    console.log("The value passed is not string")
    return ("NOT A STRING")
  }
}
function strSplt(s, a) {
  do {
    a.push(s.substring(0, 1));
  }
  while ((s = s.substring(1, s.length)) != "");
  return (a);
}
/** function rFile(file){
 *    var rawFile = new XMLHttpRequest();
 *    rawFile.open("GET", file, false);
 *    rawFile.onreadystatechange = function ()
 *    {
 *        if(rawFile.readyState === 4)
 *        {
 *            if(rawFile.status === 200 || rawFile.status == 0)
 *            {
 *                var allText = rawFile.responseText;
 *                alert(allText);
 *            }
 *        }
 *    }
 *    rawFile.send(null);
 *}
**/
//FILE READER
function readFile(file){
    
    var file = this.files[0];
    var fileLines = [];
    var qID;
    var qQuestion;
    var questions = [
       
    ];
    var reader = new FileReader();
    reader.onload = function(progressEvent){
    // Entire file
    console.log(this.result);

    // By lines
    var lines = this.result.split('\n');
    for(var line = 0; line < lines.length; line++){
        fileLines.push(lines[line]);
        qID = lines[line].substring(0,2);
        qQuestion = lines[line].substring(3);
        questions.push({qID:ID, qQuestion:question})
        
        
    }
    };
    reader.readAsText(file);
    
}
function fillPage(questions){
    //old ID for design
  var lastID = 0;
  //code that displays the questions on the website with their id.
  for (var i = 0; i < questions.length; i++) {
    //variable decleration
    var qNumber;

    //the function that finds the ID
    qNumber = idToNumber(questions[i].id.toString(), lastID);
    /**
     * redundant
     * document.getElementsByTagName('questions').innerHTML += "<span id=" + questions[i].id.toString() + ">" + questions[i].question + "</span><br>"; */
    $("#questions").append("<span class=" + "\"q" + questions[i].id.toString() + " questionid\" " + ">" + qNumber +"</span><span class=" + "\"q" + questions[i].id.toString() + " question\" " + ">"+ questions[i].question + "</span><br>");
    $("#questions").append("<input class=\"input\" type=\"text\" id=\""+questions[i].id.toString()+"\" placeholder=\"Your Answer\"autocomplete=off name=\" " + questions[i].id.toString() + "\" /><br>")
    lastID = questions[i].id;
    
  }
  for (var i = 0; i < questions.length;i++){
    allIDS.push(questions[i].id);
}
}
function submitAnswers(){
    console.log(allIDS);
    for (var i=0; i < allIDS.length; i++){
        qAnswers.push(document.getElementById(allIDS[i].toString()).value);
        console.log(qAnswers[i]);
    }
}
