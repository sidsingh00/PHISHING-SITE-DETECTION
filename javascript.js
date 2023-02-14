const path = require('path');
const post =8000;
const db = require('./db/config');
const Contact = require('./contact/contact');
const { appendFile } = require('fs');


function myFunction(x) {
    x.classList.toggle("mdi:eye-off");
  }

var  contact =[{
  username:'sidharth',
  password:'12345'
},
{
  username:'ayushi',
  password:'123456',
},
{
  username :'bhai',
  password:'123456778',
},
]
var app = document.getElementsByClassName('username');
app.post('/login',function(req,res){
  Contact.create({
    username: req.body.username,
    password: req.body.password
  },
  function(err,newContact){
    if(err){
      console.log('error in  create the a contact!'); return;};

     console.log('*******',newContact);
     return res.redirect('back');
  });
})