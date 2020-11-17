var Pagination_mixin = {
    delimiters: ["[[", "]]"],
    data() {
        return {
        currentPage: 1,
        page_total:20,
        }
    },
    methods: {
      // handleSizeChange(val) {
      //   console.log(`每页 ${val} 条`);
      // },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
      }
    },
}

