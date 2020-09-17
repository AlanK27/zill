

const express = require('express');

const weekly_change = require('../controller/weekly_change')

const router = express.Router()

router.get('/weekly', weekly_change.weekly)

module.exports = router;

