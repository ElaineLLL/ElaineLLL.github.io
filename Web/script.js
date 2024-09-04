// document.getElementById('clickMe').addEventListener('click', async function() {
//     try {
//         const response = await fetch('/api/message');
//         const data = await response.json();
//         alert(data.message);
//     } catch (error) {
//         console.error('Error fetching the message:', error);
//     }
// });

var color = document.getElementById('color');
color.addEventListener('keypress', async function(event) {
    if (event.key == "Enter"||event.code=="Enter") {
        event.preventDefault();
        try{
            if (color.value.toLowerCase() == "blue") {
                const response = await fetch('/api/blue');
                const data = await response.json();
                alert(data.message);
            }else{
                const response = await fetch('/api/empty');
                const data = await response.json();
                alert(data.message);
            }
        }catch(error){
            console.error('Error fetching the message:', error);
        }
    }
});