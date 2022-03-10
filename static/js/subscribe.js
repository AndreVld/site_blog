window.onload = function () {
    $('.user_info').on('click','input[type="button"]',function (){
        let t_href = event.target;

        $.ajax({
            url: '/users/subscribe/' + t_href.name ,
            success:function(data) {
                $('.btn_sub').val(data.result);

            }
        });
        event.preventDefault();
    })
}