var register = (data, redirect_url) => {
    fetch('http://localhost:8000/users/insert_user/', {
        method: 'POST', // or 'PUT'
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify(data)
    }).then(res => {
        console.log(res.json())
        window.location.href(redirect_url);
    })
}


var get_users = () => {
    fetch('http://localhost:8000/users/get_users/', {
        method: 'GET', // or 'PUT'
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    }).then(res => {
        console.log(res.json())
    })
}

var get_user_detail = () => {
    fetch('http://localhost:8000/users/get_user_detail/1/', {
        method: 'GET', // or 'PUT'
        headers: new Headers({
            'Content-Type': 'application/json'
        })

    }).then(function(response) { return response.json();
    }).then(function(data) {
        console.log(data)
        $("#inputEmail").val(data[0]['email'])
        $("#firstName").val(data[0]['first_name'])
        $("#lastName").val(data[0]['last_name'])

    });
}

var update_user = (data) => {
    fetch('http://localhost:8000/users/update_user/1', {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify(data)
    }).then(res => {
        console.log(res.json())
    })
}

var login = (data) => {
    fetch('http://localhost:8000/users/login/', {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify(data)
    }).then(res => {
        console.log(res.json())
    })
    // .catch(error => console.error('Error:', error))
    // .then(response => console.log('Success:', response));
}
