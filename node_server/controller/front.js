
var Db = require('../model/DB');

exports.front = (req, res, next) => {
    console.log('front page');
    Db.fetchAll()
        .then((rows) => {
            console.log(rows[0])
            res.render('front/front', {
                productz: rows[0],
                pageTitle: 'main table',
                path: '/'
            })

        })
        .catch(err => console.log(err));
};
