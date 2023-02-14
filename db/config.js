const mongoose = require("mongoose");

mongoose.connect( "mongodb://localhost:27017/contacts_list_db",
  { useNewUrlParser: true }
);
const db = mongoose.connection;
db.on('error',console.error.bind(console,'error connecting to db'));

db.once('open',function(){
  console.log('successfully connected to the database');
});