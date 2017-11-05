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
while (!feof($questions)) {
    $line = fgets($questions);
    if(strpos($line,'[') !== false){
        $line = str_replace("[", "", $line, $i);
        $line = str_replace("]", "", $line, $i);
        array_push($ids, $line);
        //CHECKS IF IT LISTS THE IDS RIGHT
        //echo $line, "<br>";
    }
    
 }
if(isset($_POST['submit'])) {
    $conn = new PDO($dsn, $username, $password);
    $enumber = $_POST['examnumber'];
    $ecnumber = $_POST['examcentre'];
    foreach($ids as &$id)
    {
        array_push($answers, $_POST['q'+$id]);
        $dbanswers= implode("//", $answers);
    }
    if(empty($enumber) or empty($ecnumber))
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
