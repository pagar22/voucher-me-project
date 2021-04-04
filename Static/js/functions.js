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
	
$(document).ready(function() {
	$('#like_btn').click(function() {
		var catecategoryIdVar;
		catecategoryIdVar = $(this).attr('data-categoryid');
		$.get('/voucherMe/like_category/',
			{'category_id': catecategoryIdVar},
			function(data) {
				$('#like_count').html(data);
				$('#like_btn').hide();
			})
		});
});
