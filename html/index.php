<?php
include('index.html');
function testfun()
{
    error_log('INVALID INPUT ON USER LOGIN', 3);
   
}
if(array_key_exists('submit',$_POST)){
   testfun();
}
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
    

    $sql = $conn->prepare("INSERT INTO students VALUES (234567, 'TEST13');");
    
        $sql->execute();
     
?>
