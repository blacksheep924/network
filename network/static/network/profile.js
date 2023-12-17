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
    
    const csrftoken = getCookie('csrftoken');

    const response = await fetch(`/profile/${profile}/follow`,{
    method: 'POST',
    
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,  // Include the CSRF token in the headers
      },
    
  })
  if (response.ok){
    button = document.querySelector('#follow');
    const numberer = document.querySelector('#numberer');
    
  const data = await response.json();
  console.log(data.message);
  if (data.message === 'User followed') {
    const number = document.querySelector('#getnumber')
    const textContent = number.textContent;
    const integerValue = parseInt(textContent, 10);
    button.value = 'Followed';
    button.style.background = 'green';
    number.textContent = `${integerValue + 1} `;

  }
    else{
      const number = document.querySelector('#getnumber')
      const textContent = number.textContent;
      const integerValue = parseInt(textContent, 10);
      button.value = 'Unfollowed';
      button.style.background = 'red';
      number.textContent = `${integerValue - 1}`;

    }

  }
  }



  

  
  


 
