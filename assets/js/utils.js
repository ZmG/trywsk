/** Simple utils for pages **/

function addAnchors(div){
    //loop through all your headers
    $.each($('h2'),function(index,value){
        //append the text of your header to a list item in a div, linking to an anchor we will create on the next line
        var label = this.innerHTML;
        var prettyLabel = label.split(/ +/).join("-");
        console.log(prettyLabel);
        $('#'+div).append('<li><a href="#'+prettyLabel+'">'+$(this).html()+'</a></li>');
        //add an a tag to the header with a sequential name
        $(this).html('<span id="'+prettyLabel+'">'+$(this).html()+'</span>');
    });
}
