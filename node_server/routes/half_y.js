
const express = require('express');

const changes = require('../controller/changes.js')

const router = express.Router()

router.get('/half_year', changes.change('month6'))
router.post('/half_year', changes.postchange('month6'))

module.exports = router;

