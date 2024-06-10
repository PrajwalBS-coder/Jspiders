let a=[1,2,3,4,5,6,"nhy",8]
sum=0;
/*for (let i=0;i<a.length;i++){
    if(a[i]%a[i]==0){
        sum=sum+a[i]
    }
}
console.log(sum);
let re=a.filter((ele)=>{
    if(ele%ele==0){
        return ele
    }
})
console.log(re.reduce((a,ele)=>{
    //return a+ele;
    
        return a+ele
    

},0)
)console.log(a.reduce((ac,ele)=>{
    //return a+ele;
    if(typeof(ele)=="number"){
        return ac+ele
    }

},0))
a.reduce((ac,ele)=>{
    //return a+ele;
    
        if(ele!=undefined)
        {
           console.log(ac)
        }
    

},1)
let re=a.filter((ele)=>{
    if(typeof(ele)=="number"){
        return ele
    }
})


console.log(re)
console.log(a.reduce((ac,ele)=>{
    //return a+ele;
    
    if(typeof(ele)== Number()){
    
    }
    
//console.log(sum)
},0))

let ab=23;
let sb="bana";
if(typeof ab=="number") 
    console.log(ab)


*/
let k=a.reduce((ac,item,ele)=>{
    //return a+ele;
    
   if(typeof(ele)=="number"){
        console.log(`${ac} ${item}`)
      return ac+ele
    }
    //console.log(`${ac} ${item}`)
    //return ac+ele
//console.log(sum)
},0)
console.log("output",k)
