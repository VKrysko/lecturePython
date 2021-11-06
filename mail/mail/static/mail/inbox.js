document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#submit').addEventListener('click', submit_email);
  // By default, load the inbox
  load_mailbox('inbox');



});

function compose_email() {
  document.querySelector('#emails-form').innerHTML = "";
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  emails_list(mailbox);
}

function emails_list(mailbox) {

  document.querySelector('#emails-form').innerHTML = "";
  
  
  const ur = '/emails/' + mailbox;
  fetch(ur)
    .then(response => response.json())
    .then(emails => {
      // Вивести листи в консоль
      console.log(emails);


      // ... зробити з листами щось інше ...
      for (let email of emails) {
        id=email.id;
       // var my_div = newDiv = null;
        element = document.createElement('div');
        element.addEventListener('click', function() {
          console.log(id);
        });
        if (mailbox === 'sent') {
          element.innerHTML = `<a  name="${email.id}">Кому : ${email.recipients} Тема : ${email.subject} - ${email.body} Дата: ${email.timestamp} </a>`;
          element.id= 'element'+ email.id;
          console.log(element.id);
        }
        else {
          element.innerHTML = `<a  name="${email.id}"> Від кого : ${email.sender} Тема:  ${email.subject} - ${email.body} Дата : ${email.timestamp} ${email.archived} </a>`;
          element.id= 'element'+ email.id;
          console.log(element.id);
        }
        // Додати новий елемент до невпорядкованого списку:
        document.querySelector('#emails-form').append(element);
        
        //my_div = document.getElementById("{email.id}");
        //document.body.insertBefore(newDiv, my_div);
     

      }
    });

}


function submit_email() {

  const sender = document.querySelector('#user').textContent;
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;


  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      sender: sender,
      recipients: recipients,
      subject: subject,
      body: body,
      timestamp: Date.now(),
      read: false,
      archived: false
    })
  })
    .then(response => response.json())
    .then(result => {
      // Вивести результат в консоль
      console.log(timestamp);
      console.log(result);
    });


};
