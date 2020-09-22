<template>
  <div class="hello">
    <el-select
        v-model="value"
        multiple
        filterable
        allow-create
        default-first-option
        placeholder="请选择小零食" style="width: 400px">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <div style="margin-top: 50px;">
        <el-button size="medium" type="danger" icon="el-icon-dish" @click="snackCommit" circle></el-button>
      </div>
    <el-row>
      <el-col :span="8"><div class="grid-content"></div></el-col>
      <el-col :span="8"><div><snackTable ref="snacks"></snackTable></div></el-col>
      <el-col :span="8"><div class="grid-content"></div></el-col>
    </el-row>
  </div>
</template>

<script>
  import snackTable from './snackTable.vue'
export default {
  name: 'HelloWorld',
  components: {
    snackTable
  },
    data() {
      return {
        options: [{
          value: '牛肉粒',
          label: '牛肉粒'
        }, {
          value: '开心果',
          label: '开心果'
        }, {
          value: '士力架',
          label: '士力架'
        }],
        value: []
      }
    },
    mounted (){
      this.getAllSnack()
    },
    methods: {
      getAllSnack () {
       let vm = this
        this.$axios.get('/getAllSnack')
          .then((result) => {
          vm.options = result.data.data
        })
      },
      snackCommit () {
        let vm = this
        this.$axios.post('/addSnack', {
          snacks: this.value.join(',')
        })
          .then((result) => {
          // this.users = result.data
            if (result.data.status === 1){
              setTimeout(function () {
                vm.getAllSnack()
                vm.$refs.snacks.getGroupedSnack()
              },1000)
            } else {
              alert('很遗憾，添加失败了!')
            }
        })
      }
      // snackCommit() {
      //   alert('你选了这些零食：'+this.value)
      // }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>
