
var newSpeedL = 0;
var newSpeedR = 0;
var start_flag = false;
var normal_speed = 0;
var joyX = 0;
var timerId;
var record_flag = false;
var motor_url;
var minPower = 5;
function set_motor(){
    if (start_flag){
        normal_speed = parseInt(document.getElementById("V").value);

        //validation check
        if (normal_speed > 100) {
            normal_speed = 100;
        }
        //max speed limited to 50
        normal_speed = parseInt(normal_speed/2);

        joyX = parseInt(joy.GetX());

        if (joyX > 100) { joyX = 100;}
        if (joyX < -100) { joyX = -100;}

        
        if (-1 <= joyX && joyX <= 1) { 
            newSpeedL = normal_speed; 
            newSpeedR = normal_speed;
        }

        if (joyX < -1) {
            newSpeedL = minPower+ (normal_speed - minPower) - parseInt((normal_speed-minPower)*(-joyX)/100);
            newSpeedR = normal_speed + parseInt(normal_speed*(-joyX)/100);
        }
        if (joyX > 1) {
            newSpeedL = normal_speed + parseInt(normal_speed*joyX/100);
            newSpeedR = minPower + (normal_speed-minPower) - parseInt((normal_speed-minPower)*joyX/100); 
        }

       
    }
    else{
        newSpeedL = 0; 
        newSpeedR = 0;
    } 

    if (record_flag == true){
        motor_url = "/motor?l=" + newSpeedL.toString() + '&r=' + newSpeedR.toString() + '&joyX=' + joyX.toString() + '&record=' + 'Y'  ;
    }
    else{
        motor_url = "/motor?l=" + newSpeedL.toString() + '&r=' + newSpeedR.toString() + '&joyX=' + joyX.toString() + '&record=' + 'N'  ;
    }

    request.open("GET", motor_url, true);
    request.send(null); 
}    

function set_motor_start(){
    if (start_flag == false) {
        start_flag = true;
        document.getElementById("runId").innerHTML = "Stop";
        timerId = setInterval(function(){ set_motor(); }, 50);
    }
    else {
        start_flag = false;
        document.getElementById("runId").innerHTML = "Start";
        clearInterval(timerId);
        var motor_url = "/motor?l=0&r=0&joyx=" + joyX.toString();
        request.open("GET", motor_url, true);
        request.send(null);
    }

}
function set_record(){
    if (record_flag == false) {
        record_flag = true;
        start_flag = true;
        document.getElementById("recordId").innerHTML = "Recording";
        timerId = setInterval(function(){ set_motor(); }, 50);
    }
    else {
        record_flag = false;
        start_flag = false;
        document.getElementById("recordId").innerHTML = "Record";
        clearInterval(timerId);
        var motor_url = "/motor?l=0&r=0&joyx=" + joyX.toString()+ '&r=' + 'N' ;
        request.open("GET", motor_url, true);
        request.send(null);
    }
    
}


