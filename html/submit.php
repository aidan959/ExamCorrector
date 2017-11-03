<?php
$servername = gethostname();
$dsn = 'mysql:host=localhost;dbname=examcorrector';
$username = "examiner";
$password = "aidan";

// Create connection
$conn = new PDO($dsn, $username, $password);
/*} catch (Exception $e){
    echo "Caught exception: ", $e->getMessage(), "\n";
}*/


//Attempt insert query execution
//if(isset($_POST['submit'])) {
    $enumber = $_POST['examnumber'];
    $ecnumber = $_POST['examcentre'];
    

    $sql = $conn->prepare("INSERT INTO students VALUES (123456, '$examcentre');");
    
        $sql->execute();
     
//}



/*if (isset($_GET['submit'])){
    $txt = "tempanswers.txt"; 
    $fh = fopen($txt, 'w+');
    foreach ($_POST as $key => $value) 
        $body .= $key . '->' . $value . '<br>';
    
    $data = $_POST['field1'] . '-' . $_POST['field2'] . "\n";
    $ret = file_put_contents('/tmp/mydata.txt', $data, FILE_APPEND | LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
        $conn->close();
    }
    else {
        echo "$ret bytes written to file";
        $conn->close();
    }
}*/


 
?>