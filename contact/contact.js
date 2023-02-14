const mongoose = require('mongoose');
const contactSchema = new mongoose.Schema({
    username:{
        type: String,
        required : true
    },
    password:{
        type: String,
        required: true
    }
});

const Contact = mongoose.model('Contact',contactSchema);

module.exports = Contact;