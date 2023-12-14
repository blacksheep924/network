let counter = 1;




function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }
    

    




document.addEventListener('click', function(event) {
    if (event.target.id === 'next') {
      next_page();
    }
    if (event.target.id === 'previous') {
      previous_page()
    }
    if (event.target.id === 'follow'){
        follow();
    }
  });
 
    async function next_page() {
        const name = document.querySelector('#name').textContent;
        counter++;
        
        let posts = document.querySelector('#body');
        posts.value ='';
        response =  await fetch(`/profile/${name}/?page=${counter}`)
        htmlContent =  await response.text();
        
        posts.innerHTML = htmlContent;
        

    }

    async function previous_page() {
      const name = document.querySelector('#name').textContent;
      counter--;

      let posts = document.querySelector('#body');
      response =  await fetch(`/profile/${name}/?page=${counter}`)
      htmlContent =  await response.text();
      
      posts.innerHTML = htmlContent;
      
  }

  async function follow(){

    const profile = document.querySelector('#name').textContent;
    const follower = document.querySelector('#username').textContent;
    const followed = true;
    const csrftoken = getCookie('csrftoken');

    fetch(`/profile/${profile}/follow`,{
    method: 'POST',
    
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,  // Include the CSRF token in the headers
      },
    
  })
  .then(response => response.json())
}
