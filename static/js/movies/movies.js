tooglePage1();

function tooglePage1() {
	setTimeout(() => $('.covers').toggleClass('loaded'), 600);
}

var $covers = $('.covers');
var scroll = 0;
var delta = 267;

function doScroll(scrollUp = false) {
	var listHeight = getComputedStyle(document.querySelector('ul.covers')).getPropertyValue('height');

	if(!scrollUp && scroll < parseInt(listHeight) - delta*2) {
		scroll += delta;
		$covers.removeClass('up')
			.find('li').css('transform', `translateY(-${scroll}px)`);
	}

	if(scrollUp && scroll >= delta) {
		scroll -= delta;
		$covers.addClass('up')
			.find('li').css('transform', `translateY(-${scroll}px)`);
	}
}

var link_url = ""
function movies_emby(el){
	//新开一个标签页面
	 window.open(link_url+el,'_blank');

	//当前页面打开
	// window.location.assign(link_url+el)
}

function movies_infos(){
	var url = "/movies/infos_api"
	var covers_infos_str=""
	// console.log(url)
	axios.get(url).then(res=>{
		if (res.data.code == 1){
			var movies_data = res.data.data
			link_url = res.data.link_url

			console.log(movies_data)
			for(data in movies_data){
				let movies_title = movies_data[data].original_title
				let movies_infos = movies_data[data].movies_infos
				let path = movies_data[data].img_path
				let link = movies_data[data].link
				console.log(link)
				covers_infos_str +="<li data-index="+data+" onclick='movies_emby("+link+")'><img style='background-image: url(../"+path+")'><span>"+movies_title+"</span><small>"+movies_infos+"</small></li>"
			}
		$('.covers').html(covers_infos_str);
		}else{
			alert("加载数据异常，请刷新重试")
		}
	}).catch(function(err){
		console.log(err);
		alert("加载数据失败，请刷新重试")
	});
}

movies_infos()



function emby_login(){
	url="http://localhost:8096/emby/Users/authenticatebyname?X-Emby-Client=Emby%20Web&X-Emby-Device-Name=Chrome&X-Emby-Device-Id=432a0794-9cfe-45bd-b39d-7b287e606db3&X-Emby-Client-Version=4.5.2.0"
}





