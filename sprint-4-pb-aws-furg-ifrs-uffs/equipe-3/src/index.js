require('dotenv').config({ path: __dirname + "/config/.env" })

const express = require('express')
const app = express()
const PORT = process.env.PORT || 8080
const apiAtividades = require('./routes/Atividades')
const apiPiadas = require('./routes/Piadas')

/*
 * ROOT ROTE responds with "200" status code
 * and a sucess message
 */
app.get('/', (req, res) => {
  res.status(200).send(process.env.ROOT_MSG)
})

/*
 * Define routes for "atividades" API
 */
app.use('/api/atividades/', apiAtividades.router)

/*
 * Define routes for "piadas" API
 */
app.use('/api/piadas/', apiPiadas.router)

/**
 * Any inappropriate use of the '/' route will
 * result in a 404 bad response
 * THIS ROUTE MUST STAYS AFTER ALL OTHER ROUTES
 */
app.get('/*', (req, res) => res.status(404).json({ error: process.env.BAD_REQUEST_MSG }))

app.listen(PORT, () => {
  console.log(`Server running on port ${process.env.PORT}`)
})
