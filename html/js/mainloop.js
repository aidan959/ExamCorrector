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
    * };  
  **/


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
  fillPage(questions);
  
}
//LOADFTP
try
{
    //Settings required to establish a connection with the server
    this.ftpRequest = FtpWebRequest.Create(new Uri("ftp://www.aidan.ml"));
    this.ftpRequest.Method = WebRequestMethods.Ftp.UploadFile;
    this.ftpRequest.Proxy = null;
    this.ftpRequest.UseBinary = true;
    this.ftpRequest.Credentials = new NetworkCredential("qRequester", "samacora");
 
    //Selection of file to be uploaded
    ff = new FileInfo("questions.txt");//e.g.: c:\\Test.txt
    fileContents = new byte[ff.Length];
 
    //will destroy the object immediately after being used
    using (fr = ff.OpenRead())
    {
        fr.Read(fileContents, 0, Convert.ToInt32(ff.Length));
    }
 
    using ( writer = ftpRequest.GetRequestStream())
    {
        writer.Write(fileContents, 0, fileContents.Length);
    }
    //Gets the FtpWebResponse of the uploading operation
    this.ftpResponse = this.ftpRequest.GetResponse();
    Response.Write(this.ftpResponse.StatusDescription); //Display response
}
catch (webex)
{
    this.Message = webex.ToString();
}

//Runs code once.
qLoader();


//USELESS CODE At The Moment: SAVED FOR REFERENCE AND POSSIBLE FUTURE USE


function readFile(file){
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
          
          questions=allText.split("\n");
          qWID=[];
          questions.forEach(function(line) {
            if(line.includes("[") && line.includes("]")) {
              line.replace("[","")
              line.replace("]","")
              currentID = line;
            }
            else{
              qWID.push({id: currentID.ToInt32, question: line});
            }
            
          }, this);
          return qWID;
        }
      }
    }
    rawFile.send(null);
  }
  /**
  function listCharacters(){
    
  }*/
  