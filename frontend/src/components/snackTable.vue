<template>
  <el-table
    :data="tableData"
    stripe>
   <el-table-column
      prop="name"
      label="零食"
      sortable>
    </el-table-column>
    <el-table-column
      prop="hot"
      label="热度"
      sortable
      width="180">
    </el-table-column>
  </el-table>
</template>

<script>
  export default {
    name: "snackTable",
    data() {
      this.getGroupedSnack()
      return {
        tableData: []
      }
    },
    methods: {
      getGroupedSnack () {
        let vm  = this
        this.$axios.get('/getGroupedSnack')
          .then((result) => {
          vm.tableData = result.data.data
        })
      }
    }
  }
</script>

<style scoped>

</style>
