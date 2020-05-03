
console.time('Array initialize')
var a = Array(10000);
for( var i=0;i<10000;i++){
    a[i] = i;
}
console.timeEnd('Array initializea')