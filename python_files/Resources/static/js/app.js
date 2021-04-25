//function to reset the form inputs to blank
$(document).ready(function(){
    $(".button_reset").click(function(){
        $("#client")[0].reset()
    })
})





























// $(document).ready(function(){
//     $(".button_reset").click(function($form){
//         $form.find('input:text, input:password, input:file, select, textarea').val('');
//         $form.find('input:radio, input:checkbox')
//         .removeAttr('checked').removeAttr('selected');
//     })
// })