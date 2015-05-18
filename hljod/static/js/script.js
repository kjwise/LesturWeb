var words = Array(
    'Mamma',
    'Pabbi',
    'Gunnar',
    'Ég',
    'Þú',
    'Hann',
    'Hún',
    'Leika',
    'Leikskóli',
    'Amma',
    'Afi',
    'Og',
    'Eða',
    'Vera',
    'Að',
    'Í',
    'Á',
    'Það',
    'Sem',
    'Hafa',
    'Barn',
    'Bróðir',
    'Systir',
    'Skór',
    'Sokkar',
    'Hundur',
    'Köttur',
    'Bangsi',
    'Bíll',
    'Ýta'
);

function randomWord() {
    var word = words[Math.floor(Math.random()*words.length)];

    // jQuery methods go here...
    $("#word").text(word);
}

$(function(){

    randomWord();
    $("#nextWord").bind("click", randomWord);

});