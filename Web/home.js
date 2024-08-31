document.getElementById('clickMe').addEventListener('click', async function() {
    try {
        const response = await fetch('/api/message');
        const data = await response.json();
        alert(data.message);
    } catch (error) {
        console.error('Error fetching the message:', error);
    }
});
