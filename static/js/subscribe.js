window.onload = function () {
    $('.user_info').on('click','input[type="button"]',function (){
        let t_href = event.target;
        console.log(t_href.name);

        $.ajax({
            url: '/users/subscribe/' + t_href.name ,
            success:function(data) {
                console.log(data.result);
                $('.btn_sub').val(data.result);

            }
        });
        event.preventDefault();
    })
}