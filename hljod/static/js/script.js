function play_audio(){
    console.log("playing");
    document.getElementById('audio').play()
}


function randomWord() {
    $.get( "/get_word", function( data ) {
        word = data['word'];
        file_name = data['file_name'];
        file_parts = file_name.split("_");
        file_src = '/static/mp3/'+file_parts[0]+'/'+file_name+'.mp3';
        $("#word").text(word);
        $("#audio").attr('src', file_src);
    });

}

$(function(){

    randomWord();
    $("#next_word").on("click", randomWord);
    $("#play_audio").on("click", play_audio);

});