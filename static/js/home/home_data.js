function Movies_Vue(){
    new Vue({
        el: "#movies",
        mixins: [],
        delimiters: ["[[", "]]"],
        data(){
            return{

                movies_data:[],
            }
        },
        methods: {

            movie_infos(){
                var url = "movies/m_api"
                var infos_list=[]
                // var self = this

                axios.get(url).then(res=>{
                    if (res.data.code == 1){
                        // items = res.data.data || [];
                        // for (let item of items){
                        //     infos_list.push(item);
                        // }
                        this.movies_data = res.data.data
                        console.log(this.movies_data)
                    }else{
                        alert("加载数据异常，请刷新重试")
                    }
                }).catch(function(err){
                    // console.log(err);
                    alert("加载数据失败，请刷新重试")
                });
            },
        },

        created() {
            this.movie_infos();
        },

    });
}

function Life_Vue(){
    new Vue({
        el: "#life",
        mixins: [],
        delimiters: ["[[", "]]"],
        data(){
            return{
                life_data_up:[],
                life_data_down:[],
            }
        },
        methods: {

            life_infos(){
                var url = "life/l_api"
                var infos_list=[]
                // var self = this

                axios.get(url).then(res=>{
                    var index = 0
                    if (res.data.code == 1){
                        items = res.data.data || [];
                        for (let item of items){
                            if(index <= 2){
                                this.life_data_up.push(item);
                            }else{
                                this.life_data_down.push(item);
                            }
                            index+=1
                        }
                        // this.movies_data = res.data.data
                        console.log(this.life_data_up)
                        console.log(this.life_data_down)
                    }else{
                        alert("加载数据异常，请刷新重试")
                    }
                }).catch(function(err){
                    console.log(err);
                    alert("加载数据失败，请刷新重试")
                });
            },
        },

        created() {
            this.life_infos();
        },

    });
}

function Tools_Vue(){
    new Vue({
        el: "#tools",
        mixins: [],
        delimiters: ["[[", "]]"],
        data(){
            return{

                tools_data:[],
            }
        },
        methods: {
            tools_infos(){
                var url = "tools/t_api"
                var infos_list=[]
                // var self = this

                axios.get(url).then(res=>{
                    if (res.data.code == 1){
                        // items = res.data.data || [];
                        // for (let item of items){
                        //     infos_list.push(item);
                        // }
                        this.tools_data = res.data.data
                        console.log(this.tools_data)
                    }else{
                        alert("加载数据异常，请刷新重试")
                    }
                }).catch(function(err){
                    // console.log(err);
                    alert("加载数据失败，请刷新重试")
                });
            },
        },

        created() {
            this.tools_infos();
        },

    });
}

function Content_Vue(){
    new Vue({
        el: "#banner",
        mixins: [],
        delimiters: ["[[", "]]"],
        data(){
            return{

                banner_data:[],
            }
        },
        methods: {
            banner_infos(){
                var url = "content/c_api"
                // var infos_list=[]
                // var self = this

                axios.get(url).then(res=>{
                    if (res.data.code == 1){
                        // items = res.data.data || [];
                        // for (let item of items){
                        //     infos_list.push(item);
                        // }
                        this.banner_data = res.data.data
                        console.log(this.banner_data)
                    }else{
                        alert("加载数据异常，请刷新重试")
                    }
                }).catch(function(err){
                    // console.log(err);
                    alert("加载数据失败，请刷新重试")
                });
            },
        },

        created() {
            this.banner_infos();
        },

    });
}

$(function() {
    Movies_Vue()
    Life_Vue()
    Tools_Vue()
    Content_Vue()
})