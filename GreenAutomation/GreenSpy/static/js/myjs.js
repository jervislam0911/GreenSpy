$(document).ready(function() {
    setInterval(update,1000);
});



//update real time data using Ajax.

function update(){
    $.getJSON("/data/", function(data){
        $.each(data, function(){
            $("#content").html("<p> Light value is " + this.Light + "</p>");
        });
    });
};

