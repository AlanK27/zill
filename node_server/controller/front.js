const async = require('async');

const Db = require('../model/DB');

const items_per_page = 10;


exports.front = (req, res, next) => {
    const page = +req.query.page || 1;
    const pagge = parseFloat(page);
    let aeg;

    async.series([

        function(callback) {
            Db.db_size('today')
            .then((res) =>{
                aeg = parseFloat(Object.values(res[0][0])[0])
                callback();
            });
        },
       
        function(callback) {
            Db.fetchA('today', (pagge-1)*10, 10 )
            .then((rows) => {
                res.render('front/front', {
                    productz: rows[0],
                    pageTitle: 'main table',
                    path: '/',
                    hasNextPage: items_per_page * pagge < aeg,
                    hasPreviousPage: pagge > 1,
                    nextPage: pagge + 1,
                    previousPage: pagge - 1,
                    lastPage: Math.ceil(aeg/ items_per_page),
                    currentPage: pagge,
                    maxpage: Math.floor(pagge/10) +1
                })
            })
            .catch(err => {
                console.log(err);
                const error = new Error(err);
                error.httpStatusCode = 500;
                return next(error);
            })
        }
    ]);
};
