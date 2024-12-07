const express = require('express');
const router = express.Router();
const piadaController = require('./../controllers/PiadaController');

/**
 * The root rote '/api/piadas/' returns a 
 * formated 'piada' json on 200 status code.
 */
router.get('/', async (req, res) => {
    const data = await piadaController.fetchPiadaData()
    if (data === null) {
        return res.status(500).json({ error: process.env.API_REQUEST_ERROR_MESSAGE })
    }
    const PiadaObject = piadaController.formatPiadaData(data)
    return res.status(200).json(PiadaObject)

})


module.exports = { router };