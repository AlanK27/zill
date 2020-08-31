

exports.error = (req, res, next)=> {
    res.status(404).render('404',
    {pageTitle: '404'},
    console.log('404')
    );
};


