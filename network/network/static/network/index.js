document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archive').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#submit').addEventListener('click', submit_email);
  
  // By default, load the inbox
  load_mailbox('inbox');
 


});

function compose_email() {
  //document.querySelector('#emails-form').innerHTML = "";
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
 // archived(mailbox);

}

function emails_list(mailbox) {

  
const element = document.createElement('div');
element.innerHTML = '';
element.id='emails-form';

document.querySelector('#emails-view').append(element);

  
 // document.querySelector('#emails-form').innerHTML = "";
  const ur = '/emails/' + mailbox;
  fetch(ur)
    .then(response => response.json())
    .then(emails => {
      // Вивести листи в консоль
      console.log(emails);


      // ... зробити з листами щось інше ...
      for (let email of emails) {

       
        st_row = document.createElement('div');
        st_row.className = "row";
        st_row.id =email.id+'st'
        
       
        let button_div = document.createElement('button');
        button_div.type = "button";
        button_div.id = email.id;

        button_div.addEventListener('click', function () {
          console.log(button_div.id);
          console.log(email.read, email.archived)
        });
        
        
        //document.addEventListener('click', event => {

          // Знайти, що було натиснуто
       //   const element = event.target;
      
         // // Перевірити, чи користувач натиснув кнопку приховати
        //  if (element.className === 'Archived') {
        //    console.log(button_div.id);
         //    archived(boolArch, button_div.id);
         //     element.parentElement.remove()
        //  }
          
     // });
        new_row = document.createElement('div');
        new_row.className = "row";
        new_row.id = 'row ' + email.id;
       
        new_col_1 = document.createElement('div');
        new_col_1.className = "col-4";

        new_col_4 = document.createElement('div');
        new_col_4.className = "col-2";

        if (mailbox === 'sent') {
          ncol_1 = `${email.recipients}`;
          butText = 'btn btn-light col-12';
          new_col_4.innerHTML = ``
          
        }
        else {


          if (email.archived = 'false') {
            mailbox ='inbox';
            console.log(mailbox, email.archived );
    textArch='Архівувати';
    boolArch='true'
          }
          else {
            mailbox = 'archive';
            console.log(mailbox, email.archived );
    textArch='Розархівувати';
    boolArch='false'
           
          }

          if (email.read = 'false') {

            butText = 'btn btn-outline-secondary  col-8';
            //console.log(email.id, email.read, butText);
          }
          else {
            butText = 'btn btn-light  col-8';
           // console.log(email.id, email.read, butText);
          }

          ncol_1 = `${email.sender}`;

          new_col_4.innerHTML = `<button type="button" id=mail.id class='Archived' onclick="archived(boolArch,button.id)">${textArch}</button>`
         
         // button_arch.innerHTML = textArch;
  
         // document.querySelector('#emails-view').append(button_arch);
         
        }

       // button_div.className = butText;
        //console.log(button_div.className)
        //document.querySelector('new_row').append(new_col_1);
        //document.getElementById(button_div.id).appendChild(new_row);
        button_div.append(new_row);
        
        new_col_1.innerHTML = `${ncol_1}`;

        document.querySelector('#emails-form').append(st_row);
        st_row.append(button_div);
        st_row.append(new_col_4);
       // new_row.append(new_col_0)
       new_row.append(new_col_1);

        new_col_2 = document.createElement('div');
        new_col_2.className = "col-4";
        new_col_2.innerHTML = `${email.subject}`;
        
        new_row.append(new_col_2);
        //document.getElementById(new_row.id).appendChild(new_col_2);

        new_col_3 = document.createElement('div');
        new_col_3.className = "col-3";
        //let options = { day: 'numeric',month: 'long'};
        let options = { day: 'numeric', month: 'numeric', year: 'numeric' };
        let date = new Date(Date.parse(email.timestamp)).toLocaleString('UA', options);
        //console.log(date);
        new_col_3.innerHTML = `${date} `;
        //arch_col_2.innerHTML=`${textArch}`;
        new_row.append(new_col_3);
        //new_col_0.innerHTML=`<button type="button" class=${butText} >`+new_col_0.innerHTML+`</button>`
       // new_row.append(new_col_4);

       // document.getElementById(new_row.id).appendChild(new_col_3);
        //document.getElementById(new_row.id).appendChild(new_col_4);
        // Додати новий елемент до невпорядкованого списку:


        //my_div = document.getElementById("{email.id}");
        //document.body.insertBefore(newDiv, my_div);


      };

     

    });

    //button_arch.addEventListener('click', function () {
      
      //console.log(textArch, boolArch, checkArchs);
     // archived(boolArch, checkArchs);

       
   // });
 
}





function archived() {
  console.log(id);
  email_id=id;
  console.log(email_id);

  //document.getElementById(element.id+'st').remove()
  fetch('/emails/<int:email_id>', {
    method: 'PUT',
    body: JSON.stringify({
        archived: boolArch
    })
  })
  
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
