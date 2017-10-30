<?php
$servername = gethostname();
$dsn = 'mysql:host=127.0.0.1;dbname=examcorrector';
$username = "examiner";
$password = "password";


include('index.html');
// Create connection
try{
    $conn = new PDO($dsn, $username, $password);
} catch (Exception $e){
    echo "Caught exception: ", $e->getMessage(), "\n";
}


// Attempt insert query execution
try{
$sql = "INSERT INTO students (exam_number, exam_centre) VALUES (111111, 'TEST12')";
} catch (Exception $e){
    echo "Caught exception: ", $e->getMessage(), "\n";
}

if (isset($_GET['submit'])){
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
}


?>
