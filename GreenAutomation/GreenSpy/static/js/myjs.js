var myChart;
$(document).ready(function() {
    $(".power_on").click(function(){
        $("#div1").load("/power_on/");
    });

    $(".power_off").click(function(){
        $("#div1").load("/power_off/");
    });

//    setInterval(update,1000);
    $('.login').addClass('animated fadeInUp');
    $('.signup').addClass('animated fadeInUp');
    $('#logo_pic').addClass('animated flip');
    $('#title, #small_title').addClass('animated zoomIn');
    $('i.fa-facebook, i.fa-github,i.fa-linkedin').hover(function(){
      $(this).addClass('animated rubberBand');
    },function(){
      $(this).removeClass('animated rubberBand');
    });

    $('.arrow').hover(function () {
        $('#aboutUs').fadeIn(300);
    },
        function () {
            $('#aboutUs').fadeOut(300);
    });

    $('a[href^="#"]').on('click', function(event) {
    var target = $('#heading');
    if( target.length ) {
        event.preventDefault();
        $('html, body').stop().animate({
            scrollTop: target.offset().top - $("div.navbar-header").height()- 15
        }, 600);
    }
});

    $('.my-slider').unslider({
//        autoplay: true


    });

    		var clock;

			clock = $('.clock').FlipClock({
		        clockFace: 'HourCounter',
		        autoStart: false,
		        callbacks: {
		        	stop: function() {
		        		$('.message').html('The clock has stopped!')
		        	}
		        }
		    });

		    clock.setTime(26600);
		    clock.setCountdown(false);
		    clock.start();




      var circle1 = new circleDonutChart('example1');
      var circle2 = new circleDonutChart('example2');
      circle1.draw({end:75,start:0, maxValue:100, titlePosition:"outer-top", titleText:"Human Resources Investment", outerCircleColor:'#5FDEF0', innerCircleColor:'#0F93A6'});
      circle2.draw({end:10,start:0, maxValue:300, unitText:'%', titlePosition:"outer-top", titleText:"GreenSpy Automation System", outerCircleColor:'#0085c8', innerCircleColor:'#004081'});
//      document.addEventListener('click', moveAround, false);
      setInterval(moveAround,5000);
      //document.addEventListener('touchstart', moveAround, false);
      function moveAround(){
        var random_val = 100*Math.random();
        circle1.draw( {end:random_val} );
        circle2.draw( {end:random_val/2, unitText:'%', maxValue:100} );
      }

      $('.thumbnail').hover(
        function(){
            $(this).find('.caption').fadeIn(400); //.fadeIn(250)
        },
        function(){
            $(this).find('.caption').fadeOut(400); //.fadeOut(205)
        }
    );


    $("[name='temp-checkbox']").bootstrapSwitch('state', false);
    $("[name='temp-checkbox']").on('switchChange.bootstrapSwitch', function (event, state) {

    if(state == false){ $("#fan").load("/power_off/");}else{
        $("#fan").load("/power_on/");}
});


var temperature = Number($(".temperature").text());
var humidity = Number($(".humidity").text());
var light = Number($(".light").text());
Chart.defaults.global.defaultFontColor = 'white';

var ctx = document.getElementById("myChart");
myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Temperature", "Light", "Humidity"],
        datasets: [{
            label: '# of conditional needs',
            data: [temperature, light, humidity],
            backgroundColor: [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        },

        {
            label: '# of Sensing data',
            data: [temperature, light, humidity],
            backgroundColor: 'rgba(230,220,220,0.5)',
            borderWidth: 1
        },





        ]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});

    setInterval(automation,1000);

});





$(function(){

    setInterval(function(){
        $('#logo_pic').toggleClass('animated flip');
    }, 4000);
});


$('#header #menu li a').hover(function () {
  $(this).fadeOut(0).addClass('hover').fadeIn(300);
},
function () {
  $(this).fadeOut(300)
         .queue(function(){ $(this).removeClass('hover').fadeIn(0).dequeue() });
});



//sensing automation.
function automation(){
    $.getJSON("/data/", function(data){
        $.each(data, function(){
            myChart.data.datasets[1].data[0] = Number(this.Temperature)/17;
            myChart.data.datasets[1].data[1] = Number(this.Light);
            myChart.data.datasets[1].data[2] = Number(this.Humidity)/14;
            myChart.update();
//            if (Number(this.Light) >= 22){
////                  alert("yes");
//                $("[name='light-checkbox']").bootstrapSwitch('state', true);
//            }else{
//                $("[name='light-checkbox']").bootstrapSwitch('state', false);
//            }
            if (Number(this.Temperature)/17 >= 30){
//                  alert("yes");
                $("[name='temp-checkbox']").bootstrapSwitch('state', true);
            }else{
                $("[name='temp-checkbox']").bootstrapSwitch('state', false);
            }

//            if (Number(this.Humidity) >= 29){
////                  alert("yes");
//                $("[name='humi-checkbox']").bootstrapSwitch('state', true);
//            }else{
//                $("[name='humi-checkbox']").bootstrapSwitch('state', false);
//            }

        });
    });
};


//update real time data using Ajax.
//function update(){
//    $.getJSON("/data/", function(data){
//        $.each(data, function(){
//            $("#content").html("<p> Light value is " + this.Light + "</p>" + "<p> temperature value is " + this.Temperature + "</p>"+ "<p> humidity value is " + this.Humidity + "</p>" );
//        });
//    });
//};

//submit login form
$(function(){
    $('#btnSubmit').click(function(e){
        e.preventDefault();
        $('#username , #password, #btnSubmit').addClass('animated fadeOut').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
            function(){$('#welcome').animate({marginTop: $( document ).height()/8}, 2000, function(){
                    $('#loginForm').submit();
            });
        });
    });
});


$(function(){
   var lang = "";
    $(".navbar-nav li a").each(function(){
          if(this.href == window.location){
             lang = $(this).text();
             switch(lang){
                case "Home":
                    $("body").css("background-color","white");
                     break;
                case "Sign up":
                    $('.Logo,#downArrow').hide();
                    break;
                case "Log in":
                    $('.Logo,#downArrow').hide();
                    break;
                case "Plants":
                     $("body").css({"-webkit-animation":"pulse 10s infinite",
                                    "animation":"pulse 40s infinite"
                     });
                     break;
                 }
          }
   });
});


$(function(){
 if (/plant\/[0-9]+/.test(window.location.pathname))
 {$("body").css({"-webkit-animation":"pulse 40s infinite",
                                    "animation":"pulse 40s infinite"
                     });}

});





$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    $(".parallax-two").css("background-position", "0  " + -scroll/6 + "px");

    });


$(function () {
    $(".photo_img").slice(0, 3).show();
    $("#loadMore").on('click', function (e) {
        e.preventDefault();
        $(".photo_img:hidden").slice(0, 3).fadeIn("slow");
        if ($(".photo_img:hidden").length == 0) {
            $("#load").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top - $(".photo_img").height()*2 - $("div.navbar-header").height()
        }, 1500);
    });
});

$('a[href=#top]').click(function () {
    $('body,html').animate({
        scrollTop: 0
    }, 600);
    return false;
});

$(window).scroll(function () {
    if ($(this).scrollTop() > 70) {
        $('.totop a').fadeIn();
    } else {
        $('.totop a').fadeOut();
    }
});

$(function() {
    $('#toggle-one').bootstrapToggle();
 });