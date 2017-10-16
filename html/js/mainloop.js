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
      { id: 121, question: "Using the information on the webpage, complete the following sentences: In the world () million go hungry everyday. This includes more than million children who are under five years of age." },
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

//Runs code once.
qLoader();



//TEXT FILE READ USING HTTP, IMPORTANT TO CHANGE WHERE FROM!
function LoadFile(){

  
}
//USELESS CODE At The Moment: SAVED FOR REFERENCE AND POSSIBLE FUTURE USE\
function readFile(file){
    $.get("http://www.whatever.com/foo.txt", null, function(response){
      $("#theTextArea").val(response); // where theTextArea is the ID of the textarea you want to put the data into.
    });
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
  
/*function getQuestions(){

  //LOADFTP
 
      //Settings required to establish a connection with the server
      this.ftpRequest = this.ftpWebRequest.Create("ftp://192.168.1.6/files/questions.txt");
      this.ftpRequest.Method = WebRequestMethods.Ftp.DownloadFile;
      this.ftpRequest.Proxy = null;
      this.ftpRequest.UseBinary = true;
      this.ftpRequest.Credentials = new NetworkCredential("examcorrector", "ADow@9064");
  
      //Selection of file to be uploaded
      ff = new FileInfo("files/questions.txt");//e.g.: c:\\Test.txt
      
  
     response = request.GetResponse();  
      
      responseStream = response.GetResponseStream();  
      reader = new StreamReader(responseStream);  
      Console.WriteLine(reader.ReadToEnd());  

      Console.WriteLine("Download Complete, status {0}", response.StatusDescription);  

      reader.Close();  
      response.Close();    

  

}*/