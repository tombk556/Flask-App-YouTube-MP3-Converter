// Select the form element
const form = document.querySelector('form');
const url = document.getElementById('url').value;
const title = document.getElementById('title').value;
const artist = document.getElementById('artist').value;
const URL = '/send';

const handleSubmit = async (e) => {
  e.preventDefault();
  
  const url = document.getElementById('url').value;
  const title = document.getElementById('title').value;
  const artist = document.getElementById('artist').value;
  
  // clear the textarea input
  form.reset();
  fetch(URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url, title, artist }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Server not response');
      }
    })
    .then((data) => {
      console.log('Response:');
      console.log(data);
    })
    .catch((error) => {
      alert(error.message);
    });
};

// Add an event listener to the form when it is submitted
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();
  handleSubmit(event);
});
