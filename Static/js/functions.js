function alertFunction(){
        alert("Do you really want to log out?");
    }
function copyText() {
		var copyText = document.getElementById("CopyCode");
		copyText.select();
		copyText.setSelectionRange(0, 99999)
		document.execCommand("copy");
		alert("Promo " + copyText.value + " copied!");
	}
	
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/voucherMe/like_business/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});