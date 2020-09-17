const async = require('async');

const Db = require('../model/DB');

const items_per_page = 20;


exports.changes = function(param) {
    var app = param.app;
    var param2 = options.param2


    (req, res, next) => {
    const page = +req.query.page || 1;
    const page_number = parseFloat(page);
    let aeg;

    async.series([

        function(callback) {
            Db.db_size('---------')
            .then((res) =>{
                aeg = parseFloat(Object.values(res[0][0])[0])
                callback();
            });
        },
       
        function(callback) {
            Db.fetchA('---------', (page_number-1)*items_per_page,  items_per_page)
            .then((rows) => {
                res.render('front/change', {
                    productz: rows[0],
                    pageTitle: '---------',
                    path: '/---------',
                    hasNextPage: items_per_page * page_number < aeg,
                    hasPreviousPage: page_number > 1,
                    nextPage: page_number + 1,
                    previousPage: page_number - 1,

                    hasNext2Pages: (items_per_page * (page_number + 1)) < aeg,
                    hasPrevious2Pages: (page_number - 1 )> 1,
                    next2Page: page_number + 2,
                    previous2Page: page_number - 2,
                    
                    lastPage: Math.ceil(aeg/ items_per_page),
                    currentPage: page_number,
                    maxpage: Math.floor(page_number/items_per_page) +1
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
