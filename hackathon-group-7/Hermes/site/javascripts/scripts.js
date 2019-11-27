var arrPosicoes = [];
var dictImagePosicao = [];
function imageToBase64(img) {
    var canvas, ctx, dataURL, base64;
    canvas = document.createElement("canvas");
    ctx = canvas.getContext("2d");
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);
    dataURL = canvas.toDataURL();
    base64 = dataURL.replace(/^data:image\/png;base64,/, "");
    return base64;
}

function getGravidadeLabel(gravidade_id){
    switch(gravidade_id){
        case 1 : 
            return "Intacto";
        case 2 :
            return "Leve";
        default :
            return  "Intacto";
    }
}
function getPosicaoLabel(label){
    return label.replace("_" , " ");
}
function showloader() {
    $(".loader_wrapper").fadeIn(1000);
}

function hideloader() {
    $(".loader_wrapper").fadeOut(1000);
}
function setPosicoes(posicao, objImage) {
    var pos = posicao.toLowerCase().replace(" ", "_");
    dictImagePosicao.push({
        "id": objImage.attr('id'),
        "posicao": pos,
        "index": objImage.data("index")
    });
    arrPosicoes.push(pos);
}
function indexImages(images) {
    images.map((idx, img) => {
        $(img).attr('data-index', idx);
    });
}


function getImages(objImages) {
    if (!objImages && arrPosicoes.length == 0) return false;
    $(".imgsCompare").empty();
    objImages.map((item) => {
        let arrImage = dictImagePosicao.filter(function (elem) {
            return elem.posicao.indexOf(item.POSICAO) > -1;
        });
        try {
            let idx = arrImage[0].index;
            $("<img>")
                .attr("src", location.href + "images_cloudant/" + item.DSC_IMAGEM)
                .bind("click",showCompImages)
                .bind("load", function () {
                    $(this).css("border", "2px solid #827e7e");
                    $(this).parent().removeClass("linear-background");
                })
                .bind('error', function (e) {
                    console.log('image error: ' + this.src);
                    $(this).css("border", "2px solid #827e7e");
                    $(this).attr("src", "images/sem_foto.png");

                })
                .addClass("img-responsive")
                .appendTo($(".imgsCompare[data-index = " + idx + "]"))
                .parent().addClass("linear-background")
                .append("<span class='resultSpan'><b>Posição : <span class \"ucwords\">" + item.POSICAO + "</span><br>Gravidade : " +getGravidadeLabel(item.GRAVIDADE) + "<br> Score : " + parseFloat(item.SCORE.replace(",", ".")).toFixed(3) + "</b></span>");

        } catch (err) {
            console.log(err);
        }
    });
}



function resetView(clearSelectedImgs) {
    if (clearSelectedImgs) {
        $(".spartan_remove_row").each(function () {
            $(this).click();
        });
        images_count = 0;
    }
    $(".imgsCompare").empty();
    $("#body_sinistros").empty();
    $("#warning-message").hide();
    $("#tbCfgCategoria").hide();
}

function showCompImages(){
    console.log('Entrou na Função showCompImages');
    $("#img-right").empty();
    $("#img-left").empty();
    var imgRight = $(this);
    var index = imgRight.parent().data('index');
    var imgLeft = $(".img_[data-index=" +index + "]");
    $('<img>')
        .attr('src',imgLeft.attr('src'))
        .addClass("img-responsive")
        .css("border", "2px solid #827e7e")
        .appendTo($("#img-left"));
    $('<img>')
        .attr('src',imgRight.attr('src'))
        .addClass("img-responsive")
        .css("border", "2px solid #827e7e")
        .appendTo($("#img-right"));  
        $("#cmpImages").modal("show");
}
function hideCompImages(){
    console.log('Entrou na Função hideCompImages');
}