let counter = 1;

document.addEventListener('DOMContentLoaded', function() {
  
   
  load_post();  
  
    
  });

  document.addEventListener('click', function(event) {
    if (event.target.id === 'next') {
      next_page();
    }
    if (event.target.id === 'previous') {
      previous_page()
    }
  });

  
  
  async function load_post() {
    let textarea = document.querySelector('textarea');
    textarea.innerHTML = '';
    
    
    let posts = document.querySelector('#posts');

    let response = await fetch(`/listing?page=${counter}`)
    let htmlContent = await response.text();
    

    
    posts.innerHTML = htmlContent;
    
    
    }
    
    async function next_page() {
      
        
     
        counter++;
      
        let posts = document.querySelector('#posts');
        posts.value ='';
        response =  await fetch(`/listing?page=${counter}`)
        htmlContent =  await response.text();
        
        posts.innerHTML = htmlContent;
        console.log(counter);
        
    
    

    }

    async function previous_page() {
      
        
     
      counter--;

    
      let posts = document.querySelector('#posts');
      response =  await fetch(`/listing?page=${counter}`)
      htmlContent =  await response.text();
      
      posts.innerHTML = htmlContent;
      console.log(counter);
      
  
  

  }

 
  
  


    
    





  