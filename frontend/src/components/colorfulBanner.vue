<template>
  <div class="mod" id="colorful"><a class="inner"></a></div>
</template>

<script>
export default {
  name: 'colorfulBanner',
  data () {
    return {
      // msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>
#colorful {
  position: absolute; /*绝对对位*/
  top: 0%; /*距上部*/
  left: 50%;
  transform: translate(-50%,-50%); /*移动，根据X,Y轴*/
  width: 100%; /*宽*/
  height: 20px; /*高*/
  text-align: center; /*字体水平居中*/
  font-size: 45px; /*字体大小*/
  line-height: 120px; /*行高*/
  color: #fff;
  text-transform: uppercase; /*字体大写*/
  text-decoration: none; /*字体增加装饰：去除下划线*/
  font-family: sans-serif; /*非衬线体*/
  box-sizing: border-box; /*盒模型大小规则*/
  background: linear-gradient(
    90deg,#03a9f4, #f441a5, #ffeb3b,
  #03a9f4, #f441a5, #ffeb3b, #03a9f4, #f441a5, #ffeb3b); /*渐变背景*/
  border-radius: 0; /*边框圆角*/
  background-size: 400%; /*背景大小*/
  z-index: 1; /*层叠定位*/
  animation: animate 8s linear infinite normal;
}
div:hover{
  animation: animate 8s linear infinite normal; /*动画: 名称 时间 线性 循环 播放完回退播放*/
}
@keyframes animate{
  0%{
    background-position: 0%; /*修改背景定位，实现渐变色炫光*/
  }
  25%{
    background-position: 25%;
  }
  50%{
    background-position: 50%;
  }
  75%{
    background-position: 75%;
  }
  100%{
    background-position: 100%;
  }
}

.mod{
    display: flex;
    align-items: center;/*垂直居中*/
    height: 100%;
}
.inner{
    width:100%; /*若为一行文字,同时实现水平居中*/
}
.inner{
    margin: auto; /*实现div水平居中*/
}
</style>
