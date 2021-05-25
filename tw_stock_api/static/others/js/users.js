var register = (data, redirect_url) => {
    $.ajax({
        type: "POST",
        url: "http://appworks.octave.vip/users/insert_user/",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (returnData) {
            console.log(returnData);
            alert('註冊成功')
            window.location.href = redirect_url
        },
        error: function (returnData) {
            console.error('Error')
            alert('error')
        },
    })
}


var get_users = () => {
    $.ajax({
        type: "GET",
        url: "http://appworks.octave.vip/users/get_users/",
        contentType: "application/json",
        success: function (returnData) {
            console.log(returnData);
        },
        error: function (returnData) {
            console.error('Error')
        },
    })
}


var get_user_detail = (user_id) => {
    $.ajax({
        type: "GET",
        url: "http://appworks.octave.vip/users/get_user_detail/"+user_id,
        contentType: "application/json",
        success: function (data) {
            console.log(data);
            $("#inputEmail").val(data[0]['email'])
            $("#firstName").val(data[0]['first_name'])
            $("#lastName").val(data[0]['last_name'])
        },
        error: function (returnData) {
            console.error('Error')
        },
    })
}

var update_user = (data, user_id) => {
    $.ajax({
        type: "POST",
        url: "http://appworks.octave.vip/users/update_user/"+user_id,
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (returnData) {
            console.log(returnData);
            alert('修改成功');
        },
        error: function (returnData) {
            console.error('Error');
            alert('error');
        },
    })
}

var login = (data, redirect_url) => {
    $.ajax({
        type: "POST",
        url: "http://appworks.octave.vip/users/login/",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (returnData) {
            console.log(returnData);
            window.location.href = redirect_url
        },
        error: function (returnData) {
            console.error('Error')
            alert('error')
        },
    })
}

var update_secret_key = (user_id) => {
    $.ajax({
        type: "POST",
        url: "http://appworks.octave.vip/users/update_secret_key/"+user_id,
        contentType: "application/json",
        success: function (returnData) {
            console.log(returnData);
            $("#inputSecretKey").val(returnData.secret_key)
        },
        error: function (returnData) {
            console.error('Error')
            alert('error')
        },
    })

}

var get_secret_key = (user_id) => {
    $.ajax({
        type: "GET",
        url: "http://appworks.octave.vip/users/get_secret_key/"+user_id,
        contentType: "application/json",
        success: function (data) {
            console.log(data);
            $("#inputSecretKey").val(data[0]['secret_key'])
        },
        error: function (returnData) {
            console.error('Error')
        },
    })
}