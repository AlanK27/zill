const async = require('async');
const fastcsv = require('fast-csv');
const fs = require('fs');
const Json2csvParser = require('json2csv').Parser;

const Db = require('../model/DB');

const items_per_page = 20;


exports.front = (req, res, next) => {
    const page = +req.query.page || 1;
    const page_number = parseFloat(page);
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
            Db.fetchA('today', (page_number-1)*items_per_page,  items_per_page)
            .then((rows) => {
                let jsonData = JSON.parse(JSON.stringify(rows[0]));
                res.render('front/front', {
                    productz: rows[0],
                    pageTitle: 'main table',
                    path: '/',
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

exports.postfront = function (req, res) {
    Db.fetchQAll('main')
        .then((result) =>{
            let jsonData = JSON.parse(JSON.stringify(result[0]));
            let json2csvParser = new Json2csvParser({ header: false});
            let csv = json2csvParser.parse(jsonData);
            
            fs.writeFile('name', csv, function(error) {
                if (error) throw error;
                res.setHeader('Content-Type', 'application/csv');
                res.setHeader('Content-Disposition', 'inline; filename = "main_db.csv"');
                res.send(csv)  
            })
        });
};



exports.upload = (req, res) => {
    res.render('front/upload', {
        pageTitle: 'Upload',
        path: '/upload',}
    ) 
};

exports.uploaded = (req, res) => {
    
    let stream = fs.createReadStream(req.file.path);
    let csvData = [];
    let csvStream = fastcsv
        .parse()
        .on('data', function(data) {
            csvData.push(data);
        })
        .on('end', function() {
            Db.insert('main', csvData)
        });
    stream.pipe(csvStream);
};
