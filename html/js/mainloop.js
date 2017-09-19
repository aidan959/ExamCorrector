

function qLoader(){
  //VARIABLE DEFINITION
  /**
  //Questions need 
  //1) a question section as a number
  //2) a question's second section as a number
  //3) the question 
  //Possible Method:
  var questions = 
  {
    questionID1: 0,
    questionID2: 0,
    questionSTR: ""
  };
*/
  //Question list(LONG)
  //SAMPLE
  //FROM 2017 PAPER
  var questions=
  [
    {id: 111, question: "How many Sustainable Development Goals are there?"},
    {id: 112, question: "What did the Millennium Development Goals tackle?"},
    {id: 121, question: "Using the information on the webpage, complete the following sentences: In the world () million go hungry everyday. {his includes more than million children who are under five years of age."},
    {id: 122, question: "What is the world’s biggest health problem?"},
    {id: 123, question: "What does Sustainable Development Goal 2 aim to do by 2030"},
    {id: 131, question: "What is needed to reach Sustainable Development Goal 2?"},
    {id: 141, question: "Your CSPE class would like to invite a person from Concern to come to talk to your class about world hunger. Describe two steps that your class would have to take to organise the visit. <br> First Step:"},
    {id: 142, question: "Second Step:"},
    {id: 151, question: "Buzz Aldren, the astronaut who was the second man to walk on the moon, said,  “If we can conquer space we can {onquer world hunger.”  Your CSPE class wants to have a debate with this title.  Give one argument in favour of this {oint of view and one argument against. Argument in favour:"},
    {id: 152, question: "Argument against"}
  ]
  var lastID=0;
  for (var i = 0; i < questions.length; i++){
    var input = document.createElement('input'); 
    var qNumber;
    input.type = "text"; 
   
    //...    
    qNumber = idToNumber(questions[i].id.toString(), lastID);
    //document.getElementsByTagName('questions').innerHTML += "<span id=" + questions[i].id.toString() + ">" + questions[i].question + "</span><br>"; 
    $("#questions").append("<span class=" + "q" + questions[i].id.toString() + "questions " + ">" + qNumber + questions[i].question + "</span><br>");
    lastID=questions[i].id;
  }
  var samplefile="file:///file.txt";
  
  
}

function idToNumber(id, lastID)
{
  var output = null;
  var qNum, qPart, qRNumeral ="";
  var idArray=[];
  var returnVal="";
  var qNum;
  var qPart;
  var qRNumeral;
  var space = " ";
  var oldIDArray=[];
  var tab = "&nbsp";
  lastID=lastID.toString();
  if ($.type(id) === "string"){
   
    try{
      if (id.length==3){
        idArray = strSplt(id, idArray)
        oldIDArray = strSplt(lastID, oldIDArray);
        qNum = idArray[0];
        qPart = idArray[1];
        qRNumeral = idArray[2];
        
        console.log(idArray.join("")); 
        console.log(lastID);
        //Check if is the same base question as not to repeat numbers
        if(idArray[0] != oldIDArray[0]){
          returnVal += char = '0ABCDEFGHIJK'[qNum] + space;
        }
        else{
          returnVal += tab + tab + tab + tab;
        }
        if(idArray[1] != oldIDArray[1]){
        returnVal += char = '01234567'[qPart] + space;
        }
        else{
          returnVal += tab + tab + tab;
        }
        returnVal += ["invalid ID","i","ii", "iii", "iv", "v", "vi", "vii", "viii"][qRNumeral] +space;
        returnVal += ")" + space;
        return(returnVal);
              
    
      }
      else{
        console.log("String is too long or too short.")
      }
    }    
    catch(err) {
      console.log("ID is inputed as an int, or as an invalid type")
    }
  }
  else{
    console.log("The value passed is not string")
    return("NOT A STRING")
  }
}
function strSplt(s, a )
{
  do{ 
    a.push(s.substring(0, 1));
  } 
  while( (s = s.substring(1, s.length)) != "" );
  return(a);
}
qLoader();


//USELESS CODE ATM: SAVED FOR REFERENCE AND POSSIBLE FUTURE USE


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