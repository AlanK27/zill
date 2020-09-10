
const path = require('path');

const express = require('express');

const front = require('../controller/front')

const router = express.Router();


router.get('/', front.front);

module.exports = router;

