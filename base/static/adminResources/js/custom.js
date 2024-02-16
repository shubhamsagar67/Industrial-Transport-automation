var globalCounter = 0;

function addData() {
    var tbl = document.getElementById("tbl");
    tbl.style.display = "";

    var state = document.getElementById("transportDetailStateId");
    var city = document.getElementById("transportDetailCityId");

    var row = tbl.insertRow(-1);

    var no = row.insertCell(0);
    var p = row.insertCell(1);
    var q = row.insertCell(2);
    var r = row.insertCell(3);

    globalCounter += 1;

    no.innerHTML = globalCounter;
    p.innerHTML = state.options[state.selectedIndex].text + '<input type="hidden" style="border:hidden" id="stateId" name="transportDetailStateId" value="' + state.options[state.selectedIndex].value + '">';
    q.innerHTML = city.options[city.selectedIndex].text + '<input type="hidden" style="border:hidden" id="cityId" name="transportDetailCityId" value="' + city.options[city.selectedIndex].value + '">';
    r.innerHTML = '<button data-repeater-delete="" type="button" onclick="del(this)" \n' +
        '                                                                class="btn btn-danger btn-sm icon-btn ml-2">\n' +
        '                                                            <i class="mdi mdi-delete"></i>\n' +
        '                                                        </button>'
}

function del(d) {
    var tbl = document.getElementById("tbl");
    var l = d.parentNode.parentNode;
    tbl.deleteRow(l.rowIndex);
}