// Acc
$(document).on("click", ".naccs .menu div", function() {
    var numberIndex = $(this).index();

    if (!$(this).is("active")) {
        $(".naccs .menu div").removeClass("active");
        $(".naccs ul li").removeClass("active");

        $(this).addClass("active");
        $(".naccs ul").find("li:eq(" + numberIndex + ")").addClass("active");

        var listItemHeight = $(".naccs ul")
            .find("li:eq(" + numberIndex + ")")
            .innerHeight();
        $(".naccs ul").height(listItemHeight + "px");
    }
});


function upload_Vue(){
    new Vue({
        el: "#upload",
        mixins: [],
        delimiters: ["[[", "]]"],
        data() {
          return {
            movies_name: '',
            movies_text:'',
            movies_text_p:'',
            imageUrl: '',
            dialogVisible: false,
            // movies_dialogVisible: false,
            movies_url: '',
            tools_radio:'2',
            image_radio:'6',


          };
        },
        methods: {
        // handleRemove(file, fileList) {
        //   console.log(file, fileList);
        // },
        // handlePictureCardPreview(file) {
        //   this.dialogImageUrl = file.url;
        //   this.dialogVisible = true;
        // },
        reset(){
            this.movies_name= ''
            this.movies_text=''
            this.movies_text_p=''
            this.movies_image=''
            // this.movies_dialogVisible= false
            this.movies_url=''
            console.log("重置")
        },

        submit(){
            console.log("提交")
        },

        handleAvatarSuccess(res, file) {
            this.imageUrl = URL.createObjectURL(file.raw);
          },
          beforeAvatarUpload(file) {
          //   const isJPG = file.type === 'image/jpeg';
          //   const isLt2M = file.size / 1024 / 1024 < 2;
          //
          //   if (!isJPG) {
          //     this.$message.error('上传头像图片只能是 JPG 格式!');
          //   }
          //   if (!isLt2M) {
          //     this.$message.error('上传头像图片大小不能超过 2MB!');
          //   }
          //   return isJPG && isLt2M;
          },
          handleRemove(file, fileList) {
            console.log(file, fileList);
          },
          handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
          },

        },


        created() {
            // this.banner_infos();
        },

    });
}

$(function() {
    upload_Vue()
})
