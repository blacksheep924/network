let counter = 1;


document.addEventListener('click', function(event) {
  if (event.target.id === 'next') {
    next_page();
  }
  if (event.target.id === 'previous') {
    previous_page()
  }
  
});


async function next_page() {
    const name = document.querySelector('#name').textContent;
    counter++;
    
    let posts = document.querySelector('#body');
    posts.value ='';
    response =  await fetch(`/following/${name}/?page=${counter}`)
    htmlContent =  await response.text();
    
    posts.innerHTML = htmlContent;
    

}

async function previous_page() {
  const name = document.querySelector('#name').textContent;
  counter--;

  let posts = document.querySelector('#body');
  response =  await fetch(`/following/${name}/?page=${counter}`)
  htmlContent =  await response.text();
  
  posts.innerHTML = htmlContent;
  
}