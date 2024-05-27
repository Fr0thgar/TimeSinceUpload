function updateCounter(lastUploadTime){
    const now = new Date();
    const elapsed = now - lastUploadTime;
    const days = Math.floor(elapsed / (1000 * 60 * 60 * 24));
    const hours = Math.floor((elapsed % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((elapsed % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((elapsed % (1000 * 60)) / 1000);

    document.getElementById('counter').innerHTML = 
    `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
}