
const express = require('express');

const front = require('../controller/front')

const router = express.Router();

router.get('/', front.front);
router.post('/', front.postfront);

router.get('/upload', front.upload);
router.post('/upload', front.uploaded);

module.exports = router;
