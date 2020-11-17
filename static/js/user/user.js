// // 创建数据，使用POST方法
// axios.post(url, data).then(good).catch(bad);

axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val();

function login_api(){
        var url = "login"
        let data = new URLSearchParams()
        var email = document.getElementById("login_email").value
        var password = document.getElementById("login_passwd").value
        data.append('email', email)
        data.append('password', password)

        axios.post(url,data).then(res=>{
        if (res.data.code == 1){
            console.log("登录成功")
            window.location.assign("center")
        }else{
            console.log(res.data)
            msg = res.data.msg
            // window.location.href="center"
            // this.close_loading()
            alert(msg)
        }
        }).catch(function(err){
            // this.close_loading()
            console.log(err)
            alert("登录失败，请刷新页面重试")
        });
}
function register_api(){
    var url = "register"
        let data = new URLSearchParams()

        var name = document.getElementById("register_name").value
        var password = document.getElementById("register_passwd").value
        var email = document.getElementById("login_email").value
        var passwd_c = document.getElementById("register_passwd_c").value

        if(passwd_c != password){
            alert("两次输入的密码不一致")
            return
        }
        data.append('username', name)
        data.append('password', password)
        data.append('email', email)
        axios.post(url,data).then(res=>{
        if (res.data.code == 1){
            this.page_tools_data = res.data.data
            this.page_total =  Number(res.data.total)
            // console.log(this.page_tools_data)
        }else{
            // this.close_loading()
            // alert("加载数据异常，请刷新重试")
        }
        }).catch(function(err){
            // this.close_loading()
            console.log(err)
            // alert("加载数据失败，请刷新重试")
        });
}



$("#login_btn").click(function(){
    login_api()
});

$("#register_btn").click(function(){
    register_api()
});