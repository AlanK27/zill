
const express = require('express');

const half_y_change = require('../controller/half_y_change.js')

const router = express.Router()

router.get('/half_year', half_y_change.half)

module.exports = router;

