$(document).ready( function () {

    $("#table_container").hide()
    $("#create_container").hide()

    $("#signup_btn").click(function(){
        console.log("Hey")
        $("#signup_modal_div").modal('show');
    });

    $("#login_btn").click(function(){
        console.log("Hey")
        $("#login_modal_div").modal('show');
    });
});
function login(){
    $("#login_modal_div").modal('hide');
        $.ajax({
            type:"post",
            url:"http://127.0.0.1:8000/login/",
            crossDomain:true,
            contentType: "application/json",
            data:JSON.stringify({
                "username":$("#txt_uname").val(),
                "password":$("#txt_pwd").val()
            }),
            success:function(result){
                console.log("Hello")
                console.log(result);
                $("#login_btn").hide()
                $("#signup_btn").hide()
                $("#table_container").show();
                $("#login_box_section").hide();
                //$('#datatable_main').DataTable();
                console.log(result.access_token)
                localStorage.setItem('access_token', result.access_token);
                localStorage.setItem('username',result.username);
                $.ajax({
                    type:"get",
                    url:"http://127.0.0.1:8000/get_commodities_details/",
                    crossDomain:true,
                    contentType: "application/json",
                    beforeSend: function (xhr) {
                        token = localStorage.getItem('access_token')
                        token_str = 'Bearer ' + token
                        xhr.setRequestHeader('Authorization', token_str);
                    },
                    success:function(result){
                        console.log("Hello")
                        console.log(result);
                        set_data_in_datatable(result)
                        $("#create_container").show()
                    },
                    error:function(result){
                        console.log(result.responseJSON.status_code);
                        alert(result.responseJSON.status_code);
                        //$("#message").text("Wrong Username or PAssword");
                    }
        
                });
            },
            error:function(result){
                console.log(result.responseJSON.status_code);
                alert(result.responseJSON.status_code);
                $("#message").text("Wrong Username or PAssword");
            }

        });
}

function set_data_in_datatable(result){
    var main_arr = new Array()
    for (i=0;i<result.length;i++){
        var arr = new Array()
        arr.push(result[i].commodity_name);
        if (result[i].buy_or_sell == 'B'){
            arr.push("Buy");
        }
        else{
            arr.push("Sell");
        }
        arr.push(result[i].price);
        arr.push(result[i].buy_sell_date);
        main_arr.push(arr);
    }
    $('#datatable_main').DataTable({
        data:main_arr,
        "bDestroy": true,
        columnDefs: [
            {
                "className": "text-center",
                "width": "4%"
           },
           {
            "className": "text-center",
            targets: 4,
            "width": "4%",
            render: function (data, type, full, meta) {                         
                return '<button class="btn"><i class="fa fa-trash"></i></button>';
                  
              }
       }],
    });
}

function submit_form(){
    alert("Hei")
    $("#myModal").modal('hide')
    list = new Array()
    temp_obj = {}
    commodity_id = $("#commodity_dropdown").val()
    commodity_name = $("#commodity_dropdown option:selected").text();
    buy_or_sell = $("#buy_sell option:selected").text();
    price = $("#price_b_s").val()
    date_b_s = $("#date_b_s").val()
    alert(commodity_id)
    alert(commodity_name)
    alert(buy_or_sell)
    alert(price)
    alert(date_b_s)
    temp_obj['commodity_id'] = commodity_id
    temp_obj['commodity_name'] = commodity_name
    if (buy_or_sell == 'Buy'){
        buy_or_sell = 'B'
    }
    else{
        buy_or_sell = 'S'
    }
    temp_obj['buy_or_sell'] = buy_or_sell
    temp_obj['price'] = price
    temp_obj['buy_sell_date'] = date_b_s
    list.push(temp_obj)
    $.ajax({
        type:"post",
        url:"http://127.0.0.1:8000/create_commodities/",
        crossDomain:true,
        contentType: "application/json",
        beforeSend: function (xhr) {
            token = localStorage.getItem('access_token')
            token_str = 'Bearer ' + token
            xhr.setRequestHeader('Authorization', token_str);
        },
        data:JSON.stringify(list),
        success:function(result){
            console.log("Hello")
            console.log(result);
            // set_data_in_datatable(result)
            // $("#create_container").show()
            $.ajax({
                type:"get",
                url:"http://127.0.0.1:8000/get_commodities_details/",
                crossDomain:true,
                contentType: "application/json",
                beforeSend: function (xhr) {
                    token = localStorage.getItem('access_token')
                    token_str = 'Bearer ' + token
                    xhr.setRequestHeader('Authorization', token_str);
                },
                success:function(result){
                    console.log("Hello")
                    console.log(result);
                    set_data_in_datatable(result)
                    //$("#create_container").show()
                },
                error:function(result){
                    console.log(result.responseJSON.status_code);
                    alert(result.responseJSON.status_code);
                    //$("#message").text("Wrong Username or PAssword");
                }
    
            });
        },
        error:function(result){
            console.log(result.responseJSON.status_code);
            alert(result.responseJSON.status_code);
            //$("#message").text("Wrong Username or PAssword");
        }

    });

}

// $(document).ready( function () {

//     $("#register_link").click(function(){
//         $("#login-container").hide()
//         $("#signup_container").show()
//     });
// });


$(document).on("submit", "#signup_form", function(e){
    e.preventDefault();
    alert('it works!');
    username = $("#username").val()
    password = $("#password").val()
    email = $("#email").val()
    mobile = $("#phone_no").val()
    first_name = $("#first_name").val()
    last_name = $("#last_name").val()
    temp_obj = {}
    temp_obj["username"] = username
    temp_obj["password"] = password
    temp_obj["email"] = email
    temp_obj["phone_no"] = mobile
    temp_obj["first_name"] = first_name
    temp_obj["last_name"] = last_name
    $.ajax({
        type:"post",
        url:"http://127.0.0.1:8000/signup/",
        crossDomain:true,
        contentType: "application/json",
        data:JSON.stringify(temp_obj),
        success:function(result){
           console.log(result)
           if (result.status_code=="S100"){
            $("#signup_modal_div").modal('hide');
               $("#signup_success").innerHTML = "SignUp Successfully. Please Login"
           }
        },
        error:function(result){
            console.log(result.responseJSON.status_code);
            alert(result.responseJSON.status_code);
            //$("#message").text("Somethong went wrong");
        }

    });
});

function signup(){
    username = $("#username").val()
    password = $("#password").val()
    email = $("#email").val()
    mobile = $("#phone_no").val()
    first_name = $("#first_name").val()
    last_name = $("#last_name").val()

    if (username == "" || username == undefined){
        var x = document.getElementById("username").required
        document.getElementById("demo").innerHTML = x
    }

    temp_obj = {}
    temp_obj["username"] = username
    temp_obj["password"] = password
    temp_obj["email"] = email
    temp_obj["phone_no"] = phone_no
    temp_obj["first_name"] = first_name
    temp_obj["last_name"] = last_name
    $.ajax({
        type:"post",
        url:"http://127.0.0.1:8000/signup/",
        crossDomain:true,
        contentType: "application/json",
        data:JSON.stringify(temp_obj),
        success:function(result){
           console.log(result)
        },
        error:function(result){
            console.log(result.responseJSON.status_code);
            alert(result.responseJSON.status_code);
            //$("#message").text("Somethong went wrong");
        }

    });
}
