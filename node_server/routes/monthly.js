

const express = require('express');

const monthly_change = require('../controller/monthly_change.js')

const router = express.Router()

router.get('/monthly', monthly_change.monthly)

module.exports = router;

