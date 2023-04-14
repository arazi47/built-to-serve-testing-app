window.addEventListener('load', function () {
        var table = document.getElementById("gbentries-table");
        var rows = table.getElementsByTagName("tr");
        for (i = 1; i < rows.length; i++) {
            var row = table.rows[i];
            row.onclick = function(myrow){
                              return function() {
                                 document.getElementById("id-input").value = myrow.getElementsByTagName("td")[0].innerHTML;
                                 document.getElementById("username-input").value = myrow.getElementsByTagName("td")[1].innerHTML;
                                 document.getElementById("comment-input").value = myrow.getElementsByTagName("td")[2].innerHTML;
                                 document.getElementById("posted-on-input").value = myrow.getElementsByTagName("td")[3].innerHTML;
                          };
                      }(row);
        }
});