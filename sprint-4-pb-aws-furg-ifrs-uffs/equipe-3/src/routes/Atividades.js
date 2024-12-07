const express = require('express')
const router = express.Router()
const atividadeController = require('./../controllers/AtividadeController')

/**
 * The root rote '/api/atividades/' returns a 
 * formated 'atividade' json on 200 status code.
 */
router.get('/', async (req, res) => {
  const data = await atividadeController.fetchAtividadeData()
  if (data === null) {
    return res.status(500).json({ error: process.env.API_REQUEST_ERROR_MESSAGE })
  }
  const atividadeObject = atividadeController.formatAtividadeData(data)
  return res.status(200).json(atividadeObject)
})

module.exports = { router }