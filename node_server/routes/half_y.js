
const express = require('express');

const changes = require('../controller/changes.js')

const router = express.Router()

router.get('/half_year', changes.change('month6'))

module.exports = router;

