async function sleep(s) {
    await new Promise(resolve => {
        setTimeout(() => {
            resolve(function()  {
                return ("sleeping for " + s + " seconds");
            }());
        }, s)
    }).then((d) => {
        console.log(d)
    })
}
sleep(100)