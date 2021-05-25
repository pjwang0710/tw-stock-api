var get_tw_stock_info = (user_id) => {
    $.ajax({
        type: "GET",
        url: "http://localhost:8000/stocks/get_api_user_count/"+user_id,
        contentType: "application/json",
        success: function (data) {
            console.log(data);
            $("#apiCount").html(data['count'])
        },
        error: function (returnData) {
            console.error('Error')
        },
    })
}