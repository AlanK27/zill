
const path = require('path');
const bodyParse = require('body-parser');

const express = require('express');

const error = require('./controller/404');
const db = require('./util/db/mysql_db')

const mainpage = require('./routes/front');

const app = express();

app.set('view engine', 'pug')
app.set('views', 'views');

app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParse.urlencoded({ extended: true}));

app.use(mainpage);

app.use(error.error);

app.listen(8800);
