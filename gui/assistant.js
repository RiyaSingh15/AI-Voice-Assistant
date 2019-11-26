// function to greet according to time
function time() {
    var today = new Date();
    var hour = today.getHours();
    if (hour >= 0 && hour < 12) {
        eel.speak("Good Morning!");
        eel.create_connection();
    }


    else if (hour >= 12 && hour < 18) {
        eel.speak("Good Afternoon!");
        eel.create_connection();
    }


    else {
        eel.speak("Good Evening!");
        eel.create_connection();
    }
}

eel.expose(said);
function said(arg1) {
    document.getElementById("para2").innerHTML = "User Said:" + arg1;
}

eel.expose(bootinfo);
function bootinfo(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10) {
    document.getElementById("para1").innerHTML = "Boot Information <br> Boot Time: " + arg1 + " / " + arg2 + " / " + arg3 + "  " + arg4 + " : " + arg5 + " : " + arg6 + "<br>Total Read: " + arg7 + "<br> Total Write:" + arg8 + "<br> Total Bytes Sent: " + arg9 + "<br>Total Bytes Received: " + arg10 + "<br> Processor: " + arg6;
}

eel.expose(cpuinfo);
function cpuinfo(arg1, arg2, arg3, arg4, arg5, arg6) {
    document.getElementById("para1").innerHTML = "CPU Information <br> Physical cores: " + arg1 + "<br>Total cores: " + arg2 + "<br> Max Frequency:" + arg3 + " Mhz" + "<br> Min Frequency: " + arg4 + " Mhz" + "<br>Current Frequency: " + arg5 + "Mhz" + "<br> Total CPU Usage: " + arg6 + "%";
}

eel.expose(dateinfo);
function dateinfo(arg1, arg2, arg3, arg4) {
    document.getElementById("para1").innerHTML = "Date <br> " + arg1 + " " + arg2 + " " + arg3 + " ," + arg4;
}

eel.expose(memoryinfo);
function memoryinfo(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8) {
    document.getElementById("para1").innerHTML = "Memory Information <br> Total: " + arg1 + "<br> Available: " + arg2 + "<br> Used: " + arg3 + " <br> Percentage: " + arg4 + "%" + "<br>SWAP <br> Total: " + arg5 + "<br> Free: " + arg6 + "<br> Used: " + arg7 + " <br> Percentage: " + arg8 + "%";
}

eel.expose(cmdinfo);
function cmdinfo() {
    document.getElementById("para1").innerHTML = "Opening Command Prompt";
}

eel.expose(dbinfo);
function dbinfo() {
    document.getElementById("para1").innerHTML = "Opening DB Browser";
}

eel.expose(downloadinfo);
function downloadinfo() {
    document.getElementById("para1").innerHTML = "Opening Downloads";
}

eel.expose(bashinfo);
function bashinfo() {
    document.getElementById("para1").innerHTML = "Opening Git-Bash";
}

eel.expose(gitinfo);
function gitinfo() {
    document.getElementById("para1").innerHTML = "Opening Git-Cmd";
}

eel.expose(githubinfo);
function githubinfo() {
    document.getElementById("para1").innerHTML = "Opening GitHub";
}

eel.expose(googleinfo);
function googleinfo() {
    document.getElementById("para1").innerHTML = "Opening Google";
}

eel.expose(psiphoninfo);
function psiphoninfo() {
    document.getElementById("para1").innerHTML = "Opening Psiphon";
}

eel.expose(spotifyinfo);
function spotifyinfo() {
    document.getElementById("para1").innerHTML = "Opening Spotify";
}

eel.expose(stackinfo);
function stackinfo() {
    document.getElementById("para1").innerHTML = "Opening StackOverFlow";
}

eel.expose(videoinfo);
function videoinfo() {
    document.getElementById("para1").innerHTML = "Opening Videos";
}

eel.expose(vscinfo);
function vscinfo() {
    document.getElementById("para1").innerHTML = "Opening VSCode";
}

eel.expose(youtubeinfo);
function youtubeinfo() {
    document.getElementById("para1").innerHTML = "Opening YouTube";
}

eel.expose(xamppinfo);
function xamppinfo() {
    document.getElementById("para1").innerHTML = "Opening Xampp-Control";
}

eel.expose(playinfo);
function playinfo() {
    document.getElementById("para1").innerHTML = "Playing Music";
}

eel.expose(wikiinfo);
function wikiinfo(arg1) {
    document.getElementById("para1").innerHTML = arg1;
}

eel.expose(sysinfo);
function sysinfo(arg1, arg2, arg3, arg4, arg5, arg6) {
    document.getElementById("para1").innerHTML = "System Information <br> System: " + arg1 + "<br>Node Name: " + arg2 + "<br> Release:" + arg3 + "<br> Version: " + arg4 + "<br>Machine: " + arg5 + "<br> Processor: " + arg6;
}

eel.expose(timeinfo);
function timeinfo(arg1, arg2, arg3) {
    document.getElementById("para1").innerHTML = "Time: " + arg1 + " : " + arg2 + " : " + arg3;
}