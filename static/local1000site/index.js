    function repOver(obj) {
        for (i = 0; i < rep_list.length; i++) {
            rep_list[i].addEventListener("mouseover", mOver);
        }
    }

    var rep_list;

    function onLoad() {
        rep_list = document.getElementsByClassName("rep_list");
        repOver(null);
    }

    function mOver(event) {
        document.getElementById("img_container").style.display = "block";
        document.getElementById("repertory").style.display = "none";
        if (event.target.className==='rep_list') {
            var index = event.target.children[0].attributes.aindex.value;
            var picname = event.target.children[0].attributes.apicname.value;
            var imgNode = document.getElementById("quick_img");
            imgNode.src="/static/source/" + index + "/" + picname;
        }
    }

    function mDown(obj) {
        for (i = 0; i < rep_list.length; i++) {
            rep_list[i].removeEventListener("mouseover", mOver);
        }
        document.getElementById("img_container").style.display = "none";
        document.getElementById("repertory").style.display = "block";
        document.getElementById("repertory").innerHTML = "";
        var local1000Req = new Request("/local1000/picContentAjax/?id=" + obj.children[0].attributes.rep_id.value)
        fetch(local1000Req)
            .then(function(resp){
                return resp.json();
            })
            .then(function(resp) {
                console.log(resp);
                var repName = resp.dirName;
                for (var i = 0; i < resp.pics.length; i++) {
                    document.getElementById("repertory").appendChild(document.createElement("img"));
                }
                resp.pics.forEach((pic, index) => {
                    fetch(`/static/source/${repName}/${pic}`).then(function(response) {
                        return response.blob();
                    }).then(function(blob) {
                        var objectURL = URL.createObjectURL(blob);

                        var img = document.getElementById("repertory").children[index];
                        img.id=pic;
                        img.src = objectURL;
                    });
                });
            });
    }
