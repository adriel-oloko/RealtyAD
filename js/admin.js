var cnt = 0;
var arr = [];

function add_image() {
    var sbl = document.getElementById('sbl_content').innerHTML;
    cnt=cnt+1;
    document.getElementById('sbl_content').innerHTML = sbl+'<div id="'+cnt+'"style="margin-left: 5%; width: 90%; background-image: linear-gradient(to bottom right, #313a56, #e7edff); ; padding: 15px; border-radius: 8px; margin-top: 15px;"><img id="img_'+cnt+'" style="width: 20%; height: auto; vertical-align: middle; text-align: left; margin-right: 70%; border-radius: 8px;" /><span class="fa fa-minus" style="font-size: larger; font-weight: 900; vertical-align: middle; text-align: right;" onclick="remove_image('+cnt+');"></span></div>';


    var preview = document.getElementById('img_'+cnt);
    var file = document.getElementById('upload_file').files[0];
    var reader = new FileReader;

    reader.onloadend = function() {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
    }

    arr.push(document.getElementById('upload_file').files[0].name);
    document.getElementById('img_list').value = arr;
    uploadFile();
}

function remove_image(id) {
    document.getElementById(id).style.display = 'None';
    delete arr[id-1];// = null;
    document.getElementById('img_list').value = arr;
}

function uploadFile() {
    xhr = new XMLHttpRequest();
    var file = document.getElementById('upload_file').files[0];
    var formData = new FormData;
    formData.append('file', file, file.name);

    xhr.open("POST", '/image-upload', true);
    //xhr.setRequestHeader("Content-Type", "multipart/form-data; boundary=abc");
    xhr.send(formData);
}