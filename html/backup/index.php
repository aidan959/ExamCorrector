<?php
include('index.html');
$servername = gethostname();
$dsn = 'mysql:host=localhost;dbname=examcorrector';
$username = "examiner";
$password = "aidan";
$questions = fopen("questions.txt", "r") or die("Unable to open file!");
$ids= array();
$weberrors=array();
$answers=array();
$issue=false;
//Reads the text file line by line
while (!feof($questions)) {
    
    //gets the line
    $line = fgets($questions);
    
    //checks if the line has a [ and ]
    if(strpos($line,'[') !== false and strpos($line,']') !== false){
        
        //removes those brackets
        $line = str_replace("[", "", $line, $i);
        $line = str_replace("]", "", $line, $i);
        
        //pushs the id to the array
        array_push($ids, $line);
        
        //UNCOMMENT TO CHECK IF IT LISTS THE IDS RIGHT
        //echo $line, "<br>";
    }
    
}
//Checks if submit has been pressed
if(isset($_POST['submit'])) {
    //Opens the database connection
    $conn = new PDO($dsn, $username, $password);

    //Gets the examnumber and centre from the site
    $enumber = $_POST['examnumber'];
    $ecnumber = $_POST['examcentre'];
    //gets each id from the array, and uses the id to call from the page
    
    foreach($ids as &$id)
    {
        //checks if ID is empty and 
        if (empty($_POST['q'+$id])){
            echo "empty!";
        }
        else{
            array_push($answers, $_POST['q'+$id]);
        }
        //joins the arrays with a //
        $dbanswers= implode("//", $answers);
    }
    //checks if the important values are empty
    if(empty($enumber) or empty($ecnumber) or $issue == true)
    {
        if(empty($enumber))
        {
            array_push($weberrors,"exam number");
        }
        if(empty($ecnumber)){
            array_push($weberrors,"exam centre");
        }
        //Do something if either are  empty
    }
    else
    {
        $sql = $conn->prepare("INSERT INTO students VALUES ($enumber, '$ecnumber','$dbanswers');");
        $sql->execute();
    }
    foreach($weberrors as &$error)
    echo "<br>","There is an issue with your", $error; 
    
}
?>
