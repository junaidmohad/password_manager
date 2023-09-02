//Delay function to give typing effect
const sleep = function(n){
    return new Promise((resolve,reject)=>{
        setTimeout(resolve,n)
    });
}
//Executing Typing
const typing = async function(data){
    //main typeWrite function to implement typing effect
    const typeWriter = async function(n=100,id,text){
        const element = document.getElementById(id);
        for (let i=0;i<=text.length;i++){
            element.innerText = text.substring(0,i);
            await sleep(n);
        }
        document.getElementById('cursor').remove();
        return Promise.resolve('Done');
    }
    //Type the heading
    await typeWriter(80,'heading','Did you know...');
//     //Type the data after the heading has been typed
    typeWriter(30,'para',data);
}
//Data to be retrieved will be stored in head and data. Head will always remain the same
const data = `65% more passwords were compromised in 2022 than 2020...
38% of Americans report having at least one of their passwords cracked or guessed...`
typing(data);
