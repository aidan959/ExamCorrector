<html>
<head>
    <title>Results</title>
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="shortcut icon" type="image/x-icon" src="favicon.ico" />
    <script src="https://code.jquery.com/jquery-1.11.0.min.js"></script>
    
</head>
<body>
<input type="text" id="search" placeholder="Type to search">
<?php
$servername = gethostname();
$dsn = 'mysql:host=localhost;dbname=s4u155_examcorrector;charset=utf8';
$username = "s4u155";
$password = "devKycBu";

// Create connection
$conn = new PDO($dsn, $username, $password);
$sth = $conn->prepare("SELECT * FROM students ORDER by results DESC"); //You don't need a ; like you do in SQL
$sth->execute();
$result = $sth->fetchall();
?>
<table id= "table" class="table table-bordered">
<th>Exam Number</th>
<th>Exam Centre</th>
<th>Answers</th>
<th>Marks</th>
<?php

foreach($result as $row){ //Creates a loop to loop through results]
    echo "<tr><td>" . $row[0] . "</td><td>" . $row[1] . "</td> <td>";

    $marksplit = str_split($row[5]);
    $answersplit = explode("//", $row[2]);
    $answercount = count(str_split($row[5]));;
    $markcount = count(explode("//", $row[2]));
    
    for ($n=0; $n<$answercount; $n++) {
        echo $answersplit[$n] . " ";
        echo $marksplit[$n] ." - Marks<br>";
    
                
    }
    echo "</td> <td>" . $row[3]*100 . "% </tr>";  //$row['index'] the index here is a field name
}

echo "</table>"; //Close the table in HTML
$link = null; //Make sure to close out the database connection

?>
</body>
<script>
        var $rows = $('#table tr');
    $('#search').keyup(function() {
        var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
        
        $rows.show().filter(function() {
            var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
            return !~text.indexOf(val);
        }).hide();
});
    </script>
</html>