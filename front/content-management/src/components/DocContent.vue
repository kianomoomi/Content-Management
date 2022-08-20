<template>
  <div class="container">
  <h2>{{title}}</h2>
    <a href="title_1_A_Untitled_Document.pdf" download>Download</a>
  <ul class="responsive-table">
    <li class="table-header">
      <div class="col col-1">Field</div>
      <div class="col col-2">Value</div>
    </li>
    <li v-for="(k, v) in extra" :key="k" class="table-row">
      <div class="col col-1">{{k}}</div>
      <div class="col col-2"> {{v}}</div>
    </li>
  </ul>
</div>
</template>

<script>
export default {
    props: {
        title: String,
    },
    data(){
        return{
            extra: {
            "f2": "v2",
            "f1": "v1",
            "f3": "v1",
            "f4": "v1",
            "f5": "v1",
            "f6": "v1",
            "f7": "v1",
            "f8": "v1",

            }
        }
    }

}
</script>

<style scoped>
.container {
  margin-top: 100px;
  max-width: 1000px;
  padding-left: 10px;
  padding-right: 10px;
  margin-left: 65px;
}
h2 {
  font-size: 26px;
  margin: 20px 0;
  text-align: center;
}
h2 small {
  font-size: 0.5em;
}
.responsive-table {
    height: 50px;
}
.responsive-table li {
  border-radius: 3px;
  padding: 25px 25px;
  display: flex;
  justify-content: space-between;
  margin-bottom: 25px;
}
.responsive-table .table-header {
  background-color: #080710;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: #fff;
}
.responsive-table .table-row {
  background-color: #ffffff;
  box-shadow: 0px 0px 9px 0px rgba(0, 0, 0, 0.1);
}
.responsive-table .col-1 {
  flex-basis: 10%;
}
.responsive-table .col-2 {
  flex-basis: 90%;
}
.responsive-table .col-3 {
  flex-basis: 25%;
}
.responsive-table .col-4 {
  flex-basis: 25%;
}
</style>