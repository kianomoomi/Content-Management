<template>
  <div class="new-doc-content">
    <h3 class="mt-3">Create document content</h3>
    <b-row class="doc-content-management">
        <b-col>
        <div class="label-container">
            <label for="title">Enter your title</label>
        </div>
        <b-form-input id="title" v-model="title"></b-form-input>
        </b-col>
    </b-row>
    <b-row class="doc-file-input mt-3">
        <b-col>
        <div class="label-container">
            <label for="file">Upload your file</label>
        </div>
            <input 
            class="form-control" 
            type="file" 
            id="file" 
            accept=".pdf,.doc,.docx,.xml,.xlsx,.txt" 
            />
        </b-col>
    </b-row>
        <b-row class="doc-file-input mt-3">
        <b-col>
        <div class="label-container">
            <label for="attachment">Upload your attachment</label>
        </div>
            <input 
            class="form-control" 
            type="file" 
            id="attachment" 
            accept=".pdf,.doc,.docx,.xml,.xlsx,.txt" 
            />
        </b-col>
    </b-row>
    <b-row v-for="i in newFields" :key="i" class="mt-3 new-content-info">
    <b-col sm="3" class="field-title">
        <div class="label-container">
            <label for="field">Enter your field</label>
        </div>
        <b-form-input 
        id="field"
        v-model="diffrentFields[i]['field']"
        >
        </b-form-input>
    </b-col>
    <b-col sm="8" class="field-text">
        <div class="label-container">
            <label for="value">Enter your value</label>
        </div>
        <b-form-input 
        id="value"
        v-model="diffrentFields[i]['value']" 
        >
        </b-form-input>
    </b-col>
    </b-row>
    <div class="mt-4 add-field-button">
        <b-button variant="dark" @click="addNewField()" class="add-attribute-btn">
            <!-- <font-awesome-icon icon="fa-solid fa-plus"/> -->
            add attribute
        </b-button>
        <b-button variant="dark" @click="submitDocContent()">
            submit
        </b-button>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            diffrentFields: {
                1: {"field": '', "value": ''},
            },
            newFields: 1,
            title: ''
        }
    },
  methods: {
      addNewField(){
          this.newFields = this.newFields + 1;
          this.diffrentFields[this.newFields] = {"field" : '', "value": ''};
      },
  }
}
</script>

<style scoped>
.doc-content-management{
    margin-left: 70px !important;
    margin-top: 50px !important;
}
.doc-file-input {
    margin-left: 70px !important;
}
.new-doc-content {
    width: 80%;
    height: 100%
}
.new-content-info{
    margin-left: 55px !important;
    margin-right: -40px !important;
}
.add-field-button {
    text-align: right;
}
.delete-field-button {
    margin-left: -20px !important;
}
.field-title {
    margin-right: 40px !important;
    margin-left: 15px !important;
}
.submit-button {
    position: relative;
}
input {
    border-radius: 30px;
    outline: none !important;
}
input:focus {
    box-shadow: inset 0 -1px 0 #ddd;
    outline: none !important;
    border:1px solid #ccc !important;
}
button:focus, button:hover, button:active {
    outline: none !important;
}
.label-container {
    text-align: left;
    margin-left: 8px;
    margin-bottom: 3px;
}
.add-attribute-btn {
    margin-right: 5px;
}
</style>