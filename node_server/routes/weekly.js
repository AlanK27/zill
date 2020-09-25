
const express = require('express');

const changes = require('../controller/changes.js')

const router = express.Router()

router.get('/weekly', changes.change('week1'))
router.post('/weekly', changes.postchange('week1'))

module.exports = router;