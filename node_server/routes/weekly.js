
const express = require('express');

const changes = require('../controller/changes.js')

const router = express.Router()

router.get('/weekly', changes.change('week1'))

module.exports = router;