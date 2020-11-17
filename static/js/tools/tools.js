function Tools_Vue(){
    new Vue({
        el: "#tools",
        mixins: [Pagination_mixin],
        delimiters: ["[[", "]]"],
        data(){
            return{
                top_show:0,
                page_tools_data:[],
                tools_loading:false,
                res_innner : "",
                detail_data:{},

            }
        },
        methods: {
            tools_page_infos(page){
                var url;
                if(page){
                     url = "/tools/page_api?page="+page
                }else{
                     url = "/tools/page_api"
                }
                this.open_loading()
                this.top_infos()
                axios.get(url).then(res=>{
                    if (res.data.code == 1){
                        this.page_tools_data = res.data.data
                        this.page_total =  Number(res.data.total)
                        this.close_loading()
                        // console.log(this.page_tools_data)
                    }else{
                        // this.close_loading()
                        this.page_total = 0
                        alert("加载数据异常，请刷新重试")
                    }
                }).catch(function(err){
                    // this.close_loading()
                    this.page_total = 0
                    console.log(err)
                    alert("加载数据失败，请刷新重试")
                });
            },
            handleCurrentChange(page) {
            console.log(`当前页: ${page}`);
            this.tools_page_infos(page)

            },
            open_loading() {
                this.close_topshow()
                this.tools_loading = true;
            },
            close_loading(){
                this.open_topshow()
                this.tools_loading = false;
            },
            open_topshow(){
                this.top_show = 1;
            },
            close_topshow(){
                this.top_show = 0;
            },
            tools_detail(e){
                var id=e.currentTarget.getAttribute("name")
                console.log(id)
                this.open_detail()
                this.open_loading()
                this.tools_detail_infos(id)
                this.close_loading()
            },
            open_detail(){
                var modal = document.querySelector(".modal");
                modal.className += "  is-open"
                modal.style.backgroundColor="rgba(51, 51, 51, 0.5)";
            },
            close_detail(){
                var modal = document.querySelector(".modal");
                modal.className = "modal"
                modal.style.backgroundColor="";
            },
            top_infos() {
                this.res_innner = ""
                var top_url = "/tools/top_api"
                axios.get(top_url).then(res => {
                 if (res.data.code == 1){
                     var candidates = res.data.data;

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

                        this.res_innner += div
                     }

                 }else{
                     alert("加载数据失败，请刷新重试")
                 }
                 }).catch(function(err){
                    // console.log(err);
                    alert("失败，请刷新重试")
                 })

            },

            tools_detail_infos(id){
                detail_url = "/tools/detail_api?tid="+id
                axios.get(detail_url).then(res => {
                 if (res.data.code == 1){
                     this.detail_data = res.data.data;
                 }else{
                     alert("加载数据失败，请刷新重试")
                 }
                 }).catch(function(err){
                    // console.log(err);
                    alert("失败，请刷新重试")
                 })
            },
            tools_download(){

            },
        },
        created() {
            this.tools_page_infos();
        },

    });
}

// window.onload = function(){
    Tools_Vue()
// }


