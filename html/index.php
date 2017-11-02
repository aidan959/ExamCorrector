<?php
include('index.html');
function testfun()
{
   echo "Your test function on button click is working";
}
if(array_key_exists('submit',$_POST)){
   testfun();
}
?>
