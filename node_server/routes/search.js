

const express = require('express');

const search = require('../controller/search')

const router = express.Router()

router.get('/searches', search.getsearch)
router.get('/search', search.postsearch)
router.post('/search', search.ToCSV)

module.exports = router;
