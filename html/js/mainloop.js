//MAIN FUNCTION
function qLoader() {
  //VARIABLE DEFINITION
  /**
  * Questions need 
  * 1) a question section as a number
  * 2) a question's second section as a number
  * 3) the question 
  * Possible Method:
  * var questions = 
  * {
  *  questionID1: 0,
  *  questionID2: 0,
  *  questionSTR: ""
  * };  **/


  //Question list(LONG)
  //SAMPLE
  //FROM 2017 PAPER
  //{ id: sampleINT, question: "Sample" }
  var questions =
    [

      { id: 111, question: "How many Sustainable Development Goals are there?" },
      { id: 112, question: "What did the Millennium Development Goals tackle?" },
      { id: 121, question: "Using the information on the webpage, complete the following sentences: In the world () million go hungry everyday. {his includes more than million children who are under five years of age." },
      { id: 122, question: "What is the world’s biggest health problem?" },
      { id: 123, question: "What does Sustainable Development Goal 2 aim to do by 2030" },
      { id: 131, question: "What is needed to reach Sustainable Development Goal 2?" },
      { id: 141, question: "Your CSPE class would like to invite a person from Concern to come to talk to your class about world hunger. Describe two steps that your class would have to take to organise the visit. <br> First Step:" },
      { id: 142, question: "Second Step:" },
      { id: 151, question: "Buzz Aldren, the astronaut who was the second man to walk on the moon, said,  “If we can conquer space we can {onquer world hunger.”  Your CSPE class wants to have a debate with this title.  Give one argument in favour of this {oint of view and one argument against. Argument in favour:" },
      { id: 152, question: "Argument against" }

    ]

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
    lastID = questions[i].id;
  
  }
}

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
//Runs code once.
qLoader();


//USELESS CODE At The Moment: SAVED FOR REFERENCE AND POSSIBLE FUTURE USE


/**function readFile(file){
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET",file,false)
    rawFile.onreadystatechange
    = 
    function ()
    {
      if(rawFile.readyState===4)
      {
        if(rawFile.statuts === 200 || rawFile.status == 0)
        {
          var allText=rawFile.responseText;
          alert(allText);
        }
      }
    }
    rawFile.send(null);
  }
  function listCharacters(){
    
  }**/