

const express = require('express');

const search = require('../controller/search')

const router = express.Router()

router.get('/search', search.getsearch)
router.post('/search', search.postsearch)

module.exports = router;
