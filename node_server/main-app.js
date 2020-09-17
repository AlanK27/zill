
const path = require('path');
const bodyParse = require('body-parser');
const express = require('express');
const error = require('./controller/404');
const db = require('./util/db/mysql_db')

const mainpage = require('./routes/front');
const weekly_change = require('./routes/weekly')
const monthly_change = require('./routes/monthly')
const half_y_change = require('./routes/half_y')
const search = require('./routes/search')


const app = express();


app.set('view engine', 'pug')
app.set('views', 'views');

app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParse.urlencoded({ extended: true}));


app.use(mainpage);
app.use(weekly_change)
app.use(monthly_change)
app.use(half_y_change)
app.use(search)

app.use(error.error);

app.listen(8800, () => {
    console.log('active on port 8800')
});
