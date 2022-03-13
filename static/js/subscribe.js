window.onload = function () {
    $('.user_info').on('click','input[type="button"]',function (){
        let t_href = event.target;
        console.log(123);
        console.log(t_href);

        $.ajax({
            url: '/users/subscribe/' + t_href.name ,
            success:function(data) {
                $('.btn_sub').val(data.result);

            }
        });
        event.preventDefault();
    });
}
$(document).ready(function () {
     $('#commentForm').submit(function(e){
         e.preventDefault();


         $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: '/create_comment',
            success:function(response){
              $('.block_comment').html(response.result)
            },
            error: function (response) {
                alert(response.errors);
                console.log(response.errors)
                }
         });

     });
})

