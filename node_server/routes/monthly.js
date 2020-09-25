
const express = require('express');

const changes = require('../controller/changes.js')

const router = express.Router()

router.get('/monthly', changes.change('month1'))
router.post('/monthly', changes.postchange('month1'))

module.exports = router;