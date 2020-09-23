
const express = require('express');

const changes = require('../controller/changes.js')

const router = express.Router()

router.get('/monthly', changes.change('month1'))

module.exports = router;