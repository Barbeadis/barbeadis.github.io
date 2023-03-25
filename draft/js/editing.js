const MIME_TYPE = 'text/plain';

function save_positions() {
    pos = ""
    $("#images").children().each(function() {
        style = getComputedStyle(this);
        pos += "#" + this.id + " ";
        pos += "{top: " + style.top + "; left: " + style.left + ";}";
        pos += "\n";
    });
    console.log(pos);

    $("#saveLink").remove();
    var a = document.createElement('a');
    var bb = new Blob([pos], {type: MIME_TYPE});
    a.id = "saveLink";
    a.href = window.URL.createObjectURL(bb);
    a.download = "barbeadis_pos.css";
    a.textContent = 'Download ready';
    a.dataset.downloadurl = [MIME_TYPE, a.download, a.href].join(':');
    $(".header").append(a);
}

function enable_editing() {
    $("body").css('background', "white");
    $("body").css('background-image', 'url("img/grid.png")');
    $("body").css('background-repeat', "repeat");
    $("#images img").draggable();
    $("#images p").draggable();
    $("#showPositions").click(save_positions);
}

function init() {
    /* $("#showPositions").click(enable_editing); */
}

$(init);

