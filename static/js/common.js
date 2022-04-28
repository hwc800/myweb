 function checkqx(data) {
     if(data.trim()!=""&& data.replace(/\s+/g,"")!=""&&JSON.parse(data)["code"]==-1){
         layer.msg(JSON.parse(data)["msg"], {
             offset: '15px'
             ,icon: 1
             ,time: 1000
         } );
         return false;
     }else {
         return true;
     }
 }
