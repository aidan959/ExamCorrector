//CODE IS EXECUTED ON THE LOAD OF THE TEXT FILE!
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
  /**var questions =
    [
      { id: 111, question: "How many Sustainable Development Goals are there?" },
      { id: 112, question: "What did the Millennium Development Goals tackle?" },
      { id: 121, question: "Using the information on the webpage, complete the following sentences: In the world () million go hungry everyday. This includes more than million children who are under five years of age." },
      { id: 122, question: "What is the world’s biggest health problem?" },
      { id: 123, question: "What does Sustainable Development Goal 2 aim to do by 2030" },
      { id: 131, question: "What is needed to reach Sustainable Development Goal 2?" },
      { id: 141, question: "Your CSPE class would like to invite a person from Concern to come to talk to your class about world hunger. Describe two steps that your class would have to take to organise the visit. <br> First Step:" },
      { id: 142, question: "Second Step:" },
      { id: 151, question: "Buzz Aldren, the astronaut who was the second man to walk on the moon, said,“If we can conquer space we can {onquer world hunger.”Your CSPE class wants to have a debate with this title.Give one argument in favour of this {oint of view and one argument against. Argument in favour:" },
      { id: 152, question: "Argument against" }
    ]
  */
  
  fillPage(LoadFile());
  $('.questions').hide();
  $('.loader').hide();
  $('#examination').on('keyup keypress', function(e) {
      var numItems = $('.empty').length
      if ($('#examcentre').val() && $('#examnumber').val()){
        $('.questions').show();
        $('.loader').show();
      }
      else{
          $('.questions').hide();
          $('.loader').hide();
      }
      if(numItems>0){
          $('.loader').hide();
      }
      else{
          $('.loader').show();
      }
      var keyCode = e.keyCode || e.which;
      if (keyCode === 13) { 
        e.preventDefault();
        return false;
      }
  });
   $('.field input').keyup(function() {
        
        var empty = false;
        $('.field input').each(function() {
            $('input').each(function () {
                if ($.trim($(this).val()) == '') {
                    isValid = false;
                    $(this).addClass('empty');
                } else {
                    $(this).removeClass('empty');
                }
            });
            
        });

        if (empty) {
            $('#submit input').prop('disabled', true);
        } else {
            $('#submit input').prop('disabled', false);
        }
    });
}






