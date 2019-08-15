// Make Pop-up on click
function clickPopup() {
	alert('test');
}


// Select image by clicking on card
function selectImage(img_num_str) {
	//var tmp_str = 'Image ' + toString(Number(img_num))
	console.log('img_num_str',img_num_str)
	var tmp_str = 'Image ' + img_num_str + ' selected'
	alert(tmp_str);
}

var server_address = 'http://127.0.0.1:5002/grab_images'

var request = new XMLHttpRequest()

request.open('GET', server_address, true)

request.onload = function() {
  // Begin accessing JSON data here
  if (request.status >= 200 && request.status < 400) {
    var data = JSON.parse(this.response)
    var img_dict = JSON.parse(data)
    console.log('img_dict', img_dict)
    console.log("img_dict['0'].img_base64",img_dict['0'].img_base64)
    document.getElementById("card-img1").src = img_dict['0'].img_base64;
    document.getElementById("card-img2").src = img_dict['1'].img_base64;
    document.getElementById("card-img3").src = img_dict['2'].img_base64;
    document.getElementById("card-img4").src = img_dict['3'].img_base64;
    
    document.getElementById("card-title1").innerHTML = img_dict['0'].img_date;
    document.getElementById("card-title2").innerHTML = img_dict['1'].img_date;
    document.getElementById("card-title3").innerHTML = img_dict['2'].img_date;
    document.getElementById("card-title4").innerHTML = img_dict['3'].img_date;
    
    document.getElementById("card-text1").innerHTML = img_dict['0'].img_name;
    document.getElementById("card-text2").innerHTML = img_dict['1'].img_name;
    document.getElementById("card-text3").innerHTML = img_dict['2'].img_name;
    document.getElementById("card-text4").innerHTML = img_dict['3'].img_name;

    document.getElementById("spinner").toggleAttribute('hidden');
    document.getElementById("form").toggleAttribute('hidden');
  } else {
    error_message = "Server Error - Try Refreshing Page"
    alert(error_message)
  }
}

request.send()

