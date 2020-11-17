let switchCtn = document.querySelector("#switch-cnt");
let switchC1 = document.querySelector("#switch-c1");
let switchC2 = document.querySelector("#switch-c2");
let switchCircle = document.querySelectorAll(".switch__circle");
let switchBtn = document.querySelectorAll(".switch-btn");
let aContainer = document.querySelector("#a-container");
let bContainer = document.querySelector("#b-container");
let allButtons = document.querySelectorAll(".submit");
let body = document.querySelector("body");

let changeForm = (e) => {
    switchCtn.classList.add("is-gx");
    setTimeout(function(){
        switchCtn.classList.remove("is-gx");
    }, 1500);

    switchCtn.classList.toggle("is-txr");
    switchCircle[0].classList.toggle("is-txr");
    switchCircle[1].classList.toggle("is-txr");

    switchC1.classList.toggle("is-hidden");
    switchC2.classList.toggle("is-hidden");
    aContainer.classList.toggle("is-txl");
    bContainer.classList.toggle("is-txl");
    aContainer.classList.toggle("is-z200");
};


let mainF = (e) => {
    // for (var i = 0; i < allButtons.length; i++)
    //     allButtons[i].addEventListener("click", getButtons );
    for (var i = 0; i < switchBtn.length; i++)
        switchBtn[i].addEventListener("click", changeForm);


    var password = document.getElementsByName('password');
    var confirm_password = document.getElementsByName("confirm_password")[0];
    var index_num = 0

    for (let i = 0; i < password.length; i++){
        password[i].addEventListener('focus', function(){
            document.getElementById("img_left").style.display= "none" ;
            document.getElementById("img_right").style.display= "block" ;
        });

        password[i].addEventListener('blur', function(){
            document.getElementById("img_left").style.display= "block" ;
            document.getElementById("img_right").style.display= "none" ;
        });
    }

    confirm_password.addEventListener('focus', function(){
            document.getElementById("img_left").style.display= "none" ;
            document.getElementById("img_right").style.display= "block" ;
    });

    confirm_password.addEventListener('blur', function(){
            document.getElementById("img_left").style.display= "block" ;
            document.getElementById("img_right").style.display= "none" ;
    });


};


window.addEventListener("load", mainF);

