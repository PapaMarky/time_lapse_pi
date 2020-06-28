function get_preview() {
    console.log('get_preview()');
    var rot = document.getElementById("rot").value;
    var exposure = document.getElementById("exposure").value;
    var awb = document.getElementById("awb").value;
    var sh = document.getElementById("sh").value;
    var co = document.getElementById("co").value;
    var br = document.getElementById("br").value;
    var sa = document.getElementById("sa").value;
    var ifx = document.getElementById("ifx").value;
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
	    var arr = JSON.parse(xhttp.responseText)
	    console.log('Got response: ' + xhttp.responseText);
	    document.getElementById("cmd_text").innerHTML = "<pre>" + arr.command + "<br/>Status: " + arr.status + "<br/>output: '" + arr.output + "'</pre>"
	    document.getElementById("preview").src = "/static/preview.png?r="+new Date().getTime();
	}
    };
    var url = "snapshot?br="+br+"&rot="+rot+"&ex="+exposure+"&awb="+awb+"&sh="+sh+"&co="+co+"&br="+br+"&sa="+sa+"&ifx="+ifx;
    
    xhttp.open("GET", url, true);
    xhttp.send();
}
