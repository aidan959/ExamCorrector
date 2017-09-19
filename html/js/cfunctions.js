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