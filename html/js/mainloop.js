var desc=[
    "manhole cover on foothpath on barrog gaa grounds kilbarrack road loose.",
    "Footpath at driveway to 17 Maywood Lawn in bad state of disrepair."
];
function questionList(){
    var full_list = ""
    for(var i=0; i<desc.length; ++i){
        full_list = full_list + desc[i] + '<br>'
    }
    $("#container").text(full_list);     
  }