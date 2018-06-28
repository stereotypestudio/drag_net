// $(function(){
// 	console.log('I am loading')
// 	$('#search').keyup(function() {
// 		$.ajax({
// 			type: "POST",
// 			url: "/search",
// 			data: { 
// 				'search_text' : $('#search').val(),
// 				'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
// 			},
// 			success : searchSuccess,
// 			dataType: 'html'
// 		});

// 	});
// 	console.log("test")
// });

// function searchSucess(data, textStatus, jqXHR) {
// 	$('#search-results').html(data);
// }

$(document).ready(function(){
		$('.comment-form').submit(function(event){
			event.preventDefault();
			$.ajax({
				url: '/comment/submit-comment/',
				method: 'post',
				data:$(this).serialize(),
				success:function(response){
					$('.comments').append(`<p>Comment: ${response.content}</p>`);
					$('form')[0].reset();
				}
			});
		});
});

	$( document ).ready( function() {
    	$( '#q' ).keyup( function() {
    		q = $( '#q' ).val();
    		$( '#results' ).html( '&nbsp;' ).load( '/search?q=' + q );
    	});
	});

