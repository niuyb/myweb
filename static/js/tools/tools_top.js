
function Leaderboard() {
    // var self = this;
    var top_url = "/tools/top_api"

    var res_el=document.getElementById("results")
    console.log(res_el)
    var end_innerhtml = ""

    axios.get(top_url).then(res => {
         if (res.data.code == 1){
             var candidates = res.data.data;

             // console.log(candidates)
             // var el_num=document.getElementById("results")
             // console.log(el_num)
             // if (el_num.childElementCount > 0){
             //     return
             // }

             for(var i = 0,len = candidates.length; i < len; i++){

                var color =  res.data.data[i].color
                var color_b = d3.rgb(color).hsl().brighter(0.8).toString();
                var div;
                var name = res.data.data[i].name;
                var description = res.data.data[i].description;
                var percent = res.data.data[i].percent;

                div = '<div class="candidate" style="background:'+color_b+';">' +
                '<h2 class="candidate__name">'+ name +'</h2>' +
                '<span class="candidate__description">'+description+'</span>' +
                '<span class="candidate__percent">'+percent+'%</span>' +
                '<div class="candidate__bar" style="width: '+percent+'%; background: '+ color+';"></div>' +
                '</div>'

                // $("#results").append(div);
                res_el.innerHTML += div
                end_innerhtml = res_el.innerHTML
                console.log(res_el.innerHTML )
             }
             var res_len=$('#results').children().length;
             if (res_len <= 0){
                 return end_innerhtml
             }

         }else{
             alert("加载数据失败，请刷新重试")
         }
     }).catch(function(err){
        console.log(err);
        alert("失败，请刷新重试")
    })


}


jQuery.fn.wait = function (func, times, interval) {
    var _times = times || -1, //100次
    _interval = interval || 20, //20毫秒每次
    _self = this,
    _selector = this.selector, //选择器
    _iIntervalID; //定时器id
    if( this.length ){ //如果已经获取到了，就直接执行函数
        func && func.call(this);
    } else {
        _iIntervalID = setInterval(function() {
            if(!_times) { //是0就退出
                clearInterval(_iIntervalID);
            }
            _times <= 0 || _times--; //如果是正数就 --

            _self = $(_selector); //再次选择
            if( _self.length ) { //判断是否取到
                func && func.call(_self);
                clearInterval(_iIntervalID);
            }
        }, _interval);
    }
    return this;
}


// $("#btn_comment_submit").wait(function() { //等待#btn_comment_submit元素的加载
//     this.removeClass("comment_btn").addClass("btn"); //提交按钮
//     //这里的 this 就是 $("#btn_comment_submit")
// });